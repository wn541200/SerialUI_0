import queue
import threading
import time
from PyQt5.QtCore import *


class DBJProtocol(QObject):
    START = b'NB'

    voltageChanged = pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.responses = queue.Queue()
        self.events = queue.Queue()
        self.lock = threading.Lock()
        self.buffer = bytearray()
        self.action = {
            30: self.code_30_function
        }

    def clear(self):
        self.responses.put('')
        del self.buffer[:]

    def command(self, transport, command, response='OK', timeout=1):
        uart_write_and_wait_respond_thread = threading.Thread(target=self._run_event, args=(transport, command, timeout))
        uart_write_and_wait_respond_thread.start()

    def _run_event(self, transport, command, timeout):
        start = time.time()
        with self.lock:
            transport.write(command)
            while True:
                try:
                    r = self.responses.get(timeout=timeout)
                    if r == b'OK':
                        return
                except queue.Empty:
                    print('下位机未响应命令')
                    break

        end = time.time()
        print(end-start)

    def on_uart_event(self, data):
        self.buffer.extend(data)
        if b'NB' in self.buffer:
            start = self.buffer.index(b'N')
            try:
                data_len = self.buffer[start+4]
                packet = self.buffer[start:start+5+data_len+1]
                del self.buffer[:start+5+data_len+1]
                self.parse_received_packet(packet)
                self.responses.put(b'OK')
            except Exception as e:
                print(e)

    def parse_received_packet(self, packet):
        print(packet)
        print('function code:' + str(packet[4]))

        code = int(packet[4])
        if code in self.action:
            func = self.action[code]
            data_len = int(packet[5])
            if data_len > 0:
                data = packet[6:6+data_len]
            else:
                data = None
            func(data)
        else:
            print('功能码未实现：' + str(packet[4]))

    def code_30_function(self, data):
        print(data)
        if data is not None:
            battery_total_voltage = int(data[0] | (data[1] << 8))
            self.voltageChanged.emit('voltage', battery_total_voltage)
            print(battery_total_voltage)


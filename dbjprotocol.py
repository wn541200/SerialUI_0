import queue
import threading
import time
import serial


class DBJProtocol():
    START = b'NB'

    def __init__(self):
        self.responses = queue.Queue()
        self.events = queue.Queue()
        self.lock = threading.Lock()
        self.buffer = bytearray()

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

    def packet_parse(self, packet):
        print(packet)

    def on_uart_event(self, data):
        self.buffer.extend(data)
        if b'NB' in self.buffer:
            start = self.buffer.index(b'N')
            try:
                data_len = self.buffer[start+4]
                packet = self.buffer[start:start+5+data_len+1]
                del self.buffer[:start+5+data_len+1]
                self.packet_parse(packet)
                self.responses.put(b'OK')
            except Exception as e:
                print(e)


        # print(self.buffer)



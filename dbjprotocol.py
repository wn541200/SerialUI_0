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
        self.packet = bytearray()

    def clear(self):
        self.responses.put('')
        del self.packet[:]

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

    def packet_parse(self, data):
        pass

    def on_uart_event(self, data):
        self.packet.extend(data)
        if b'NB' in self.packet:
            self.responses.put(b'OK')
            print('xxxx')


        print(self.packet)



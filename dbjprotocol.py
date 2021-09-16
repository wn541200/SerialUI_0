import queue
import threading
import time
from PyQt5.QtCore import *


class DBJProtocol(QObject):
    START = b'NB'

    voltageChanged = pyqtSignal(str, int)
    port_send_request_signal = pyqtSignal(bytes)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.responses = queue.Queue()
        self.events = queue.Queue()
        self.lock = threading.Lock()
        self.buffer = bytearray()
        self.action = {
            30: self.code_30_function
        }
        self.function_map = {
            'cell_over_voltage': [40, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'cell_under_voltage': [41, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'total_over_voltage': [42, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'total_under_voltage': [43, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'discharging_over_current': [44, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'charging_over_current': [45, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'soc_over_threshold': [46, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'soc_under_threshold': [47, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'discharging_over_temperature': [48, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'charging_over_temperature': [49, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'discharging_under_temperature': [50, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'charging_under_temperature': [51, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'voltage_diff_great': [52, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'temperature_diff_great': [53, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'mos_over_temperature': [54, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback],
            'environment_over_temperature': [55, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback, self.writeCallback]

        }

    def clear(self):
        self.responses.put('')
        del self.buffer[:]

    # 定义该函数用来连接信号
    def command_read_mcu(self, command:str, data=None):
        if command in self.function_map:
            func_item = self.function_map[command]
            if func_item[1] is not None:
                read_func = func_item[1]
                read_func(code=int(func_item[0]).to_bytes(length=1, byteorder='little'), data=data)

    def command_write_mcu(self, command:str, data=None):
        if command in self.function_map:
            func_item = self.function_map[command]
            if func_item[2] is not None:
                write_func = func_item[2]
                write_func(code=int(func_item[0]).to_bytes(length=1, byteorder='little'), data=data)

    def command(self, command_packet, response='OK', timeout=1):
        uart_write_and_wait_respond_thread = threading.Thread(target=self._run_event, args=(command_packet, timeout))
        uart_write_and_wait_respond_thread.start()

    def _run_event(self, command, timeout):
        start = time.time()
        with self.lock:
            self.port_send_request_signal.emit(command)
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
        print(data)
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

        # 获取读写标记
        op = int(packet[3])
        # 提取接受到的数据的功能码
        code = int(packet[4])
        # 找到对应功能码的回调处理函数
        for k, v in self.function_map.items():
            if v[0] == code:
                if op == 1:
                    func = v[3]
                else:
                    func = v[4]

                data_len = int(packet[5])
                if data_len > 0:
                    data = packet[6:6 + data_len]
                else:
                    data = None
                func(data)
                break

        # if code in self.action:
        #     func = self.action[code]
        #     data_len = int(packet[5])
        #     if data_len > 0:
        #         data = packet[6:6+data_len]
        #     else:
        #         data = None
        #     func(data)
        # else:
        #     print('功能码未实现：' + str(packet[4]))

    def code_30_function(self, data):
        print(data)
        if data is not None:
            battery_total_voltage = int(data[0] | (data[1] << 8))
            self.voltageChanged.emit('voltage', battery_total_voltage)
            print(battery_total_voltage)

    def readBatterySettingItem(self, code, data):
            send_buffer = bytearray()
            send_buffer.extend(self.START)
            send_buffer.extend(b'\x01')
            send_buffer.extend(b'\x01')
            send_buffer.extend(code)
            send_buffer.extend(b'\x00')

            self.command(bytes(send_buffer))

    def writeBatterySettingItem(self, code, data):
            send_buffer = bytearray()
            send_buffer.extend(self.START)
            send_buffer.extend(b'\x01')
            send_buffer.extend(b'\x00')
            send_buffer.extend(code)
            send_buffer.extend(b'\x0d')
            send_buffer.extend(int(data.protect_threshold).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.protect_hysteresis).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.protect_threshold_delay).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.protect_hysteresis_delay).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.alarm_threshold).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.alarm_threshold_delay).to_bytes(length=2, byteorder='little'))
            send_buffer.extend(int(data.enabled).to_bytes(length=2, byteorder='little'))


            self.command(bytes(send_buffer))

    def readCallback(self, data):
        print('readCallback')
        print(data)

    def writeCallback(self, data):
        print('writeCallback')
        print(data)
import queue
import struct
import threading
import time
from math import ceil

from PyQt5.QtCore import *


class DBJProtocol(QObject):
    START = b'\x3a\x7e'

    batteryStatusChanged = pyqtSignal(str, object)
    batterySettingsChanged = pyqtSignal(str, bool, int, int, int, int, int, int)
    systemStatusChanged = pyqtSignal(str, object)
    historyRecordCountChanged = pyqtSignal(int)
    port_send_request_signal = pyqtSignal(bytes)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.responses = queue.Queue()
        self.events = queue.Queue()
        self.lock = threading.Lock()
        self.buffer = bytearray()

        self.function_map = {
            'projectId': [1, self.readBatterySettingItem, self.writeProductID, self.readProductIDCallback,
                          self.writeCallback],
            'bmsId': [2, self.readBatterySettingItem, self.writeProductID, self.readBmsIdCallback,
                      self.writeCallback],
            'version': [3, self.readBatterySettingItem, self.writeProductID, self.readVersionCallback,
                        self.writeCallback],
            'protocolVersion': [4, self.readBatterySettingItem, self.writeProductID, self.readProtocolVersionCallback,
                                self.writeCallback],
            'bmsSN': [5, self.readBatterySettingItem, self.writeProductID, self.readBmsSNCallback,
                                self.writeCallback],
            'balanceInfo': [8, self.readBatterySettingItem, self.writeProductID, self.readBalanceInfoCallback,
                      self.writeCallback],
            'circleSetting': [9, self.readBatterySettingItem, self.writeProductID, self.readCircleSettingCallback,
                            self.writeCallback],
            'socSohSetting': [10, self.readBatterySettingItem, self.writeProductID, self.readSocSohSettingCallback,
                              self.writeCallback],
            'resistance': [11, self.readBatterySettingItem, self.writeProductID, self.readResistanceCallback,
                              self.writeCallback],
            'dischargingCurrentRatio': [12, self.readBatterySettingItem, self.writeProductID, self.readDischargingCurrentRatioCallback,
                           self.writeCallback],
            'chargingCurrentRatio': [13, self.readBatterySettingItem, self.writeProductID, self.readChargingCurrentRatioCallback,
                                        self.writeCallback],
            'battery_status': [30, self.readBatterySettingItem, None, self.readBatteryStatus30Callback, None],
            'battery_thermal_sensors': [31, self.readBatterySettingItem, None, self.readBatteryStatus31Callback, None],
            'battery_cells': [32, self.readBatterySettingItem, None, self.readBatteryStatus32Callback, None],
            'cell_over_voltage': [40, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback40, self.writeCallback],
            'cell_under_voltage': [41, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback41, self.writeCallback],
            'total_over_voltage': [42, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback42, self.writeCallback],
            'total_under_voltage': [43, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback43, self.writeCallback],
            'discharging_over_current': [44, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback44, self.writeCallback],
            'charging_over_current': [45, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback45, self.writeCallback],
            'soc_over_threshold': [46, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback46, self.writeCallback],
            'soc_under_threshold': [47, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback47, self.writeCallback],
            'discharging_over_temperature': [48, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback48, self.writeCallback],
            'charging_over_temperature': [49, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback49, self.writeCallback],
            'discharging_under_temperature': [50, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback50, self.writeCallback],
            'charging_under_temperature': [51, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback51, self.writeCallback],
            'voltage_diff_great': [52, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback52, self.writeCallback],
            'temperature_diff_great': [53, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback53, self.writeCallback],
            'mos_over_temperature': [54, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback54, self.writeCallback],
            'environment_over_temperature': [55, self.readBatterySettingItem, self.writeBatterySettingItem, self.readCallback55, self.writeCallback],
            'system_control': [60, None, self.writeBatterySettingItem,
                                             None, self.writeCallback],
            'history_record': [70, self.readCode70, None,
                              self.readCallback70, None],
            'history_count': [71, self.readBatterySettingItem, None,
                               self.readCallback71, None]
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
        # print(data)
        self.buffer.extend(data)
        if b';~' in self.buffer:
            start = self.buffer.index(b';')
            try:
                data_len = self.buffer[start+5]
                # print(int(data_len))
                # print(len(self.buffer))
                if len(self.buffer) < int(data_len)+7:
                    return
                packet = self.buffer[start:start+5+data_len+1]
                crc = self.buffer[start+5+data_len+1]
                del self.buffer[:start+5+data_len+1]
                if self.validate_crc(packet[:], crc):
                    self.parse_received_packet(packet)
                self.responses.put(b'OK')
            except Exception as e:
                # print(e)
                pass

    def validate_crc(self, data, read_crc):
        crc = 0
        for c in data:
            crc = crc + int(c)

        crc = crc % 256

        # print(read_crc)
        # print(crc)

        return crc == read_crc

    def parse_received_packet(self, packet):
        # print(packet)
        # print('function code:' + str(packet[4]))

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

    def readProductIDCallback(self, data):
        product_id = data.decode('utf-8')
        print(product_id)
        self.systemStatusChanged.emit('projectId', product_id)

    def writeProductID(self, data):
        pass

    def readBmsIdCallback(self, data):
        bms_id = data.decode('utf-8')
        self.systemStatusChanged.emit('bmsId', bms_id)

    def readVersionCallback(self, data):
        swVersion = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('swVersion', str(round(swVersion * 0.01, 2)))
        hwVersion = int(data[2] | (data[3] << 8))
        self.systemStatusChanged.emit('hwVersion', str(round(hwVersion * 0.01, 2)))

    def readProtocolVersionCallback(self, data):
        protocolVersion = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('protocolVersion', str(protocolVersion))

    def readBmsSNCallback(self, data):
        bmsSN = data.decode('utf-8')
        self.systemStatusChanged.emit('bmsSN', bmsSN)

    def readBalanceInfoCallback(self, data):
        balanceEnableFlag = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('balanceEnableFlag', balanceEnableFlag)

        balanceEnableVoltageDiff = int(data[2] | (data[3] << 8))
        self.systemStatusChanged.emit('balanceEnableVoltageDiff', balanceEnableVoltageDiff)

        balanceEnableVoltage = int(data[4] | (data[5] << 8))
        self.systemStatusChanged.emit('balanceEnableVoltage', balanceEnableVoltage)

        balanceDisableVoltage = int(data[6] | (data[7] << 8))
        self.systemStatusChanged.emit('balanceDisableVoltage', balanceDisableVoltage)

    def readCircleSettingCallback(self, data):
        chargingCircleSetting = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('chargingCircleSetting', chargingCircleSetting)

        totalChargingCirCle = int(data[2] | (data[3] << 8))
        self.systemStatusChanged.emit('totalChargingCirCle', totalChargingCirCle)

        realCapacity = int(data[4] | (data[5] << 8))
        self.systemStatusChanged.emit('realCapacity', realCapacity)

        settingCapacity = int(data[6] | (data[7] << 8))
        self.systemStatusChanged.emit('settingCapacity', settingCapacity)

    def readSocSohSettingCallback(self, data):
        soh = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('soh', soh)

        soc = int(data[2] | (data[3] << 8))
        self.systemStatusChanged.emit('soc', soc)

    def readResistanceCallback(self, data):
        sampleResistanceValue = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('sampleResistanceValue', sampleResistanceValue)

        zeroCurrentADCValue = int(data[2] | (data[3] << 8))
        self.systemStatusChanged.emit('zeroCurrentADCValue', zeroCurrentADCValue)

    def readDischargingCurrentRatioCallback(self, data):
        dischargingCurrentRatio = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('dischargingCurrentRatio', dischargingCurrentRatio)

    def readChargingCurrentRatioCallback(self, data):
        chargingCurrentRatio = int(data[0] | (data[1] << 8))
        self.systemStatusChanged.emit('dischargingCurrentRatio', chargingCurrentRatio)

    def readCommandNoData(self, code):
        send_buffer = bytearray()
        send_buffer.extend(self.START)
        send_buffer.extend(b'\x01')
        send_buffer.extend(b'\x01')
        send_buffer.extend(code.to_bytes(length=1, byteorder='little'))
        send_buffer.extend(b'\x00')
        crc = 0
        for c in send_buffer:
            crc = crc + int(c)

        crc = crc % 256
        send_buffer.extend(crc.to_bytes(length=1, byteorder='little'))

        self.command(bytes(send_buffer))
        # print(send_buffer)

    def readBatteryStatus30Callback(self, data):
        battery_total_voltage = int(data[0] | (data[1] << 8))
        self.batteryStatusChanged.emit('voltage', str(round(battery_total_voltage*0.01, 2)))

        battery_total_current = int(data[2] | (data[3] << 8))
        self.batteryStatusChanged.emit('current', str(round(battery_total_current*0.01, 2)))

        battery_soc = int(data[4] | (data[5] << 8))
        self.batteryStatusChanged.emit('soc', str(battery_soc*0.02))

        battery_soh = int(data[6] | (data[7] << 8))
        self.batteryStatusChanged.emit('soh', str(battery_soh))

        battery_max_cell_voltage = int(data[8] | (data[9] << 8))
        self.batteryStatusChanged.emit('maxCellVoltage', str(round(battery_max_cell_voltage*0.01, 2)))

        battery_max_cell_number_voltage = int(data[10] | (data[11] << 8))
        self.batteryStatusChanged.emit('maxCellVoltageNr', str(battery_max_cell_number_voltage))

        battery_min_cell_voltage = int(data[12] | (data[13] << 8))
        self.batteryStatusChanged.emit('minCellVoltage', str(round(battery_min_cell_voltage*0.01, 2)))

        battery_min_cell_number_voltage = int(data[14] | (data[15] << 8))
        self.batteryStatusChanged.emit('minCellVoltageNr', str(battery_min_cell_number_voltage))

        battery_max_cells_voltage_diff = int(data[16] | (data[17] << 8))
        self.batteryStatusChanged.emit('maxCellsVoltageDiff', str(round(battery_max_cells_voltage_diff*0.01, 2)))

        battery_max_cell_temperature = int(data[18] | (data[19] << 8))
        self.batteryStatusChanged.emit('maxCellTemperature', str(round((battery_max_cell_temperature-2731)*0.1, 2)))

        battery_max_cell_number_temperature = int(data[20] | (data[21] << 8))
        self.batteryStatusChanged.emit('maxCellTemperatureNr', str(battery_max_cell_number_temperature))

        battery_min_cell_temperature = int(data[22] | (data[23] << 8))
        self.batteryStatusChanged.emit('minCellTemperature', str(round((battery_min_cell_temperature-2731)*0.1, 2)))

        battery_min_cell_number_temperature = int(data[24] | (data[25] << 8))
        self.batteryStatusChanged.emit('minCellTemperatureNr', str(battery_min_cell_number_temperature))

        tmp = data[26]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('cellOverVoltageAlarm', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('cellUnderVoltageAlarm', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('batteryOverVoltageAlarm', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('batteryUnderVoltageAlarm', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('batteryDischargingOverCurrentAlarm', str(temp))
        temp = (tmp >> 5) & 0x01
        self.batteryStatusChanged.emit('batteryChargingOverCurrentAlarm', str(temp))
        temp = (tmp >> 6) & 0x01
        self.batteryStatusChanged.emit('batteryDischargingOverTemperatureAlarm', str(temp))
        temp = (tmp >> 7) & 0x01
        self.batteryStatusChanged.emit('batteryChargingOverTemperatureAlarm', str(temp))

        tmp = data[27]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('batteryDischargingUnderTemperatureAlarm', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('batteryChargingUnderTemperatureAlarm', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('socOverThresholdAlarm', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('socUnderThresholdAlarm', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('voltageDiffAlarm', str(temp))
        temp = (tmp >> 5) & 0x01
        self.batteryStatusChanged.emit('temperatureDiffAlarm', str(temp))
        temp = (tmp >> 6) & 0x01
        self.batteryStatusChanged.emit('mosTemperatureHighAlarm', str(temp))
        temp = (tmp >> 7) & 0x01
        self.batteryStatusChanged.emit('envTemperatureHighAlarm', str(temp))

        tmp = data[30]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('cellOverVoltageProtect', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('cellUnderVoltageProtect', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('batteryOverVoltageProtect', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('batteryUnderVoltageProtect', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('batteryDischargingOverCurrentProtect', str(temp))
        temp = (tmp >> 5) & 0x01
        self.batteryStatusChanged.emit('batteryChargingOverCurrentProtect', str(temp))
        temp = (tmp >> 6) & 0x01
        self.batteryStatusChanged.emit('batteryDischargingOverTemperatureProtect', str(temp))
        temp = (tmp >> 7) & 0x01
        self.batteryStatusChanged.emit('batteryChargingOverTemperatureProtect', str(temp))

        tmp = data[31]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('batteryDischargingUnderTemperatureProtect', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('batteryChargingUnderTemperatureProtect', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('socOverThresholdProtect', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('socUnderThresholdProtect', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('voltageDiffProtect', str(temp))
        temp = (tmp >> 5) & 0x01
        self.batteryStatusChanged.emit('temperatureDiffProtect', str(temp))
        temp = (tmp >> 6) & 0x01
        self.batteryStatusChanged.emit('mosTemperatureHighProtect', str(temp))
        temp = (tmp >> 7) & 0x01
        self.batteryStatusChanged.emit('envTemperatureHighProtect', str(temp))

        tmp = data[34]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('dischargingMosNoFunction', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('chargingMosNoFunction', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('eepromWriteFail', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('notChargingUnderVoltage', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('shortProtect', str(temp))

        tmp = data[36]
        temp = tmp & 0x01
        self.batteryStatusChanged.emit('dischargingMosFetStatus', str(temp))
        temp = (tmp >> 1) & 0x01
        self.batteryStatusChanged.emit('chargingMosFetStatus', str(temp))
        temp = (tmp >> 2) & 0x01
        self.batteryStatusChanged.emit('preChargingMosFetStatus', str(temp))
        temp = (tmp >> 3) & 0x01
        self.batteryStatusChanged.emit('heaterSwitch', str(temp))
        temp = (tmp >> 4) & 0x01
        self.batteryStatusChanged.emit('gprs', str(temp))
        temp = (tmp >> 5) & 0x01
        self.batteryStatusChanged.emit('chargerAdapterPlugin', str(temp))
        temp = (tmp >> 6) & 0x01
        self.batteryStatusChanged.emit('loaderConnection', str(temp))

    def readBatteryStatus31Callback(self, data):
        # print(data)
        thermals = []
        count = int(data[0] | (data[1] << 8))
        for i in range(count):
            temp = int(data[2+i*2] | (data[3+i*2] << 8))
            temp = (temp-2731)*0.1
            temp = round(temp, 2)
            thermals.append(temp)
        self.batteryStatusChanged.emit('thermal_sensors', thermals)

    def readBatteryStatus32Callback(self, data):
        # print(data)
        cells_balance = []
        cells_voltage = []
        count = int(data[0] | (data[1] << 8))
        bit_count = 0

        for i in range(ceil(count/8)):
            for bit in range(8):
                cells_balance.append((data[i+2] >> bit) & 1)
                bit_count = bit_count + 1

                if bit_count >= count:
                    break

        # print(cells_balance)

        for i in range(count):
            temp = int(data[2+ceil(count/8)+i*2] | (data[3+ceil(count/8)+i*2] << 8))
            temp = temp*0.001
            temp = round(temp, 3)
            cells_voltage.append(temp)

        # print(cells_voltage)
        self.batteryStatusChanged.emit('cells_balance', cells_balance)
        self.batteryStatusChanged.emit('cells_voltage', cells_voltage)

    def getCrc(self, data):
        crc = 0
        for c in data:
            crc = crc + int(c)
        crc = crc % 256
        return crc.to_bytes(length=1, byteorder='little')

    def readBatterySettingItem(self, code, data):
        send_buffer = bytearray()
        send_buffer.extend(self.START)
        send_buffer.extend(b'\x01')
        send_buffer.extend(b'\x01')
        send_buffer.extend(code)
        send_buffer.extend(b'\x00')
        crc = self.getCrc(send_buffer)
        send_buffer.extend(crc)

        self.command(bytes(send_buffer))

    def writeBatterySettingItem(self, code, data):
        send_buffer = bytearray()
        send_buffer.extend(self.START)
        send_buffer.extend(b'\x01')
        send_buffer.extend(b'\x00')
        send_buffer.extend(code)
        send_buffer.extend(b'\x0e')
        send_buffer.extend(int(data.protect_threshold).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.protect_hysteresis).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.alarm_threshold).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.protect_threshold_delay).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.protect_hysteresis_delay).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.alarm_threshold_delay).to_bytes(length=2, byteorder='little'))
        send_buffer.extend(int(data.enabled).to_bytes(length=2, byteorder='little'))

        crc = self.getCrc(send_buffer)
        send_buffer.extend(crc)
        self.command(bytes(send_buffer))

    def readCallback40(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('cell_over_voltage', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback41(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('cell_under_voltage', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback42(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('total_over_voltage', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback43(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('total_under_voltage', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback44(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('discharging_over_current', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback45(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('charging_over_current', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback46(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('soc_over_threshold', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback47(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('soc_under_threshold', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback48(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('discharging_over_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback49(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('charging_over_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback50(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('discharging_under_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback51(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('charging_under_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback52(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('voltage_diff_great', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback53(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('temperature_diff_great', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback54(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('mos_over_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCallback55(self, data):
        protect_threshold = int(data[0] | (data[1] << 8))
        protect_hysteresis = int(data[2] | (data[3] << 8))
        alarm_threshold = int(data[4] | (data[5] << 8))
        protect_threshold_delay = int(data[6] | (data[7] << 8))
        protect_hysteresis_delay = int(data[8] | (data[9] << 8))
        alarm_threshold_delay = int(data[10] | (data[11] << 8))
        enabled = int(data[12] | (data[13] << 8))
        self.batterySettingsChanged.emit('environment_over_temperature', enabled==1, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay)

    def readCode70(self, code, data=None):
        count_from = 1
        count_to = 1
        send_buffer = bytearray()
        send_buffer.extend(self.START)
        send_buffer.extend(b'\x01')
        send_buffer.extend(b'\x01')
        send_buffer.extend(code) # code 70
        send_buffer.extend(b'\x08') # len
        send_buffer.extend(struct.pack('i', count_from))
        send_buffer.extend(struct.pack('i', count_to))
        crc = self.getCrc(send_buffer)
        send_buffer.extend(crc)
        self.command(bytes(send_buffer))

        print(send_buffer)


    def readCallback70(self, data):
        history_count = struct.unpack('i', data);
        self.historyRecordCountChanged.emit(history_count[0])

    def readCallback71(self, data):
        history_count = struct.unpack('i', data);
        self.historyRecordCountChanged.emit(history_count[0])

    def readCallback(self, data):
        print('readCallback')
        print(data)

    def writeCallback(self, data):
        print('writeCallback')
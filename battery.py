from PyQt5.QtCore import *
from threading import Timer
from BatteryModel import BatteryModel


class BatteryStatus(QObject):
    OFF = 0
    ON = 1

    batteryUpdated = pyqtSignal(str)
    cells_countChanged = pyqtSignal(str)
    voltageChanged = pyqtSignal(str)
    currentChanged = pyqtSignal(str)
    socChanged = pyqtSignal(str)
    sohChanged = pyqtSignal(str)
    maxCellVoltageChanged = pyqtSignal(str)
    maxCellVoltageNrChanged = pyqtSignal(str)
    minCellVoltageChanged = pyqtSignal(str)
    minCellVoltageNrChanged = pyqtSignal(str)
    maxCellTemperatureChanged = pyqtSignal(str)
    maxCellTemperatureNrChanged = pyqtSignal(str)
    minCellTemperatureChanged = pyqtSignal(str)
    minCellTemperatureNrChanged = pyqtSignal(str)
    maxCellsVoltageDiffChanged = pyqtSignal(str)

    cellOverVoltageAlarmChanged = pyqtSignal(bool)
    cellUnderVoltageAlarmChanged = pyqtSignal(bool)
    batteryOverVoltageAlarmChanged = pyqtSignal(bool)
    batteryUnderVoltageAlarmChanged = pyqtSignal(bool)
    batteryDischargingOverCurrentAlarmChanged = pyqtSignal(bool)
    batteryChargingOverCurrentAlarmChanged = pyqtSignal(bool)
    batteryDischargingOverTemperatureAlarmChanged = pyqtSignal(bool)
    batteryChargingOverTemperatureAlarmChanged = pyqtSignal(bool)
    batteryDischargingUnderTemperatureAlarmChanged = pyqtSignal(bool)
    batteryChargingUnderTemperatureAlarmChanged = pyqtSignal(bool)
    socOverThresholdAlarmChanged = pyqtSignal(bool)
    socUnderThresholdAlarmChanged = pyqtSignal(bool)
    voltageDiffAlarmChanged = pyqtSignal(bool)
    temperatureDiffAlarmChanged = pyqtSignal(bool)
    mosTemperatureHighAlarmChanged = pyqtSignal(bool)
    envTemperatureHighAlarmChanged = pyqtSignal(bool)

    cellOverVoltageProtectChanged = pyqtSignal(bool)
    cellUnderVoltageProtectChanged = pyqtSignal(bool)
    batteryOverVoltageProtectChanged = pyqtSignal(bool)
    batteryUnderVoltageProtectChanged = pyqtSignal(bool)
    batteryDischargingOverCurrentProtectChanged = pyqtSignal(bool)
    batteryChargingOverCurrentProtectChanged = pyqtSignal(bool)
    batteryDischargingOverTemperatureProtectChanged = pyqtSignal(bool)
    batteryChargingOverTemperatureProtectChanged = pyqtSignal(bool)
    batteryDischargingUnderTemperatureProtectChanged = pyqtSignal(bool)
    batteryChargingUnderTemperatureProtectChanged = pyqtSignal(bool)
    socOverThresholdProtectChanged = pyqtSignal(bool)
    socUnderThresholdProtectChanged = pyqtSignal(bool)
    voltageDiffProtectChanged = pyqtSignal(bool)
    temperatureDiffProtectChanged = pyqtSignal(bool)
    mosTemperatureHighProtectChanged = pyqtSignal(bool)
    envTemperatureHighProtectChanged = pyqtSignal(bool)

    dischargingMosNoFunctionChanged = pyqtSignal(bool)
    chargingMosNoFunctionChanged = pyqtSignal(bool)
    eepromWriteFailChanged = pyqtSignal(bool)
    notChargingUnderVoltageChanged = pyqtSignal(bool)
    shortProtectChanged = pyqtSignal(bool)

    dischargingMosFetStatusChanged = pyqtSignal(bool)
    chargingMosFetStatusChanged = pyqtSignal(bool)
    preChargingMosFetStatusChanged = pyqtSignal(bool)
    heaterSwitchChanged = pyqtSignal(bool)
    gprsChanged = pyqtSignal(bool)
    chargerAdapterPluginChanged = pyqtSignal(bool)
    loaderConnectionChanged = pyqtSignal(bool)

    systemStatusChanged = pyqtSignal(str)

    cellsChanged = pyqtSignal(str)
    thermal_sensorsChanged = pyqtSignal(str)

    read_battery_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        # 定义为一个字典，把几个东西绑定为一条
        # 变量名 / 值 / 信号
        self.update_needed = {
            'cells_count': [0, self.cells_countChanged],
            'voltage': [0, self.voltageChanged],
            'current': [0, self.currentChanged],
            'soc': [0, self.socChanged],
            'soh': [0, self.sohChanged],
            'status': [0, self.systemStatusChanged],
            'maxCellVoltage': [0, self.maxCellVoltageChanged],
            'maxCellVoltageNr': [0, self.maxCellVoltageNrChanged],
            'minCellVoltage': [0, self.minCellVoltageChanged],
            'minCellVoltageNr': [0, self.minCellVoltageNrChanged],
            'maxCellsVoltageDiff': [0, self.maxCellsVoltageDiffChanged],
            'maxCellTemperature': [0, self.maxCellTemperatureChanged],
            'maxCellTemperatureNr': [0, self.maxCellTemperatureNrChanged],
            'minCellTemperature': [0, self.minCellTemperatureChanged],
            'minCellTemperatureNr': [0, self.minCellTemperatureNrChanged],
            'cellOverVoltageAlarm': [False, self.cellOverVoltageAlarmChanged],
            'cellUnderVoltageAlarm': [False, self.cellUnderVoltageAlarmChanged],
            'batteryOverVoltageAlarm': [False, self.batteryOverVoltageAlarmChanged],


            'cells': [[], self.cellsChanged],
            'thermal_sensors': [[1], self.thermal_sensorsChanged]
        }

        self.batteryModel = BatteryModel(self.update_needed['thermal_sensors'][0])
        self.timer = Timer(5, self.foo)
        self.timer.start()

    @pyqtProperty(str, notify=cells_countChanged)
    def cells_count(self):
        return self.update_needed['cells_count'][0]

    @pyqtProperty(str, notify=voltageChanged)
    def voltage(self):
        return str(self.update_needed['voltage'][0])

    @voltage.setter
    def voltage(self, value):
        self.update_needed['voltage'][0] = value
        self.voltageChanged.emit(value)

    @pyqtProperty(str, notify=currentChanged)
    def current(self):
        return str(self.update_needed['current'][0])

    @pyqtProperty(str, notify=socChanged)
    def soc(self):
        return str(self.update_needed['soc'][0])

    @pyqtProperty(str, notify=sohChanged)
    def soh(self):
        return str(self.update_needed['soh'][0])

    @pyqtProperty(str, notify=maxCellVoltageChanged)
    def max_cell_voltage(self):
        return str(self.update_needed['maxCellVoltage'][0])

    @pyqtProperty(str, notify=maxCellVoltageNrChanged)
    def max_cell_number_voltage(self):
        return str(self.update_needed['maxCellVoltageNr'][0])

    @pyqtProperty(str, notify=minCellVoltageChanged)
    def min_cell_voltage(self):
        return str(self.update_needed['minCellVoltage'][0])

    @pyqtProperty(str, notify=minCellVoltageNrChanged)
    def min_cell_number_voltage(self):
        return str(self.update_needed['minCellVoltageNr'][0])

    @pyqtProperty(str, notify=maxCellsVoltageDiffChanged)
    def max_cells_voltage_diff(self):
        return str(self.update_needed['maxCellsVoltageDiff'][0])

    @pyqtProperty(str, notify=maxCellTemperatureChanged)
    def max_cell_temperature(self):
        return str(self.update_needed['maxCellTemperature'][0])

    @pyqtProperty(str, notify=maxCellTemperatureNrChanged)
    def max_cell_number_temperature(self):
        return str(self.update_needed['maxCellTemperatureNr'][0])

    @pyqtProperty(str, notify=minCellTemperatureChanged)
    def min_cell_temperature(self):
        return str(self.update_needed['minCellTemperature'][0])

    @pyqtProperty(str, notify=minCellTemperatureNrChanged)
    def min_cell_number_temperature(self):
        return str(self.update_needed['minCellTemperatureNr'][0])


    @pyqtProperty(str, notify=systemStatusChanged)
    def status(self):
        return str(self.update_needed['status'][0])

    def foo(self):
        self.update(soc=90)
        self.batteryModel.dataReceived.emit(2)

    def update(self, *args, **kwargs):
        print(args)
        print(kwargs)

        if len(args):
            if args[0] in self.update_needed:
                item = self.update_needed[args[0]]
                item[0] = args[1]
                item[1].emit(str(args[1]))

        for k, v in kwargs.items():
            item = self.update_needed[k]
            item[0] = v
            item[1].emit(str(v))

    @pyqtSlot(int)
    def readBattery(self, code):
        self.read_battery_signal.emit(code)



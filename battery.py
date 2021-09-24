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

    cellOverVoltageAlarmChanged = pyqtSignal(str)
    cellUnderVoltageAlarmChanged = pyqtSignal(str)
    batteryOverVoltageAlarmChanged = pyqtSignal(str)
    batteryUnderVoltageAlarmChanged = pyqtSignal(str)
    batteryDischargingOverCurrentAlarmChanged = pyqtSignal(str)
    batteryChargingOverCurrentAlarmChanged = pyqtSignal(str)
    batteryDischargingOverTemperatureAlarmChanged = pyqtSignal(str)
    batteryChargingOverTemperatureAlarmChanged = pyqtSignal(str)
    batteryDischargingUnderTemperatureAlarmChanged = pyqtSignal(str)
    batteryChargingUnderTemperatureAlarmChanged = pyqtSignal(str)
    socOverThresholdAlarmChanged = pyqtSignal(str)
    socUnderThresholdAlarmChanged = pyqtSignal(str)
    voltageDiffAlarmChanged = pyqtSignal(str)
    temperatureDiffAlarmChanged = pyqtSignal(str)
    mosTemperatureHighAlarmChanged = pyqtSignal(str)
    envTemperatureHighAlarmChanged = pyqtSignal(str)

    cellOverVoltageProtectChanged = pyqtSignal(str)
    cellUnderVoltageProtectChanged = pyqtSignal(str)
    batteryOverVoltageProtectChanged = pyqtSignal(str)
    batteryUnderVoltageProtectChanged = pyqtSignal(str)
    batteryDischargingOverCurrentProtectChanged = pyqtSignal(str)
    batteryChargingOverCurrentProtectChanged = pyqtSignal(str)
    batteryDischargingOverTemperatureProtectChanged = pyqtSignal(str)
    batteryChargingOverTemperatureProtectChanged = pyqtSignal(str)
    batteryDischargingUnderTemperatureProtectChanged = pyqtSignal(str)
    batteryChargingUnderTemperatureProtectChanged = pyqtSignal(str)
    socOverThresholdProtectChanged = pyqtSignal(str)
    socUnderThresholdProtectChanged = pyqtSignal(str)
    voltageDiffProtectChanged = pyqtSignal(str)
    temperatureDiffProtectChanged = pyqtSignal(str)
    mosTemperatureHighProtectChanged = pyqtSignal(str)
    envTemperatureHighProtectChanged = pyqtSignal(str)

    dischargingMosNoFunctionChanged = pyqtSignal(str)
    chargingMosNoFunctionChanged = pyqtSignal(str)
    eepromWriteFailChanged = pyqtSignal(str)
    notChargingUnderVoltageChanged = pyqtSignal(str)
    shortProtectChanged = pyqtSignal(str)

    dischargingMosFetStatusChanged = pyqtSignal(str)
    chargingMosFetStatusChanged = pyqtSignal(str)
    preChargingMosFetStatusChanged = pyqtSignal(str)
    heaterSwitchChanged = pyqtSignal(str)
    gprsChanged = pyqtSignal(str)
    chargerAdapterPluginChanged = pyqtSignal(str)
    loaderConnectionChanged = pyqtSignal(str)

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

            'cellOverVoltageAlarm': [0, self.cellOverVoltageAlarmChanged],
            'cellUnderVoltageAlarm': [0, self.cellUnderVoltageAlarmChanged],
            'batteryOverVoltageAlarm': [0, self.batteryOverVoltageAlarmChanged],
            'batteryUnderVoltageAlarm': [0, self.batteryUnderVoltageAlarmChanged],
            'batteryDischargingOverCurrentAlarm': [0, self.batteryDischargingOverCurrentAlarmChanged],
            'batteryChargingOverCurrentAlarm': [0, self.batteryChargingOverCurrentAlarmChanged],
            'batteryDischargingOverTemperatureAlarm': [0, self.batteryDischargingOverTemperatureAlarmChanged],
            'batteryChargingOverTemperatureAlarm': [0, self.batteryChargingOverTemperatureAlarmChanged],
            'batteryDischargingUnderTemperatureAlarm': [0, self.batteryDischargingUnderTemperatureAlarmChanged],
            'batteryChargingUnderTemperatureAlarm': [0, self.batteryChargingUnderTemperatureAlarmChanged],
            'socOverThresholdAlarm': [0, self.socOverThresholdAlarmChanged],
            'socUnderThresholdAlarm': [0, self.socUnderThresholdAlarmChanged],
            'voltageDiffAlarm': [0, self.voltageDiffAlarmChanged],
            'temperatureDiffAlarm': [0, self.temperatureDiffAlarmChanged],
            'mosTemperatureHighAlarm': [0, self.mosTemperatureHighAlarmChanged],
            'envTemperatureHighAlarm': [0, self.envTemperatureHighAlarmChanged],

            'cellOverVoltageProtect': [0, self.cellOverVoltageProtectChanged],
            'cellUnderVoltageProtect': [0, self.cellUnderVoltageProtectChanged],
            'batteryOverVoltageProtect': [0, self.batteryOverVoltageProtectChanged],
            'batteryUnderVoltageProtect': [0, self.batteryUnderVoltageProtectChanged],
            'batteryDischargingOverCurrentProtect': [0, self.batteryDischargingOverCurrentProtectChanged],
            'batteryChargingOverCurrentProtect': [0, self.batteryChargingOverCurrentProtectChanged],
            'batteryDischargingOverTemperatureProtect': [0, self.batteryDischargingOverTemperatureProtectChanged],
            'batteryChargingOverTemperatureProtect': [0, self.batteryChargingOverTemperatureProtectChanged],
            'batteryDischargingUnderTemperatureProtect': [0, self.batteryDischargingUnderTemperatureProtectChanged],
            'batteryChargingUnderTemperatureProtect': [0, self.batteryChargingUnderTemperatureProtectChanged],
            'socOverThresholdProtect': [0, self.socOverThresholdProtectChanged],
            'socUnderThresholdProtect': [0, self.socUnderThresholdProtectChanged],
            'voltageDiffProtect': [0, self.voltageDiffProtectChanged],
            'temperatureDiffProtect': [0, self.temperatureDiffProtectChanged],
            'mosTemperatureHighProtect': [0, self.mosTemperatureHighProtectChanged],
            'envTemperatureHighProtect': [0, self.envTemperatureHighProtectChanged],

            'dischargingMosNoFunction': [0, self.dischargingMosNoFunctionChanged],
            'chargingMosNoFunction': [0, self.chargingMosNoFunctionChanged],
            'eepromWriteFail': [0, self.eepromWriteFailChanged],
            'notChargingUnderVoltage': [0, self.notChargingUnderVoltageChanged],
            'shortProtect': [0, self.shortProtectChanged],

            'dischargingMosFetStatus': [0, self.dischargingMosFetStatusChanged],
            'chargingMosFetStatus': [0, self.chargingMosFetStatusChanged],
            'preChargingMosFetStatus': [0, self.preChargingMosFetStatusChanged],
            'heaterSwitch': [0, self.heaterSwitchChanged],
            'gprs': [0, self.gprsChanged],
            'chargerAdapterPlugin': [0, self.chargerAdapterPluginChanged],
            'loaderConnection': [0, self.loaderConnectionChanged],


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
    def maxCellVoltage(self):
        return str(self.update_needed['maxCellVoltage'][0])

    @pyqtProperty(str, notify=maxCellVoltageNrChanged)
    def maxCellVoltageNr(self):
        return str(self.update_needed['maxCellVoltageNr'][0])

    @pyqtProperty(str, notify=minCellVoltageChanged)
    def minCellVoltage(self):
        return str(self.update_needed['minCellVoltage'][0])

    @pyqtProperty(str, notify=minCellVoltageNrChanged)
    def minCellVoltageNr(self):
        return str(self.update_needed['minCellVoltageNr'][0])

    @pyqtProperty(str, notify=maxCellsVoltageDiffChanged)
    def maxCellsVoltageDiff(self):
        return str(self.update_needed['maxCellsVoltageDiff'][0])

    @pyqtProperty(str, notify=maxCellTemperatureChanged)
    def maxCellTemperature(self):
        return str(self.update_needed['maxCellTemperature'][0])

    @pyqtProperty(str, notify=maxCellTemperatureNrChanged)
    def maxCellTemperatureNr(self):
        return str(self.update_needed['maxCellTemperatureNr'][0])

    @pyqtProperty(str, notify=minCellTemperatureChanged)
    def minCellTemperature(self):
        return str(self.update_needed['minCellTemperature'][0])

    @pyqtProperty(str, notify=minCellTemperatureNrChanged)
    def minCellTemperatureNr(self):
        return str(self.update_needed['minCellTemperatureNr'][0])

    @pyqtProperty(bool, notify=cellOverVoltageAlarmChanged)
    def cellOverVoltageAlarm(self):
        return str(self.update_needed['cellOverVoltageAlarm'][0])

    @pyqtProperty(bool, notify=cellUnderVoltageAlarmChanged)
    def cellUnderVoltageAlarm(self):
        return str(self.update_needed['cellUnderVoltageAlarm'][0])

    @pyqtProperty(bool, notify=batteryOverVoltageAlarmChanged)
    def batteryOverVoltageAlarm(self):
        return str(self.update_needed['batteryOverVoltageAlarm'][0])

    @pyqtProperty(bool, notify=batteryUnderVoltageAlarmChanged)
    def batteryUnderVoltageAlarm(self):
        return str(self.update_needed['batteryUnderVoltageAlarm'][0])

    @pyqtProperty(bool, notify=batteryDischargingOverCurrentAlarmChanged)
    def batteryDischargingOverCurrentAlarm(self):
        return str(self.update_needed['batteryDischargingOverCurrentAlarm'][0])

    @pyqtProperty(bool, notify=batteryChargingOverCurrentAlarmChanged)
    def batteryChargingOverCurrentAlarm(self):
        return str(self.update_needed['batteryChargingOverCurrentAlarm'][0])

    @pyqtProperty(bool, notify=batteryDischargingOverTemperatureAlarmChanged)
    def batteryDischargingOverTemperatureAlarm(self):
        return str(self.update_needed['batteryDischargingOverTemperatureAlarm'][0])

    @pyqtProperty(bool, notify=batteryChargingOverTemperatureAlarmChanged)
    def batteryChargingOverTemperatureAlarm(self):
        return str(self.update_needed['batteryChargingOverTemperatureAlarm'][0])

    @pyqtProperty(bool, notify=batteryDischargingUnderTemperatureAlarmChanged)
    def batteryDischargingUnderTemperatureAlarm(self):
        return str(self.update_needed['batteryDischargingUnderTemperatureAlarm'][0])

    @pyqtProperty(bool, notify=batteryChargingUnderTemperatureAlarmChanged)
    def batteryChargingUnderTemperatureAlarm(self):
        return str(self.update_needed['batteryChargingUnderTemperatureAlarm'][0])

    @pyqtProperty(bool, notify=socOverThresholdAlarmChanged)
    def socOverThresholdAlarm(self):
        return str(self.update_needed['socOverThresholdAlarm'][0])

    @pyqtProperty(bool, notify=socUnderThresholdAlarmChanged)
    def socUnderThresholdAlarm(self):
        return str(self.update_needed['socUnderThresholdAlarm'][0])

    @pyqtProperty(bool, notify=voltageDiffAlarmChanged)
    def voltageDiffAlarm(self):
        return str(self.update_needed['voltageDiffAlarm'][0])

    @pyqtProperty(bool, notify=temperatureDiffAlarmChanged)
    def temperatureDiffAlarm(self):
        return str(self.update_needed['temperatureDiffAlarm'][0])

    @pyqtProperty(bool, notify=mosTemperatureHighAlarmChanged)
    def mosTemperatureHighAlarm(self):
        return str(self.update_needed['mosTemperatureHighAlarm'][0])

    @pyqtProperty(bool, notify=envTemperatureHighAlarmChanged)
    def envTemperatureHighAlarm(self):
        return str(self.update_needed['envTemperatureHighAlarm'][0])

    @pyqtProperty(bool, notify=cellOverVoltageProtectChanged)
    def cellOverVoltageProtect(self):
        return str(self.update_needed['cellOverVoltageProtect'][0])

    @pyqtProperty(bool, notify=cellUnderVoltageProtectChanged)
    def cellUnderVoltageProtect(self):
        return str(self.update_needed['cellUnderVoltageProtect'][0])

    @pyqtProperty(bool, notify=batteryOverVoltageProtectChanged)
    def batteryOverVoltageProtect(self):
        return str(self.update_needed['batteryOverVoltageProtect'][0])

    @pyqtProperty(bool, notify=batteryUnderVoltageProtectChanged)
    def batteryUnderVoltageProtect(self):
        return str(self.update_needed['batteryUnderVoltageProtect'][0])

    @pyqtProperty(bool, notify=batteryDischargingOverCurrentProtectChanged)
    def batteryDischargingOverCurrentProtect(self):
        return str(self.update_needed['batteryDischargingOverCurrent'][0])

    @pyqtProperty(bool, notify=batteryChargingOverCurrentProtectChanged)
    def batteryChargingOverCurrentProtect(self):
        return str(self.update_needed['batteryChargingOverCurrentProtect'][0])

    @pyqtProperty(bool, notify=batteryDischargingOverTemperatureProtectChanged)
    def batteryDischargingOverTemperatureProtect(self):
        return str(self.update_needed['batteryDischargingOverTemperatureProtect'][0])

    @pyqtProperty(bool, notify=batteryChargingOverTemperatureProtectChanged)
    def batteryChargingOverTemperatureProtect(self):
        return str(self.update_needed['batteryChargingOverTemperatureProtect'][0])

    @pyqtProperty(bool, notify=batteryDischargingUnderTemperatureProtectChanged)
    def batteryDischargingUnderTemperatureProtect(self):
        return str(self.update_needed['batteryDischargingUnderTemperatureProtect'][0])

    @pyqtProperty(bool, notify=batteryChargingUnderTemperatureProtectChanged)
    def batteryChargingUnderTemperatureProtect(self):
        return str(self.update_needed['batteryChargingUnderTemperatureProtect'][0])

    @pyqtProperty(bool, notify=socOverThresholdProtectChanged)
    def socOverThresholdProtect(self):
        return str(self.update_needed['socOverThresholdProtect'][0])

    @pyqtProperty(bool, notify=socUnderThresholdProtectChanged)
    def socUnderThresholdProtect(self):
        return str(self.update_needed['socUnderThresholdProtect'][0])

    @pyqtProperty(bool, notify=voltageDiffProtectChanged)
    def voltageDiffProtect(self):
        return str(self.update_needed['voltageDiffProtect'][0])

    @pyqtProperty(bool, notify=temperatureDiffProtectChanged)
    def temperatureDiffProtect(self):
        return str(self.update_needed['temperatureDiffProtect'][0])

    @pyqtProperty(bool, notify=mosTemperatureHighProtectChanged)
    def mosTemperatureHighProtect(self):
        return str(self.update_needed['mosTemperatureHighProtect'][0])

    @pyqtProperty(bool, notify=envTemperatureHighProtectChanged)
    def envTemperatureHighProtect(self):
        return str(self.update_needed['envTemperatureHighProtect'][0])

    @pyqtProperty(bool, notify=dischargingMosNoFunctionChanged)
    def dischargingMosNoFunction(self):
        return str(self.update_needed['dischargingMosNoFunction'][0])

    @pyqtProperty(bool, notify=chargingMosNoFunctionChanged)
    def chargingMosNoFunction(self):
        return str(self.update_needed['chargingMosNoFunction'][0])

    @pyqtProperty(bool, notify=eepromWriteFailChanged)
    def eepromWriteFail(self):
        return str(self.update_needed['eepromWriteFail'][0])

    @pyqtProperty(bool, notify=notChargingUnderVoltageChanged)
    def notChargingUnderVoltage(self):
        return str(self.update_needed['notChargingUnderVoltage'][0])

    @pyqtProperty(bool, notify=shortProtectChanged)
    def shortProtect(self):
        return str(self.update_needed['shortProtect'][0])

    @pyqtProperty(bool, notify=dischargingMosFetStatusChanged)
    def dischargingMosFetStatus(self):
        return str(self.update_needed['dischargingMosFetStatus'][0])

    @pyqtProperty(bool, notify=chargingMosFetStatusChanged)
    def chargingMosFetStatus(self):
        return str(self.update_needed['chargingMosFetStatus'][0])

    @pyqtProperty(bool, notify=preChargingMosFetStatusChanged)
    def preChargingMosFetStatus(self):
        return str(self.update_needed['preChargingMosFetStatus'][0])

    @pyqtProperty(bool, notify=heaterSwitchChanged)
    def heaterSwitch(self):
        return str(self.update_needed['heaterSwitch'][0])

    @pyqtProperty(bool, notify=gprsChanged)
    def gprs(self):
        return str(self.update_needed['gprs'][0])

    @pyqtProperty(bool, notify=chargerAdapterPluginChanged)
    def chargerAdapterPlugin(self):
        return str(self.update_needed['chargerAdapterPlugin'][0])

    @pyqtProperty(bool, notify=loaderConnectionChanged)
    def loaderConnection(self):
        return str(self.update_needed['loaderConnection'][0])


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



from PyQt5.QtCore import *
from threading import Timer
from BatteryModel import BatteryModel
from BatteryRecordModel import BatteryRecordModel


class BatteryStatus(QObject):
    OFF = 0
    ON = 1

    batteryUpdated = pyqtSignal(object)
    cells_countChanged = pyqtSignal(object)
    voltageChanged = pyqtSignal(object)
    currentChanged = pyqtSignal(object)
    socChanged = pyqtSignal(object)
    sohChanged = pyqtSignal(object)
    maxCellVoltageChanged = pyqtSignal(object)
    maxCellVoltageNrChanged = pyqtSignal(object)
    minCellVoltageChanged = pyqtSignal(object)
    minCellVoltageNrChanged = pyqtSignal(object)
    maxCellTemperatureChanged = pyqtSignal(object)
    maxCellTemperatureNrChanged = pyqtSignal(object)
    minCellTemperatureChanged = pyqtSignal(object)
    minCellTemperatureNrChanged = pyqtSignal(object)
    maxCellsVoltageDiffChanged = pyqtSignal(object)

    cellOverVoltageAlarmChanged = pyqtSignal(object)
    cellUnderVoltageAlarmChanged = pyqtSignal(object)
    batteryOverVoltageAlarmChanged = pyqtSignal(object)
    batteryUnderVoltageAlarmChanged = pyqtSignal(object)
    batteryDischargingOverCurrentAlarmChanged = pyqtSignal(object)
    batteryChargingOverCurrentAlarmChanged = pyqtSignal(object)
    batteryDischargingOverTemperatureAlarmChanged = pyqtSignal(object)
    batteryChargingOverTemperatureAlarmChanged = pyqtSignal(object)
    batteryDischargingUnderTemperatureAlarmChanged = pyqtSignal(object)
    batteryChargingUnderTemperatureAlarmChanged = pyqtSignal(object)
    socOverThresholdAlarmChanged = pyqtSignal(object)
    socUnderThresholdAlarmChanged = pyqtSignal(object)
    voltageDiffAlarmChanged = pyqtSignal(object)
    temperatureDiffAlarmChanged = pyqtSignal(object)
    mosTemperatureHighAlarmChanged = pyqtSignal(object)
    envTemperatureHighAlarmChanged = pyqtSignal(object)

    cellOverVoltageProtectChanged = pyqtSignal(object)
    cellUnderVoltageProtectChanged = pyqtSignal(object)
    batteryOverVoltageProtectChanged = pyqtSignal(object)
    batteryUnderVoltageProtectChanged = pyqtSignal(object)
    batteryDischargingOverCurrentProtectChanged = pyqtSignal(object)
    batteryChargingOverCurrentProtectChanged = pyqtSignal(object)
    batteryDischargingOverTemperatureProtectChanged = pyqtSignal(object)
    batteryChargingOverTemperatureProtectChanged = pyqtSignal(object)
    batteryDischargingUnderTemperatureProtectChanged = pyqtSignal(object)
    batteryChargingUnderTemperatureProtectChanged = pyqtSignal(object)
    socOverThresholdProtectChanged = pyqtSignal(object)
    socUnderThresholdProtectChanged = pyqtSignal(object)
    voltageDiffProtectChanged = pyqtSignal(object)
    temperatureDiffProtectChanged = pyqtSignal(object)
    mosTemperatureHighProtectChanged = pyqtSignal(object)
    envTemperatureHighProtectChanged = pyqtSignal(object)

    dischargingMosNoFunctionChanged = pyqtSignal(object)
    chargingMosNoFunctionChanged = pyqtSignal(object)
    eepromWriteFailChanged = pyqtSignal(object)
    notChargingUnderVoltageChanged = pyqtSignal(object)
    shortProtectChanged = pyqtSignal(object)

    dischargingMosFetStatusChanged = pyqtSignal(object)
    chargingMosFetStatusChanged = pyqtSignal(object)
    preChargingMosFetStatusChanged = pyqtSignal(object)
    heaterSwitchChanged = pyqtSignal(object)
    gprsChanged = pyqtSignal(object)
    chargerAdapterPluginChanged = pyqtSignal(object)
    loaderConnectionChanged = pyqtSignal(object)

    systemStatusChanged = pyqtSignal(object)

    cellsChanged = pyqtSignal(object)
    thermal_sensorsChanged = pyqtSignal(object)

    read_battery_signal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        self.batteryThermalSensorsModel = BatteryModel(datas=[])
        self.batteryCellsBalanceModel = BatteryModel(datas=[])
        self.batteryCellsVoltageModel = BatteryModel(datas=[])
        self.batteryRecordModel = BatteryRecordModel()

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
            'thermal_sensors': [[], self.batteryThermalSensorsModel.dataReceived],
            'cells_balance': [[], self.batteryCellsBalanceModel.dataReceived],
            'cells_voltage': [[], self.batteryCellsVoltageModel.dataReceived]
        }

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
        return self.update_needed['cellOverVoltageAlarm'][0] == '1'

    @pyqtProperty(bool, notify=cellUnderVoltageAlarmChanged)
    def cellUnderVoltageAlarm(self):
        return self.update_needed['cellUnderVoltageAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryOverVoltageAlarmChanged)
    def batteryOverVoltageAlarm(self):
        return self.update_needed['batteryOverVoltageAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryUnderVoltageAlarmChanged)
    def batteryUnderVoltageAlarm(self):
        return self.update_needed['batteryUnderVoltageAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingOverCurrentAlarmChanged)
    def batteryDischargingOverCurrentAlarm(self):
        return self.update_needed['batteryDischargingOverCurrentAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingOverCurrentAlarmChanged)
    def batteryChargingOverCurrentAlarm(self):
        return self.update_needed['batteryChargingOverCurrentAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingOverTemperatureAlarmChanged)
    def batteryDischargingOverTemperatureAlarm(self):
        return self.update_needed['batteryDischargingOverTemperatureAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingOverTemperatureAlarmChanged)
    def batteryChargingOverTemperatureAlarm(self):
        return self.update_needed['batteryChargingOverTemperatureAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingUnderTemperatureAlarmChanged)
    def batteryDischargingUnderTemperatureAlarm(self):
        return self.update_needed['batteryDischargingUnderTemperatureAlarm'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingUnderTemperatureAlarmChanged)
    def batteryChargingUnderTemperatureAlarm(self):
        return self.update_needed['batteryChargingUnderTemperatureAlarm'][0] == '1'

    @pyqtProperty(bool, notify=socOverThresholdAlarmChanged)
    def socOverThresholdAlarm(self):
        return self.update_needed['socOverThresholdAlarm'][0] == '1'

    @pyqtProperty(bool, notify=socUnderThresholdAlarmChanged)
    def socUnderThresholdAlarm(self):
        return self.update_needed['socUnderThresholdAlarm'][0] == '1'

    @pyqtProperty(bool, notify=voltageDiffAlarmChanged)
    def voltageDiffAlarm(self):
        return self.update_needed['voltageDiffAlarm'][0] == '1'

    @pyqtProperty(bool, notify=temperatureDiffAlarmChanged)
    def temperatureDiffAlarm(self):
        return self.update_needed['temperatureDiffAlarm'][0] == '1'

    @pyqtProperty(bool, notify=mosTemperatureHighAlarmChanged)
    def mosTemperatureHighAlarm(self):
        return self.update_needed['mosTemperatureHighAlarm'][0] == '1'

    @pyqtProperty(bool, notify=envTemperatureHighAlarmChanged)
    def envTemperatureHighAlarm(self):
        return self.update_needed['envTemperatureHighAlarm'][0] == '1'

    @pyqtProperty(bool, notify=cellOverVoltageProtectChanged)
    def cellOverVoltageProtect(self):
        return self.update_needed['cellOverVoltageProtect'][0] == '1'

    @pyqtProperty(bool, notify=cellUnderVoltageProtectChanged)
    def cellUnderVoltageProtect(self):
        return self.update_needed['cellUnderVoltageProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryOverVoltageProtectChanged)
    def batteryOverVoltageProtect(self):
        return self.update_needed['batteryOverVoltageProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryUnderVoltageProtectChanged)
    def batteryUnderVoltageProtect(self):
        return self.update_needed['batteryUnderVoltageProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingOverCurrentProtectChanged)
    def batteryDischargingOverCurrentProtect(self):
        return self.update_needed['batteryDischargingOverCurrentProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingOverCurrentProtectChanged)
    def batteryChargingOverCurrentProtect(self):
        return self.update_needed['batteryChargingOverCurrentProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingOverTemperatureProtectChanged)
    def batteryDischargingOverTemperatureProtect(self):
        return self.update_needed['batteryDischargingOverTemperatureProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingOverTemperatureProtectChanged)
    def batteryChargingOverTemperatureProtect(self):
        return self.update_needed['batteryChargingOverTemperatureProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryDischargingUnderTemperatureProtectChanged)
    def batteryDischargingUnderTemperatureProtect(self):
        return self.update_needed['batteryDischargingUnderTemperatureProtect'][0] == '1'

    @pyqtProperty(bool, notify=batteryChargingUnderTemperatureProtectChanged)
    def batteryChargingUnderTemperatureProtect(self):
        return self.update_needed['batteryChargingUnderTemperatureProtect'][0] == '1'

    @pyqtProperty(bool, notify=socOverThresholdProtectChanged)
    def socOverThresholdProtect(self):
        return self.update_needed['socOverThresholdProtect'][0] == '1'

    @pyqtProperty(bool, notify=socUnderThresholdProtectChanged)
    def socUnderThresholdProtect(self):
        return self.update_needed['socUnderThresholdProtect'][0] == '1'

    @pyqtProperty(bool, notify=voltageDiffProtectChanged)
    def voltageDiffProtect(self):
        return self.update_needed['voltageDiffProtect'][0] == '1'

    @pyqtProperty(bool, notify=temperatureDiffProtectChanged)
    def temperatureDiffProtect(self):
        return self.update_needed['temperatureDiffProtect'][0] == '1'

    @pyqtProperty(bool, notify=mosTemperatureHighProtectChanged)
    def mosTemperatureHighProtect(self):
        return self.update_needed['mosTemperatureHighProtect'][0] == '1'

    @pyqtProperty(bool, notify=envTemperatureHighProtectChanged)
    def envTemperatureHighProtect(self):
        return self.update_needed['envTemperatureHighProtect'][0] == '1'

    @pyqtProperty(bool, notify=dischargingMosNoFunctionChanged)
    def dischargingMosNoFunction(self):
        return self.update_needed['dischargingMosNoFunction'][0] == '1'

    @pyqtProperty(bool, notify=chargingMosNoFunctionChanged)
    def chargingMosNoFunction(self):
        return self.update_needed['chargingMosNoFunction'][0] == '1'

    @pyqtProperty(bool, notify=eepromWriteFailChanged)
    def eepromWriteFail(self):
        return self.update_needed['eepromWriteFail'][0] == '1'

    @pyqtProperty(bool, notify=notChargingUnderVoltageChanged)
    def notChargingUnderVoltage(self):
        return self.update_needed['notChargingUnderVoltage'][0] == '1'

    @pyqtProperty(bool, notify=shortProtectChanged)
    def shortProtect(self):
        return self.update_needed['shortProtect'][0] == '1'

    @pyqtProperty(bool, notify=dischargingMosFetStatusChanged)
    def dischargingMosFetStatus(self):
        return self.update_needed['dischargingMosFetStatus'][0] == '1'

    @pyqtProperty(bool, notify=chargingMosFetStatusChanged)
    def chargingMosFetStatus(self):
        return self.update_needed['chargingMosFetStatus'][0] == '1'

    @pyqtProperty(bool, notify=preChargingMosFetStatusChanged)
    def preChargingMosFetStatus(self):
        return self.update_needed['preChargingMosFetStatus'][0] == '1'

    @pyqtProperty(bool, notify=heaterSwitchChanged)
    def heaterSwitch(self):
        return self.update_needed['heaterSwitch'][0] == '1'

    @pyqtProperty(bool, notify=gprsChanged)
    def gprs(self):
        return self.update_needed['gprs'][0] == '1'

    @pyqtProperty(bool, notify=chargerAdapterPluginChanged)
    def chargerAdapterPlugin(self):
        return self.update_needed['chargerAdapterPlugin'][0] == '1'

    @pyqtProperty(bool, notify=loaderConnectionChanged)
    def loaderConnection(self):
        return self.update_needed['loaderConnection'][0] == '1'


    @pyqtProperty(str, notify=systemStatusChanged)
    def status(self):
        return str(self.update_needed['status'][0])


    def update(self, *args, **kwargs):
        # print(args)
        # print(kwargs)

        if len(args):
            if args[0] in self.update_needed:
                item = self.update_needed[args[0]]
                item[0] = args[1]
                item[1].emit(args[1])

        for k, v in kwargs.items():
            item = self.update_needed[k]
            item[0] = v
            item[1].emit(v)

    @pyqtSlot(str)
    def readBattery(self, func_name):
        self.read_battery_signal.emit(func_name)

    @pyqtSlot()
    def recordOneBatteryItem(self):
        data = [0,
                self.update_needed['voltage'][0],
                self.update_needed['current'][0],
                self.update_needed['soc'][0],
                self.update_needed['soh'][0],
                self.update_needed['maxCellVoltage'][0],
                self.update_needed['maxCellVoltageNr'][0],
                self.update_needed['minCellVoltage'][0],
                self.update_needed['minCellVoltageNr'][0],
                self.update_needed['maxCellsVoltageDiff'][0],
                self.update_needed['maxCellTemperature'][0],
                self.update_needed['maxCellTemperatureNr'][0],
                self.update_needed['minCellTemperature'][0],
                self.update_needed['minCellTemperatureNr'][0],
                len(self.update_needed['thermal_sensors'][0]),
                len(self.update_needed['cells_voltage'][0])
                ]

        data.extend(self.update_needed['thermal_sensors'][0])
        data.extend(self.update_needed['cells_voltage'][0])

        self.batteryRecordModel.update(data)

    @pyqtSlot()
    def clearAllBatteryRecord(self):
        self.batteryRecordModel.clear()

    @pyqtSlot(str)
    def saveRecordToFile(self, url: str):
        self.batteryRecordModel.saveToFile(url)



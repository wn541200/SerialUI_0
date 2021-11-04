from PyQt5.QtCore import *


class SystemSettings(QObject):
    read_system_setting_signal = pyqtSignal(str)
    write_system_setting_signal = pyqtSignal(str, object)

    projectIdChanged = pyqtSignal(object)
    bmsIdChanged = pyqtSignal(object)
    swVersionChanged = pyqtSignal(object)
    hwVersionChanged = pyqtSignal(object)
    protocolVersionChanged = pyqtSignal(object)
    bmsSNChanged = pyqtSignal(object)
    bmsMPDateChanged = pyqtSignal(object)
    bmsProductDateChanged = pyqtSignal(object)
    cellCountChanged = pyqtSignal(object)
    thermalCountChanged = pyqtSignal(object)
    balanceEnableFlagChanged = pyqtSignal(object)
    balanceEnableVoltageDiffChanged = pyqtSignal(object)
    balanceEnableVoltageChanged = pyqtSignal(object)
    balanceDisableVoltageChanged = pyqtSignal(object)
    chargingCircleSettingChanged = pyqtSignal(object)
    totalChargingCirCleChanged = pyqtSignal(object)
    realCapacityChanged = pyqtSignal(object)
    settingCapacityChanged = pyqtSignal(object)
    sohChanged = pyqtSignal(object)
    socChanged = pyqtSignal(object)
    sampleResistanceValueChanged = pyqtSignal(object)
    zeroCurrentADCValueChanged = pyqtSignal(object)
    dischargingCurrentRatioChanged = pyqtSignal(object)
    chargingCurrentRatioChanged = pyqtSignal(object)
    bmsRTCDateChanged = pyqtSignal(object)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        # 定义为一个字典，把几个东西绑定为一条
        # 变量名 / 值 / 信号
        self.update_needed = {
            'projectId': ['', self.projectIdChanged],
            'bmsId': ['', self.bmsIdChanged],
            'swVersion': ['', self.swVersionChanged],
            'hwVersion': ['', self.hwVersionChanged],
            'protocolVersion': ['', self.protocolVersionChanged],
            'bmsSN': ['', self.bmsSNChanged],
            'bmsProductDate': ['', self.bmsProductDateChanged],
            'bmsMPDate': ['', self.bmsMPDateChanged],
            'cellCount': [0, self.cellCountChanged],
            'thermalCount': [0, self.thermalCountChanged],
            'balanceEnableFlag': ['', self.balanceEnableFlagChanged],
            'balanceEnableVoltageDiff': [0, self.balanceEnableVoltageDiffChanged],
            'balanceEnableVoltage': [0, self.balanceEnableVoltageChanged],
            'balanceDisableVoltage': [0, self.balanceDisableVoltageChanged],
            'chargingCircleSetting': [0, self.chargingCircleSettingChanged],
            'totalChargingCirCle': [0, self.totalChargingCirCleChanged],
            'realCapacity': [0, self.realCapacityChanged],
            'settingCapacity': [0, self.settingCapacityChanged],
            'soh': [0, self.sohChanged],
            'soc': [0, self.socChanged],
            'sampleResistanceValue': [0, self.sampleResistanceValueChanged],
            'zeroCurrentADCValue': [0, self.zeroCurrentADCValueChanged],
            'dischargingCurrentRatio': [0, self.dischargingCurrentRatioChanged],
            'chargingCurrentRatio': [0, self.chargingCurrentRatioChanged],
            'bmsRTCDate': ['', self.bmsRTCDateChanged]
        }

    @pyqtProperty(str, notify=projectIdChanged)
    def projectId(self):
        return str(self.update_needed['projectId'][0])

    @pyqtProperty(str, notify=bmsIdChanged)
    def bmsId(self):
        return str(self.update_needed['bmsId'][0])

    @pyqtProperty(str, notify=swVersionChanged)
    def swVersion(self):
        return str(self.update_needed['swVersion'][0])

    @pyqtProperty(str, notify=hwVersionChanged)
    def hwVersion(self):
        return str(self.update_needed['hwVersion'][0])

    @pyqtProperty(str, notify=protocolVersionChanged)
    def protocolVersion(self):
        return str(self.update_needed['protocolVersion'][0])

    @pyqtProperty(str, notify=bmsSNChanged)
    def bmsSN(self):
        return str(self.update_needed['bmsSN'][0])

    @pyqtProperty(str, notify=bmsProductDateChanged)
    def bmsProductDate(self):
        return str(self.update_needed['bmsProductDate'][0])

    @pyqtProperty(str, notify=bmsMPDateChanged)
    def bmsMPDate(self):
        return str(self.update_needed['bmsMPDate'][0])

    @pyqtProperty(str, notify=cellCountChanged)
    def cellCount(self):
        return str(self.update_needed['cellCount'][0])

    @pyqtProperty(str, notify=thermalCountChanged)
    def thermalCount(self):
        return str(self.update_needed['thermalCount'][0])

    @pyqtProperty(str, notify=balanceEnableFlagChanged)
    def balanceEnableFlag(self):
        return str(self.update_needed['balanceEnableFlag'][0])

    @pyqtProperty(str, notify=balanceEnableVoltageDiffChanged)
    def balanceEnableVoltageDiff(self):
        return str(self.update_needed['balanceEnableVoltageDiff'][0])

    @pyqtProperty(str, notify=balanceEnableVoltageChanged)
    def balanceEnableVoltage(self):
        return str(self.update_needed['balanceEnableVoltage'][0])

    @pyqtProperty(str, notify=balanceDisableVoltageChanged)
    def balanceDisableVoltage(self):
        return str(self.update_needed['balanceDisableVoltage'][0])

    @pyqtProperty(str, notify=chargingCircleSettingChanged)
    def chargingCircleSetting(self):
        return str(self.update_needed['chargingCircleSetting'][0])

    @pyqtProperty(str, notify=totalChargingCirCleChanged)
    def totalChargingCirCle(self):
        return str(self.update_needed['totalChargingCirCle'][0])

    @pyqtProperty(str, notify=realCapacityChanged)
    def realCapacity(self):
        return str(self.update_needed['realCapacity'][0])

    @pyqtProperty(str, notify=settingCapacityChanged)
    def settingCapacity(self):
        return str(self.update_needed['settingCapacity'][0])

    @pyqtProperty(str, notify=sohChanged)
    def soh(self):
        return str(self.update_needed['soh'][0])

    @pyqtProperty(str, notify=socChanged)
    def soc(self):
        return str(self.update_needed['soc'][0])

    @pyqtProperty(str, notify=sampleResistanceValueChanged)
    def sampleResistanceValue(self):
        return str(self.update_needed['sampleResistanceValue'][0])

    @pyqtProperty(str, notify=zeroCurrentADCValueChanged)
    def zeroCurrentADCValue(self):
        return str(self.update_needed['zeroCurrentADCValue'][0])

    @pyqtProperty(str, notify=dischargingCurrentRatioChanged)
    def dischargingCurrentRatio(self):
        return str(self.update_needed['dischargingCurrentRatio'][0])

    @pyqtProperty(str, notify=chargingCurrentRatioChanged)
    def chargingCurrentRatio(self):
        return str(self.update_needed['chargingCurrentRatio'][0])

    @pyqtProperty(str, notify=bmsRTCDateChanged)
    def bmsRTCDate(self):
        return str(self.update_needed['bmsRTCDate'][0])

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
    def readSystemSetting(self, func_name:str):
        self.read_system_setting_signal.emit(func_name)

    @pyqtSlot(str, QVariant)
    def writeSystemSetting(self, func_name:str, data):
        self.write_system_setting_signal.emit(func_name, data)
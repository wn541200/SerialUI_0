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
    statusChanged = pyqtSignal(str)
    discharging_mosChanged = pyqtSignal(str)
    precharging_mosChanged = pyqtSignal(str)
    heater_switchChanged = pyqtSignal(str)
    gprsChanged = pyqtSignal(str)
    charger_adapterChanged = pyqtSignal(str)
    loaderChanged = pyqtSignal(str)
    cellsChanged = pyqtSignal(str)
    thermal_sensorsChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        # 定义为一个字典，把几个东西绑定为一条
        # 变量名 / 值 / 信号
        self.update_needed = {
            'cells_count': [0, self.cells_countChanged],
            'voltage': [5, self.voltageChanged],
            'current': [3, self.currentChanged],
            'soc': [100, self.socChanged],
            'soh': [100, self.sohChanged],
            'status': [0, self.statusChanged],
            'discharging_mos': [self.OFF, self.discharging_mosChanged],
            'precharging_mos': [self.OFF, self.precharging_mosChanged],
            'heater_switch': [self.OFF, self.heater_switchChanged],
            'gprs': [self.OFF, self.gprsChanged],
            'charger_adapter': [self.OFF, self.charger_adapterChanged],
            'loader': [self.OFF, self.loaderChanged],
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

    @pyqtProperty(str, notify=currentChanged)
    def current(self):
        return str(self.update_needed['current'][0])

    @pyqtProperty(str, notify=socChanged)
    def soc(self):
        return str(self.update_needed['soc'][0])

    @pyqtProperty(str, notify=sohChanged)
    def soh(self):
        return str(self.update_needed['soh'][0])

    @pyqtProperty(str, notify=statusChanged)
    def status(self):
        return str(self.update_needed['status'][0])

    def foo(self):
        self.update(soc=90)
        self.batteryModel.dataReceived.emit(2)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            item = self.update_needed[k]
            item[0] = v
            item[1].emit(str(v))



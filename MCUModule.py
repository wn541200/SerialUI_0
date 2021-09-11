from PyQt5.QtCore import *
from uart import Uart
from dbjprotocol import DBJProtocol
from battery import BatteryStatus


class MCUModule(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.uartModule = Uart()
        self.protocol = DBJProtocol()
        self.batteryStatus = BatteryStatus()

        self.uartModule.rawDataReceeved.connect(self.protocol.on_uart_event)
        self.protocol.voltageChanged.connect(self.batteryStatus.update)
        # 4e 42 01 00 1e 02 8a 0c




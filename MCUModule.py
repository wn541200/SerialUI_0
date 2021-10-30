from PyQt5.QtCore import *
from uart import Uart
from dbjprotocol import DBJProtocol
from battery import BatteryStatus
from BatterySettins import BatterySettings
from SystemSettings import SystemSettings
from HistoryRecord import HistoryRecord


class MCUModule(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.uartModule = Uart()
        self.protocol = DBJProtocol()
        self.batteryStatus = BatteryStatus()
        self.batterySettings = BatterySettings()
        self.systemSettings = SystemSettings()
        self.historyRecord = HistoryRecord()


        # 将串口模块接收到的数据发送到协议模块解析
        self.uartModule.rawDataReceeved.connect(self.protocol.on_uart_event)

        # 发送协议模块的command到uart
        self.protocol.port_send_request_signal.connect(self.uartModule.send)

        self.batteryStatus.read_battery_signal.connect(self.protocol.command_read_mcu)

        self.batterySettings.read_battery_signal.connect(self.protocol.command_read_mcu)
        self.batterySettings.write_battery_signal.connect(self.protocol.command_write_mcu)

        self.systemSettings.read_system_setting_signal.connect(self.protocol.command_read_mcu)
        self.systemSettings.write_system_setting_signal.connect(self.protocol.command_write_mcu)
        self.historyRecord.read_history_record_signal.connect(self.protocol.command_read_mcu)

        self.protocol.batteryStatusChanged.connect(self.batteryStatus.update)
        self.protocol.batterySettingsChanged.connect(self.batterySettings.updateItem)
        self.protocol.systemStatusChanged.connect(self.systemSettings.update)
        self.protocol.historyRecordCountChanged.connect(self.historyRecord.onHistoryRecordCount)
        # 4e 42 01 00 1e 02 8a 0c




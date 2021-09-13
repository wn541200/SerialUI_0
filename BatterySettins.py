from PyQt5.QtCore import *


class SettingItem(object):
    def __init__(self):
        self.name = ''
        self.enabled = False
        self.protect_threshold = 0
        self.protect_hysteresis = 0
        self.protect_threshold_delay = 0
        self.protect_hysteresis_delay = 0
        self.alarm_threshold = 0
        self.alarm_threshold_delay = 0


class BatterySettings(QAbstractListModel):
    set_param_to_battery_signal = pyqtSignal(str, object)

    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {
                            self.role: b'name',
                            self.role + 1: b'enabled',
                            self.role + 2: b'protect_threshold',
                            self.role + 3: b'protect_hysteresis',
                            self.role + 4: b'protect_threshold_delay',
                            self.role + 5: b'protect_hysteresis_delay',
                            self.role + 6: b'alarm_threshold',
                            self.role + 7: b'alarm_threshold_delay'
        }

        self.settings = {
            'cell_over_voltage': SettingItem(),
            'cell_under_voltage': SettingItem(),
            'total_over_voltage': SettingItem(),
            'total_under_voltage': SettingItem(),
            'discharging_over_current': SettingItem(),
            'charging_over_current': SettingItem(),
            'soc_over_threshold': SettingItem(),
            'soc_under_threshold': SettingItem(),

            'discharging_over_temperature': SettingItem(),
            'charging_over_temperature': SettingItem(),
            'discharging_under_temperature': SettingItem(),
            'charging_under_temperature': SettingItem(),
            'voltage_diff_great': SettingItem(),
            'temperature_diff_great': SettingItem(),
            'mos_over_temperature': SettingItem(),
            'environment_over_temperature': SettingItem()
        }

        self.index_map = {
            0: 'cell_over_voltage',
            1: 'cell_under_voltage',
            2: 'total_over_voltage',
            3: 'total_under_voltage',
            4: 'discharging_over_current',
            5: 'charging_over_current',
            6: 'soc_over_threshold',
            7: 'soc_under_threshold',

            8: 'discharging_over_temperature',
            9: 'charging_over_temperature',
            10: 'discharging_under_temperature',
            11: 'charging_under_temperature',
            12: 'voltage_diff_great',
            13: 'temperature_diff_great',
            14: 'mos_over_temperature',
            15: 'environment_over_temperature'
        }

    def data(self, index: QModelIndex, role=None):
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """

        item_name = self.index_map[index.row()]

        if role == self.role:
            return self.settings[item_name].name

        if role == (self.role+1):
            return self.settings[item_name].enabled

        if role == (self.role+2):
            return self.settings[item_name].protect_threshold

        if role == (self.role+3):
            return self.settings[item_name].protect_hysteresis

        if role == (self.role+4):
            return self.settings[item_name].protect_threshold_delay

        if role == (self.role+5):
            return self.settings[item_name].protect_hysteresis_delay

        if role == (self.role+6):
            return self.settings[item_name].alarm_threshold

        if role == (self.role+7):
            return self.settings[item_name].alarm_threshold_delay

    def roleNames(self):
        """ roleNames(self) -> Dict[int, QByteArray] """
        return self.m_roleNames

    def rowCount(self, parent=None, *args, **kwargs):
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        print(len(self.settings))
        return len(self.settings)


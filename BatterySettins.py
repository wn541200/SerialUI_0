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


class BatterySettings(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
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

from PyQt5.QtCore import *
from urllib.parse import urlparse
import json
import copy


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
    read_battery_signal = pyqtSignal(str, object)
    write_battery_signal = pyqtSignal(str, object)

    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {
                            self.role: b'name',
                            self.role + 1: b'itemEnabled',
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

        self.settings['cell_over_voltage'].name = '单体过压'
        self.settings['cell_under_voltage'].name = '单体欠压'
        self.settings['total_over_voltage'].name = '总体过压'
        self.settings['total_under_voltage'].name = '总体欠压'
        self.settings['discharging_over_current'].name = '放电过流'
        self.settings['charging_over_current'].name = '充电过流'
        self.settings['soc_over_threshold'].name = 'SOC过高'
        self.settings['soc_under_threshold'].name = 'SOC过低'

        self.settings['discharging_over_temperature'].name = '放电高温'
        self.settings['charging_over_temperature'].name = '充电高温'
        self.settings['discharging_under_temperature'].name = '放电低温'
        self.settings['charging_under_temperature'].name = '充电低温'
        self.settings['voltage_diff_great'].name = '压差过大'
        self.settings['temperature_diff_great'].name = '温差过大'
        self.settings['mos_over_temperature'].name = 'MOS高温'
        self.settings['environment_over_temperature'].name = '环境高温'

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
        return len(self.settings)

    @pyqtSlot(int, bool, int, int, int, int, int, int)
    def setItem(self, row, enabled, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay):
        ix = self.index(row, 0)
        item_name = self.index_map[row]
        item = self.settings[item_name]
        item.enabled = enabled
        item.protect_threshold = protect_threshold
        item.protect_hysteresis = protect_hysteresis
        item.protect_threshold_delay = protect_threshold_delay
        item.protect_hysteresis_delay = protect_hysteresis_delay
        item.alarm_threshold = alarm_threshold
        item.alarm_threshold_delay = alarm_threshold_delay
        self.dataChanged.emit(ix, ix, self.roleNames())
        self.write_battery_signal.emit(item_name, self.settings[item_name])

    @pyqtSlot(str, bool, int, int, int, int, int, int)
    def updateItem(self, item_name, enabled, protect_threshold, protect_hysteresis, protect_threshold_delay,
                protect_hysteresis_delay, alarm_threshold, alarm_threshold_delay):

        for row, name in self.index_map.items():
            if name == item_name:
                ix = self.index(row, 0)
                break

        # ix = self.index(0, 0)
        item = self.settings[item_name]
        item.enabled = enabled
        item.protect_threshold = protect_threshold
        item.protect_hysteresis = protect_hysteresis
        item.protect_threshold_delay = protect_threshold_delay
        item.protect_hysteresis_delay = protect_hysteresis_delay
        item.alarm_threshold = alarm_threshold
        item.alarm_threshold_delay = alarm_threshold_delay
        self.dataChanged.emit(ix, ix, self.roleNames())

    @pyqtSlot(int)
    def readItemFromMCU(self, row):
        item_name = self.index_map[row]
        self.read_battery_signal.emit(item_name, self.settings[item_name])

    @pyqtSlot(str)
    def saveToFile(self, url: str):
        print('saveToFile')
        path = urlparse(url).path
        d = {}
        l = []
        for k, v in self.settings.items():
            d['name'] = v.name
            d['enabled'] = v.enabled
            d['protect_threshold'] = v.protect_threshold
            d['protect_hysteresis'] = v.protect_hysteresis
            d['protect_threshold_delay'] = v.protect_threshold_delay
            d['protect_hysteresis_delay'] = v.protect_hysteresis_delay
            d['alarm_threshold'] = v.alarm_threshold
            d['alarm_threshold_delay'] = v.alarm_threshold_delay

            d1 = copy.deepcopy(d)
            l.append(d1)

        try:
            with open(path[1:], 'w', encoding='utf-8') as f:
                json.dump(l, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)

    @pyqtSlot(str)
    def readFromFile(self, url: str):
        print('readFromFile')
        path = urlparse(url).path

        try:
            with open(path[1:], 'r', encoding='utf-8') as f:
                data = json.load(f)
                for d in data:
                    for k, v in self.settings.items():
                        if d['name'] == v.name:
                            v.enabled = d['enabled']
                            v.protect_threshold = d['protect_threshold']
                            v.protect_hysteresis = d['protect_hysteresis']
                            v.protect_threshold_delay = d['protect_threshold_delay']
                            v.protect_hysteresis_delay = d['protect_hysteresis_delay']
                            v.alarm_threshold = d['alarm_threshold']
                            v.alarm_threshold_delay = d['alarm_threshold_delay']
                            self.updateItem(k, v.enabled == 1, v.protect_threshold,
                                            v.protect_hysteresis, v.protect_threshold_delay,
                                            v.protect_hysteresis_delay, v.alarm_threshold,
                                            v.alarm_threshold_delay)
        except Exception as e:
            print(e)

    # def settingsToMCU(self):

from urllib.parse import urlparse

from PyQt5.QtCore import *
import csv


class BatteryRecordModel(QAbstractListModel):
    dataReceived = pyqtSignal(object)
    roleNamesChanged = pyqtSignal(int, arguments=["count"])
    errorMessage = pyqtSignal(str, arguments=["errorMSG"])

    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {self.role: b'time',
                            self.role+1: b'voltage',
                            self.role + 2: b'current',
                            self.role + 3: b'soc',
                            self.role + 4: b'soh',
                            self.role + 5: b'maxCellVoltage',
                            self.role + 6: b'maxCellVoltageNr',
                            self.role + 7: b'minCellVoltage',
                            self.role + 8: b'minCellVoltageNr',
                            self.role + 9: b'maxCellsVoltageDiff',
                            self.role + 10: b'maxCellTemperature',
                            self.role + 11: b'maxCellTemperatureNr',
                            self.role + 12: b'minCellTemperature',
                            self.role + 13: b'minCellTemperatureNr',
                            self.role + 14: b'nrThermals',
                            self.role + 15: b'nrCells'
                            }
        self.battery_data = []
        self.dataReceived.connect(self.update)

    def data(self, index: QModelIndex, role=None):
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        return self.battery_data[index.row()][role-self.role]

    def roleNames(self):
        """ roleNames(self) -> Dict[int, QByteArray] """
        return self.m_roleNames

    def rowCount(self, parent=None, *args, **kwargs):
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        return len(self.battery_data)

    @pyqtSlot(result=list)
    def getRoleNames(self):
        names = []
        for i in range(len(self.m_roleNames)):
            names.append(str(self.m_roleNames[self.role+i], encoding="utf-8"))

        return names
        # return [1, 2, 3]

    @pyqtSlot(object)
    def update(self, data):
        # ix = self.index(0, 0)
        # self.battery_data[0] = '3.5V'
        # self.dataChanged.emit(ix, ix, self.roleNames())
        # self.beginResetModel()
        # self.battery_data = []
        # self.endResetModel()

        if len(data) > len(self.m_roleNames):
            thermal_count = data[14]
            if thermal_count > 0:
                for i in range(thermal_count):
                    self.m_roleNames[self.role+16+i] = b'thermal' + str(i+1).encode('utf-8')

            cell_count = data[15]
            length = len(self.m_roleNames)
            if cell_count > 0:
                for i in range(cell_count):
                    self.m_roleNames[self.role + length + i] = b'cell' + str(i+1).encode('utf-8')

            # print(self.m_roleNames)
            self.roleNamesChanged.emit(len(self.m_roleNames))

        else:
            self.beginInsertRows(QModelIndex(), len(self.battery_data), len(self.battery_data))
            self.battery_data.append(data)
            self.endInsertRows()
        # print(self.battery_data)

    @pyqtSlot()
    def clear(self):
        self.beginResetModel()
        self.battery_data = []
        self.endResetModel()

    @pyqtSlot(str)
    def saveToFile(self, url: str):
        headers = ['时间', '总电压', '总电流', 'soc', 'soh', '最高电压', '最高电压序号', '最低电压', '最低电压序号', '最大压差',
                   '最高温度', '最高温度序号', '最低温度', '最低温度序号', '温度传感器数量', '电芯数量']

        roleNames = self.getRoleNames()
        if len(roleNames) > len(headers):
            headers.extend(roleNames[len(headers):])

        path = urlparse(url).path
        # 本地文件host name为空，解析后的路径还带有一个/,需要跳过
        try:
            with open(path[1:], 'w', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(headers)
                f_csv.writerows(self.battery_data)
        except Exception as e:
            self.errorMessage.emit('写入文件失败,请检查文件是否被其他程序打开\n' + path[1:])

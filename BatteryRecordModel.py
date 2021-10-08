from PyQt5.QtCore import *


class BatteryRecordModel(QAbstractListModel):
    dataReceived = pyqtSignal(object)

    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {self.role: b'time',
                            self.role+1: b'voltage',
                            self.role + 2: b'current',
                            self.role + 3: b'soc',
                            self.role + 4: b'soh'

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

    @pyqtSlot(object)
    def update(self, data):
        # ix = self.index(0, 0)
        # self.battery_data[0] = '3.5V'
        # self.dataChanged.emit(ix, ix, self.roleNames())
        # self.beginResetModel()
        # self.battery_data = []
        # self.endResetModel()
        self.beginInsertRows(QModelIndex(), len(self.battery_data), len(self.battery_data))
        self.battery_data.append(data)
        self.endInsertRows()
        # print(self.battery_data)

    @pyqtSlot()
    def clear(self):
        self.beginResetModel()
        self.battery_data = []
        self.endResetModel()

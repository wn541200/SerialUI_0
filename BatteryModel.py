from PyQt5.QtCore import *
from threading import Timer


class BatteryModel(QAbstractListModel):
    dataReceived = pyqtSignal(int)

    def __init__(self, datas: [], parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {self.role:b'name', self.role+1:b'number'}
        self.label = datas
        self.battery_data = datas
        self.dataReceived.connect(self.update)

    def data(self, index: QModelIndex, role=None):
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        print('xxx')
        print(index.row())

        if role == self.role:
            return self.label[index.row()]

        if role == (self.role+1):
            return self.battery_data[index.row()]

    def roleNames(self):
        """ roleNames(self) -> Dict[int, QByteArray] """
        return self.m_roleNames

    def rowCount(self, parent=None, *args, **kwargs):
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        print(len(self.battery_data))
        return len(self.battery_data)

    @pyqtSlot( int)
    def update(self, data):
        # ix = self.index(0, 0)
        # self.battery_data[0] = '3.5V'
        # self.dataChanged.emit(ix, ix, self.roleNames())
        # self.beginResetModel()
        # self.battery_data = [1, 2, 3, 4, 5]
        # self.endResetModel()
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.battery_data.append(data)
        self.endInsertRows()
        print(self.battery_data)

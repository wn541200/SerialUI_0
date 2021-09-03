from PyQt5.QtCore import *
from threading import Timer


class BatteryModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {self.role:b'name', self.role+1:b'number'}
        self.label = ['电压', '电流', 'SOC', 'SOH', '系统模式']
        self.battery_data = ['4.2V', '3A', '65%', '50%', '充电']
        self.timer = Timer(5, self.update)
        self.timer.start()

    def data(self, index: QModelIndex, role=None):
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """

        if role == self.role:
            return self.label[index.row()]

        if role == (self.role+1):
            return self.battery_data[index.row()]

    def roleNames(self):
        """ roleNames(self) -> Dict[int, QByteArray] """
        return self.m_roleNames

    def rowCount(self, parent=None, *args, **kwargs):
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        return 5

    def update(self):
        ix = self.index(0, 0)
        self.battery_data[0] = '3.5V'
        self.dataChanged.emit(ix, ix, self.roleNames())

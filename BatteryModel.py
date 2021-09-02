from PyQt5.QtCore import *


class BatteryModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(QAbstractListModel, self).__init__(parent)
        self.role = Qt.UserRole
        self.m_roleNames = {self.role:b'name', self.role+1:b'number'}
        self.label = ['电压', '电流', 'SOC', 'SOH', '系统模式']
        self.battery_data = ['4.2V', '3A', '65%', '50%', 'charging']

    def data(self, index: QModelIndex, role=None):
        """ data(self, QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any """
        print('xxxxx' + str(index.row()))
        print('yyyyy' + str(role))
        if role == self.role:
            return self.label[index.row()]

        if role == (self.role+1):
            return self.battery_data[index.row()]

    def roleNames(self):
        """ roleNames(self) -> Dict[int, QByteArray] """
        print('222222')
        return self.m_roleNames

    def rowCount(self, parent=None, *args, **kwargs):
        """ rowCount(self, parent: QModelIndex = QModelIndex()) -> int """
        print('111111')
        return 5

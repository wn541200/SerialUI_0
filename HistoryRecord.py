from PyQt5.QtCore import *


class HistoryRecord(QObject):
    read_history_record_signal = pyqtSignal(str)
    historyRecordCountChanged = pyqtSignal(int)

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self._record_count = 0

    def onHistoryRecordCount(self, count):
        self._record_count = count
        self.historyRecordCountChanged.emit(count)

    @pyqtProperty(int, notify=historyRecordCountChanged)
    def historyRecordCount(self):
        return self._record_count

    @pyqtSlot(str)
    def readHistoryRecord(self, func_name: str):
        self.read_history_record_signal.emit(func_name)


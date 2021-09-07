from PyQt5.QtQuick import QQuickView
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtQml, QtQuick
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine
import sys
import time
from uart import Uart
# from BatteryModel import BatteryModel
from battery import BatteryStatus

import threading


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # qmlRegisterType(Uart, 'UartModule', 1, 0, 'UartModule')

    # qmlRegisterType(BatteryModel, 'BatteryModel', 1, 0, 'BatteryModel')
    engine = QtQml.QQmlApplicationEngine()
    uart = Uart()
    engine.rootContext().setContextProperty("uart", uart)

    batteryStatus = BatteryStatus()
    engine.rootContext().setContextProperty("batteryStatus", batteryStatus)
    # battery = BatteryModel()
    battery = batteryStatus.batteryModel
    engine.rootContext().setContextProperty("battery", battery)
    engine.load(QUrl('UI/MainWindow.qml'))

    t = threading.currentThread()
    print(t.getName())

    sys.exit(app.exec_())

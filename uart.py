import sys
import serial
import serial.tools.list_ports
import threading
import queue

from PyQt5.QtCore import *

from rawprotocol import RawProtocol


# 该类型导入到qml中，该类型的对象在qml中实例化
# qmlRegisterType(Uart, 'UartModule', 1, 0, 'UartModule')
class Uart(QObject):
    dataReceived = pyqtSignal(str, arguments=["uartData"])  # 定义信号,qml中的处理函数的参数名为uartData，类型为string
    rawDataReceeved = pyqtSignal(bytes)
    comPortChanged = pyqtSignal(str)
    baudRateChanged = pyqtSignal(str)
    hexModeChanged = pyqtSignal(bool)
    uartError = pyqtSignal(str, arguments=["errorMSG"])

    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.ser = None
        self.module_thread = None
        self.transport = None
        self.protocol = None
        self.data_queue = queue.Queue()
        self.com_port = ''
        self.baud_rate = ''
        self.hex_mode = False
        # install this to hook child thread exception
        threading.excepthook = self.subthread_excepthook

    # 子线程中发生的异常主线程中不能直接通过except语句catch到,
    # 需要安装个hook,该方法貌似python3.8以上的才支持,
    # usb转串口设备被拔出来时会raise一个异常，
    # 当发现串口线拔出时发射信号通知UI, qml中收到该信号弹框
    def subthread_excepthook(self, args):
        # print(f'In excepthook {args=} --- {type(args)}')

        exc_type, exc_value, exc_traceback = sys.exc_info()
        # self.uartError.emit(exc_type.__name__)
        self.uartError.emit('串口错误')

        print('Handling %s exception with message "%s" in %s' % \
              (exc_type.__name__, exc_value, threading.current_thread().name))

    # 定义一个属性，表示选择哪一个串口号,qml中实例化的对象
    # 读属性， 写属性， 属性变化通知
    # 一个python的装饰器实现同一个功能代码比C++看起来简洁得多
    # 为什么这么写，我也不知道，CV过来的
    @pyqtProperty(str, notify=comPortChanged)
    def comPort(self):
        return self.com_port

    # 上面那个东西的写属性方法
    @comPort.setter
    def comPort(self, value):
        self.com_port = value
        self.comPortChanged.emit(value)
        print(value)

    @pyqtProperty(str, notify=baudRateChanged)
    def baudRate(self):
        return self.baud_rate

    @baudRate.setter
    def baudRate(self, value):
        self.baud_rate = value
        self.baudRateChanged.emit(value)
        print(value)

    @pyqtProperty(bool, notify=comPortChanged)
    def hexMode(self):
        return self.hex_mode

    @hexMode.setter
    def hexMode(self, value):
        self.hex_mode = value
        self.hexModeChanged.emit(value)

    # qml中能调用到该方法要加装饰器@pyqtSlot
    # 信号和槽是编入QT的meta的，所以qml中才能找到这个符号
    # 返回值是个list所以result设置为通用变量类型QVariant
    @pyqtSlot(result=QVariant)
    def get_port_list_info(self):
        return [p.device for p in serial.tools.list_ports.comports()]

    @pyqtSlot(result=str)
    def start(self):
        try:
            print('Open ' + self.com_port)
            # CV过来的, 参考 https://github.com/pyserial/pyserial/blob/master/serial/threaded/__init__.py
            self.ser = serial.serial_for_url(self.com_port, baudrate=int(self.baud_rate), timeout=1)
            self.module_thread = serial.threaded.ReaderThread(self.ser, RawProtocol)
            self.module_thread.start()
            self.transport, self.protocol = self.module_thread.connect()
            # 注册串口收到数据时的回调函数
            self.protocol.register_event_listener(self.on_uart_event)
        except Exception as e:
            self.stop()
            self.uartError.emit('uart open fail')
            print(e)

    @pyqtSlot()
    def stop(self):
        if self.module_thread:
            print('Close ' + self.com_port)
            self.module_thread.close()

        self.ser = None
        self.module_thread = None
        self.transport = None
        self.protocol = None

    # Debug UI使用，输入框的数据要发送到串口调用这个函数
    # UI上显示的字符都是unicode的,转为byte再发送
    @pyqtSlot(str)
    def set_text(self, data):
        # print(data)
        # print(data.encode('utf-8'))
        if self.transport:
            if self.hex_mode:
                send_buf = []
                data = data.strip()
                while data != '':
                    try:
                        num = int(data[0:2], 16)
                    except ValueError:
                        self.uartError.emit('发送数据需要是16进制')
                        return
                    send_buf.append(num)
                    data = data[2:].strip()
                self.transport.write(bytes(send_buf))
            else:
                self.transport.write(data.encode('utf-8'))

    # 在start()函数中往串口的read loop thread中注册一个监听,从串口读到数据的时候callback
    # self.protocol.register_event_listener(self.on_uart_event)
    def on_uart_event(self, data):
        # self.data_queue.put(data)
        # if not self.data_queue.empty():
        # print(data)
        self.rawDataReceeved.emit(data)

        if self.hex_mode:
            str_buffer = ''
            for byte in data:
                str_buffer += '{:02X}'.format(byte)
                str_buffer += ' '
            self.dataReceived.emit(str_buffer)
        else:
            self.dataReceived.emit(str(data, encoding='utf-8', errors='ignore'))

    def send(self, data:bytes):
        if self.transport:
            self.transport.write(data)


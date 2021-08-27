import serial
import serial.threaded


# 参考pyserial官方的例子
# https://github.com/pyserial/pyserial/blob/master/examples/at_protocol.py
# https://github.com/pyserial/pyserial/blob/master/serial/threaded/__init__.py
# 比如官方的at_protocol.py,at指令:当收到'+' 开头，结尾为 '\r\n'， 就是一个数据包
# 由于后续是做和单片机通信的，就不像官方的例子一样直接在这里处理了,
# 收到数据后直接把数据丢给观察者，观察者爱咋处理咋处理，这里不管
class RawProtocol(serial.threaded.Protocol):
    def __init__(self):
        self.transport = None
        self.listener_list = []

    def connection_made(self, transport):
        """Store transport"""
        self.transport = transport

    def connection_lost(self, exc):
        """Forget transport"""
        self.transport = None
        self.listener_list = []
        super(RawProtocol, self).connection_lost(exc)

    def data_received(self, data):
        """Buffer received data, call all listener"""
        for listener in self.listener_list:
            listener(data)

    def register_event_listener(self, listener):
        if callable(listener):
            self.listener_list.append(listener)
        else:
            raise TypeError("The listener registered is not a callable")

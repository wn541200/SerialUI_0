import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Controls 2.2 as C2
import QtQuick.Layouts 1.3


Rectangle {
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10

    // 该定时器用于检测是否有串口插拔，后端python的serial模块没找到监听串口插拔的东西
    Timer {
        id: serialPortDetectTimer
        interval: 500; running: true; repeat: true
        onTriggered: {
            var info = uart.get_port_list_info()
            if  (JSON.stringify(serial_port.model) !== JSON.stringify(info)) {
                serial_port.model = info
            }
        }
    }

    C2.GroupBox {
        id: rowBox
        anchors.centerIn: parent
        width: parent.width / 3
        Layout.fillWidth: true
        background : Rectangle {color: "LightSlateGray"}


        ColumnLayout {
            anchors.fill: parent
            spacing:  20
            RowLayout {
                Layout.fillWidth: true
                Layout.topMargin:  20
                Layout.leftMargin:  20
                Layout.rightMargin:  20
                spacing:  20
                Label {
                    text: "串口号:     "
                }
                // 串口号选择下拉框
                // 把选择的串口号传到后端的uart对象
                // 在start()的时候就不用指定打开哪一个串口
                ComboBox {
                    id: serial_port
                    Layout.fillWidth: true
                    height: 30
                    model : uart.get_port_list_info()

                    onCurrentTextChanged: {
                        if (serial_port.count) {
                            serial_en_switch.checkable = true
                            uart.comPort = currentText
                        }
                        else {
                            serial_en_switch.checkable = false
                        }
                    }

                }

            }

            RowLayout {
                Layout.fillWidth: true
                Layout.leftMargin:  20
                Layout.rightMargin:  20
                spacing:  20
                Label {
                    text: "波特率:     "
                }

                // 波特率选择下拉框
                // 把选择的波特率传到后端的uart对象
                // 在start()的时候就不用指定波特率了
                ComboBox {
                    id: baud_rate
                    Layout.fillWidth: true
                    height: 30
                    model : ['9600', '115200', '57600']

                    onActivated: {
                        uart.baudRate = currentText
                    }

                    Component.onCompleted: {
                        uart.baudRate = currentText
                    }

                }
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.leftMargin:  20
                Layout.rightMargin:  20
                spacing:  20
                Label {
                    text: "通讯地址:   "
                }


                ComboBox {

                    Layout.fillWidth: true
                    height: 30
                    model : ['0x7e', '0x7d']

                }
            }

            RowLayout {
                Layout.fillWidth: true
                Layout.leftMargin:  20
                Layout.rightMargin:  20
                spacing:  20
                Label {
                    text: "监控间隔:(s)"
                }


                ComboBox {

                    Layout.fillWidth: true
                    height: 30
                    model : ['1', '2', '3', '4', '5']

                }
            }

            C2.Switch {
                id: serial_en_switch
                Layout.alignment: Qt.AlignHCenter
                text: qsTr("串口开关")
                checkable: false
                checked: false
                onCheckedChanged: {
                    // 串口运行时把串口选择和波特率的控件变为不可用
                    // 打开串口进行通信,后端使用python的serial模块，
                    // 自带threading,线程安全，非常省事
                    if (checked) {
                        serial_port.enabled = false
                        baud_rate.enabled = false
                        serialPortDetectTimer.running = false
                        uart.start()
                    }
                    else {
                        serial_port.enabled = true
                        baud_rate.enabled = true
                        serialPortDetectTimer.running = true
                        uart.stop()
                    }
                }
            }
        }
    }
}


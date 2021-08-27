import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Dialogs 1.2
import UartModule 1.0

Rectangle {
    id: mainwindow
    anchors.fill: parent
    anchors.topMargin: 10


    UartModule {
        id: uart
        // 信号处理函数:串口接收到数据则追加到显示区域
        onDataReceived: {
            // 若使用append每次都会新起一行，这里用insert
            txt.insert(txt.length, uartData)
        }

        // 信号处理函数：后台出错抛出异常时弹框通知用户
        onUartError: {
            // 串口通信过程中如usb转串口被拔出，把串口开关置为关闭状态
            // 并重新获取可用的串口
            if (errorMSG === '串口错误') {
                serial_en_switch.checked = false
                serial_port.model = uart.get_port_list_info()
            }
            // 其他错误不需要关闭串口，直接显示错误信息
            errorMessage.text = errorMSG
            errorMessage.visible = true
        }
    }

    // 提示用户出错的对话框，出错时再显示
    MessageDialog {
        id: errorMessage
        title: qsTr("错误")
        text: qsTr("请检查串口是否失去连接")
        icon: StandardIcon.Warning
        visible: false
    }

    // 该定时器用于检测是否有串口插拔，后端python的serial模块没找到监听串口插拔的东西
    Timer {
        id: serialPortDetectTimer
        interval: 500; running: true; repeat: true
        onTriggered: serial_port.model = uart.get_port_list_info()
    }

    // 串口接受到数据后的要在TextArea控件上显示，
    // 由于需要滚动条外面套了个Flickable，
    // 代码是从QT帮助文档上CV过来的
    Flickable {
        id: view
        flickableDirection: Flickable.VerticalFlick
        width: mainwindow.width -2
        height: mainwindow.height - 120

        TextArea.flickable: TextArea {
            id: txt
            width: mainwindow.width -2
            height: mainwindow.height - 60
            textFormat:TextEdit.AutoText
            wrapMode: TextEdit.Wrap //换行
            selectByMouse: true
            selectByKeyboard: true
            readOnly: true
            persistentSelection: true
            // Different styles have different padding and background
            // decorations, but since this editor is almost taking up the
            // entire window, we don't need them.
            leftPadding: 6
            rightPadding: 6
            topPadding: 0
            bottomPadding: 0
            background: Rectangle {
                color: "lightgray"
            }

            // 添加右键菜单:全选 复制 清空
            // 重叠区域的鼠标事件穿透还是有很多疑惑
            MouseArea {
                anchors.fill: parent
                propagateComposedEvents: true
                acceptedButtons: Qt.RightButton
                onClicked: {
                    if (mouse.button == Qt.RightButton) {
                        contentMenu.x = mouseX
                        contentMenu.y = mouseY
                        contentMenu.open()
                    }
                    mouse.accepted = false
                }
            }
            Menu {
                id: contentMenu
                MenuItem {
                    text: "全选"
                    onTriggered: txt.selectAll()
                }

                MenuItem {
                    text: "复制"
                    onTriggered: txt.copy()
                }

                MenuItem {
                    text: "清空"
                    onTriggered: txt.clear()
                }
            }

            // 超过显示区域时，调整滚动条的位置
            onContentHeightChanged: {
                if (view.contentHeight > view.height) {
                    txtScroll.position = (view.contentHeight-view.height)/view.contentHeight
                }
            }

        }

        // 滚动条控件
        ScrollBar.vertical: ScrollBar {
            id: txtScroll
            snapMode: ScrollBar.SnapAlways
            stepSize : 0.1
            policy: ScrollBar.AlwaysOn
        }
    }

    // 通过串口发送的数据在这个控件输入
    TextField {
        id: id_input
        anchors.top : view.bottom
        anchors.margins: 20
        width: parent.width
        selectByMouse: true
        placeholderText: qsTr("数据输入区")

        // Hex按钮被选中时,用正则表达式把输入字符格式限制为以下几种(均忽略大小写):
        // 0x可加可不加，用英文逗号或空格隔离开
        // 1. ff ff
        // 2. ff,ff
        // 3. 0xff 0xff
        // 4. 0xff,0xff
        RegExpValidator {
            id: regHexInputLimit
            regExp : /((0x)?[0-9a-f][0-9a-f][\s|,]){100}/i
        }

        // ASCII按钮被选中时去除输入框的输入限制
        RegExpValidator {
            id: regNoInputLimit
        }
    }

    Row {
        anchors.top: id_input.bottom
        anchors.left: mainwindow.left
        anchors.margins: 20
        spacing: 10

        Switch {
            id: serial_en_switch
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

        // 串口号选择下拉框
        // 把选择的串口号传到后端的uart对象
        // 在start()的时候就不用指定打开哪一个串口
        ComboBox {
            id: serial_port
            width: 150
            height: 30
            model : uart.get_port_list_info()

            onDisplayTextChanged: {
                if (serial_port.count) {
                    serial_en_switch.checkable = true
                    uart.comPort = currentText
                }
                else {
                    serial_en_switch.checkable = false
                }
            }

        }

        // 波特率选择下拉框
        // 把选择的波特率传到后端的uart对象
        // 在start()的时候就不用指定波特率了
        ComboBox {
            id: baud_rate
            width: 150
            height: 30
            model : ['115200', '9600']

            onActivated: {
                uart.baudRate = currentText
            }

            Component.onCompleted: {
                uart.baudRate = currentText
            }

        }

        Button {
            width: 100
            height: 30
            text: qsTr("发送数据")
            enabled: {
                // 串口没有打开并且要发送数据的输入控件没东西，该按钮不可点击
                if (serial_en_switch.checked && id_input.length)
                    return true
                else
                    return false
            }
            onClicked: {
                uart.set_text(id_input.displayText)
            }
        }

        // 选择ASCII模式时解除输入限制
        RadioButton {
            checked: true
            text: qsTr("ASCII")
            onCheckedChanged: {
                uart.hexMode = false
                id_input.validator = regNoInputLimit
            }
        }

        // 选择Hex模式时输入限制为16进制格式
        RadioButton {
            id: hexModeButton
            text: qsTr("Hex")
            onCheckedChanged: {
                uart.hexMode = true
                id_input.validator = regHexInputLimit
            }
        }
    }
}
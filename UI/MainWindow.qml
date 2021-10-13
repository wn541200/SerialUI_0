import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.2
import QtQuick.Controls 2.2 as Controls2
import QtQuick.Controls.Styles 1.2
import QtQuick.Particles 2.0

Controls2.ApplicationWindow {
    id: window
    minimumWidth: 1280
    minimumHeight: 800
    width: 1280
    height: 800
    visible: true
    title: qsTr("工具")

    TabView {
        width: window.width
        height: window.height
        Layout.row: 6
        Layout.columnSpan: 3
        Layout.fillWidth: true
        implicitHeight: 30
        Tab {
            title: "通讯设置"
            source: "UartSettings.qml"
        }

        Tab {
            title: "实时监控"
            source: "MonitorTab.qml"
        }

        Tab {
            title: "信息记录"
            source: "InforRecord.qml"
        }
		
		Tab {
            title: "历史记录"
            source: "HistoryRecord.qml"
        }
		
		Tab {
            title: "系统设置"
            source: "SystemSettingTab.qml"
			visible: false
        }
		
		Tab {
            title: "参数设置"
            source: "SettingsTab.qml"
        }

        Tab {
            title: "调试"
            source: "UartDebug.qml"
        }
        style: tabViewStyle
    }

    Component {
        id: tabViewStyle
        TabViewStyle {
            tabOverlap: 16
            frameOverlap: 4
            tabsMovable: true

            frame: Rectangle {
                gradient: Gradient {
                    GradientStop { color: "#e5e5e5" ; position: 0 }
                    GradientStop { color: "#e0e0e0" ; position: 1 }
                }
                border.color: "#898989"
                Rectangle { anchors.fill: parent ; anchors.margins: 1 ; border.color: "white" ; color: "transparent" }
            }
            tab: Item {
                property int totalOverlap: tabOverlap * (control.count - 1)
                implicitWidth: Math.min ((styleData.availableWidth + totalOverlap)/control.count - 4, image.sourceSize.width)
                implicitHeight: image.sourceSize.height
                BorderImage {
                    id: image
                    anchors.fill: parent
                    source: styleData.selected ? "images/tab_selected.png" : "images/tab.png"
                    border.left: 30
                    smooth: false
                    border.right: 30
                }
                Text {
                    text: styleData.title
                    anchors.centerIn: parent
                }
            }
            leftCorner: Item { implicitWidth: 12 }
        }
    }

    footer: Rectangle {
        width: window.width
        height: 30
        color: "lightgray"

        Text {
			anchors.centerIn: parent
            text: "型号：" + systemSettings.projectId + "   " + "序列号：" + systemSettings.bmsSN + "   " + "软件版本号：" + systemSettings.swVersion + "   " + "硬件版本号：" + systemSettings.hwVersion + "   "
        }
    }
}

import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.3
// import BatteryModel 1.0

Rectangle {
    id: root
    anchors.fill: parent
    color: "#e5e5e5"
    anchors.topMargin: 10


    GridView {
        id: gridView
        width: parent.width
        height: parent.height - 80
        anchors.leftMargin: 15
        anchors.rightMargin: 15
        cellWidth: root.width / 4.5
        cellHeight: root.height / 2.3

        clip: true

        model: batterySettingsModel
        delegate: Rectangle{
            id: settingItem
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"

            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: name

                CheckBox {
                    id:checkBox
                    x: 12
                    y: 7
                    text: qsTr("使能")
                    checked: itemEnabled ? true : false
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(V)")
                }

                TextField {
                    id: protect_threshold_input
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                    text: String(protect_threshold)
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(V)")
                }

                TextField {
                    id: protect_hysteresis_input
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
                    text: String(protect_hysteresis)
                }

                Label {
                    x: 12
                    y: 107
                    width: 106
                    height: 15
                    text: qsTr("保护延时(ms)")
                    transformOrigin: Item.Center
                }

                TextField {
                    id: protect_threshold_delay_input
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                    text: String(protect_threshold_delay)
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    id: protect_hysteresis_delay_input
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                    text: String(protect_hysteresis_delay)
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(V)")
                }

                TextField {
                    id: alarm_threshold_input
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                    text: String(alarm_threshold)
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    id: alarm_threshold_delay_input
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                    text: String(alarm_threshold_delay)
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                    onClicked: {
                        batterySettingsModel.readItemFromMCU(index)
                    }
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                    onClicked: {
                        batterySettingsModel.setItem(
                                        index,
                                        checkBox.checked,
                                        Number(protect_threshold_input.text),
                                        Number(protect_hysteresis_input.text),
                                        Number(protect_threshold_delay_input.text),
                                        Number(protect_hysteresis_delay_input.text),
                                        Number(alarm_threshold_input.text),
                                        Number(alarm_threshold_delay_input.text)
                                    )
                    }
                }
            }
        }

    }



    Button {
        id: firstPageButton
        anchors.top: gridView.bottom
        text: qsTr("第一页")
    }

    Button {
        anchors.top: gridView.bottom
        anchors.left: firstPageButton.right
        text: qsTr("第二页")
    }

}



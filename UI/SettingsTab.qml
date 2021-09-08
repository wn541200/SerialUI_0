import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.3
// import BatteryModel 1.0

Rectangle {
    id: root
    width: 1280
    height: 800
    anchors.fill: parent
    color: "#e5e5e5"
    anchors.topMargin: 10

    Grid {
        anchors.fill: parent
        anchors.leftMargin: 15
        anchors.rightMargin: 15
        spacing: (root.width - 4 * settingItem.width) / 4
        rows: 2
        columns: 4


        Rectangle{
            id: settingItem
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"

            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("单体过压")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(V)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(V)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(V)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("单体欠压")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(V)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(V)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(V)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("总体过压")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(V)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(V)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(V)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("总体欠压")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(V)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(V)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(V)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }


        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"

            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("放电过流")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")

                    Label {
                        x: -140
                        y: -14
                        width: 106
                        height: 15
                        text: qsTr("保护(A)")
                    }
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(A)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(A)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("充电过流")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(A)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(A)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(A)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("SOC过高")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(%)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(%)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(%)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

        Rectangle{
            width: root.width / 4.5
            height: root.height / 2.3
            radius: 10
            border.width: 1
            border.color:"black"
            GroupBox {
                anchors.fill: parent
                anchors.margins: 5
                title: qsTr("SOC过低")

                CheckBox {
                    x: 12
                    y: 7
                    text: qsTr("使能")
                }

                Label {
                    x: 12
                    y: 46
                    width: 106
                    height: 15
                    text: qsTr("保护(%)")
                }

                TextField {
                    x: 142
                    y: 43
                    width: 113
                    height: 20
                    placeholderText: qsTr("1")
                }

                Label {
                    x: 12
                    y: 76
                    width: 106
                    height: 15
                    text: qsTr("保护恢复(%)")
                }

                TextField {
                    x: 142
                    y: 73
                    width: 113
                    height: 20
                    placeholderText: qsTr("2")
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
                    x: 142
                    y: 104
                    width: 113
                    height: 20
                    placeholderText: qsTr("3")
                }

                Label {
                    x: 12
                    y: 138
                    width: 106
                    height: 15
                    text: qsTr("保护恢复延时(ms)")
                }

                TextField {
                    x: 142
                    y: 135
                    width: 113
                    height: 20
                    placeholderText: qsTr("4")
                }

                Label {
                    x: 12
                    y: 173
                    width: 106
                    height: 15
                    text: qsTr("报警(%)")
                }

                TextField {
                    x: 142
                    y: 170
                    width: 113
                    height: 20
                    placeholderText: qsTr("5")
                }

                Label {
                    x: 12
                    y: 205
                    text: qsTr("报警延时(ms)")
                }

                TextField {
                    x: 142
                    y: 203
                    width: 113
                    height: 20
                    placeholderText: qsTr("6")
                }

                Button {
                    x: 12
                    y: 268
                    text: qsTr("读")
                }

                Button {
                    x: 161
                    y: 268
                    text: qsTr("写")
                }
            }
        }

    }


}

/*##^##
Designer {
    D{i:17;invisible:true}D{i:21;invisible:true}D{i:19;invisible:true}D{i:36;invisible:true}
D{i:53;invisible:true}D{i:1;anchors_height:400;anchors_width:400;anchors_x:73;anchors_y:40}
}
##^##*/

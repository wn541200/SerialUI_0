import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.3

Rectangle {
    anchors.fill: parent
    color: "#e5e5e5"
    GroupBox {
    id: rowBox
    anchors.centerIn: parent
    width: parent.width / 2
    title: "串口设置"
    Layout.fillWidth: true

    RowLayout {
        id: rowLayout
        anchors.fill: parent
        TextField {
            placeholderText: "This wants to grow horizontally"
            Layout.fillWidth: true
        }
        Button {
            text: "Button"
        }
    }
}

}
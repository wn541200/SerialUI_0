import QtQuick 2.2
import QtQuick.Controls 1.2


Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10
	
	Rectangle {
		id: textArea
		anchors.top: parent.top
		anchors.left: parent.left
		anchors.right: parent.right
		anchors.topMargin: 20
		anchors.leftMargin: 20
		anchors.rightMargin: 20
		height: parent.height - 120
		width: parent.width
		
		color: "white"
		
		TableView {
			anchors.fill: parent
			TableViewColumn {
				role: "time"
				title: "时间"
				width: 100
			}
			TableViewColumn {
				role: "voltage"
				title: "电压"
				width: 100
			}
			TableViewColumn {
				role: "current"
				title: "电流"
				width: 100
			}
			TableViewColumn {
				role: "soc"
				title: "soc"
				width: 100
			}
			TableViewColumn {
				role: "soh"
				title: "soh"
				width: 100
			}
			model: batteryRecordModel
		}
		
	}
	
	Button {
		id: displayButton
		anchors.top: textArea.bottom
		anchors.left: textArea.left
		anchors.topMargin: 20
		anchors.leftMargin: 20
		width: root.width / 4
		text: "显示"
		
	}
	
	Button {
		id: clearButton
		anchors.top: textArea.bottom
		anchors.left: displayButton.right
		anchors.topMargin: 20
		anchors.leftMargin: 20
		width: root.width / 4
		text: "清空"
		
		onClicked: {
			batteryStatus.clearAllBatteryRecord()
		}
	}
	
	Button {
		id: exportButton
		anchors.top: textArea.bottom
		anchors.left: clearButton.right
		anchors.topMargin: 20
		anchors.leftMargin: 20
		width: root.width / 4
		text: "导出数据"
	}
}
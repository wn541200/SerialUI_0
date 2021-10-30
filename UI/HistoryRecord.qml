import QtQuick 2.2
import QtQuick.Controls 1.2


Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10
	
	TextArea {
		id: textArea
		anchors.top: parent.top
		anchors.left: parent.left
		anchors.right: parent.right
		anchors.topMargin: 20
		anchors.leftMargin: 20
		anchors.rightMargin: 20
		height: parent.height - 120
		
		readOnly: true
	}
	
	Button {
		id: getButton
		anchors.top: textArea.bottom
		anchors.left: textArea.left
		anchors.topMargin: 20
		anchors.leftMargin: 20
		text: "获取事件总数"
		onClicked: {
		    historyRecord.readHistoryRecord("history_count")
		}
	}
	
	Rectangle {
		id: seperateItem
		anchors.left: getButton.right
		anchors.verticalCenter: getButton.verticalCenter
		width: 25
		height: 5
		radius: 3
		rotation: 90
		color: "black"
		gradient: Gradient {
			
            GradientStop { position: 0.0; color: "#f5f5f5" }
            GradientStop { position: 1.0; color: "#b5b5b5" }
        }
	}
	
	Label {
		id: countLabel
		anchors.left: seperateItem.right
		anchors.verticalCenter: seperateItem.verticalCenter
		text: "事件总数:" + historyRecord.historyRecordCount
	}
	
	Button {
		id: clearButton
		anchors.left: countLabel.right
		anchors.verticalCenter: countLabel.verticalCenter
		anchors.leftMargin: 80
		text: "清空"
	}
	
	Button {
		id: exportButton
		anchors.left: clearButton.right
		anchors.verticalCenter: clearButton.verticalCenter
		anchors.leftMargin: 10
		text: "导出数据"
	}
	
	Row {
		anchors.left: exportButton.right
		anchors.verticalCenter: exportButton.verticalCenter
		anchors.leftMargin: 80
		spacing: 5
		
		Label {
			anchors.verticalCenter: parent.verticalCenter
			text: "读取范围:"
		}
		
		Rectangle {
			anchors.verticalCenter: parent.verticalCenter
			width: 30
			height: 20
			color: "white"
			radius: 2
			border.width: 1
			border.color: "#d5d5d5"
			TextInput {
				anchors.fill: parent
				verticalAlignment: TextInput.AlignVCenter
				maximumLength: 4
			}
		}
		
		Label {
			anchors.verticalCenter: parent.verticalCenter
			text: "-"
		}
		
		Rectangle {
			anchors.verticalCenter: parent.verticalCenter
			width: 30
			height: 20
			color: "white"
			radius: 2
			border.width: 1
			border.color: "#d5d5d5"
			TextInput {
				anchors.fill: parent
				verticalAlignment: TextInput.AlignVCenter
				maximumLength: 4
			}
		}
		
		Button {
			anchors.verticalCenter: parent.verticalCenter
			text: "读取指定范围"
		}
		
		Button {
			anchors.verticalCenter: parent.verticalCenter
			text: "读取全部"
			onClicked: {
			    historyRecord.readHistoryRecord("history_record")
			}
		}
	}
}
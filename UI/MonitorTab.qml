import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.3

Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	
	GroupBox {
		id: baseInfoGroupBox
		anchors.top: parent.top
		anchors.topMargin: 20
		anchors.leftMargin: 20
		anchors.rightMargin: 20
		width: parent.width
		height: 50
		title: "基本信息"
		
		ListView {
			anchors.fill: parent
			orientation: ListView.Horizontal
			spacing: 50
			model: ContactModel {}
			
			delegate: Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: name + ": " + number
					Component.onCompleted: {
						console.log(index)
					}
				}
			}
		}
	}
	
	GridLayout{
		id: gridLayout
		property int columnRatio: 4

		anchors.top: baseInfoGroupBox.bottom
		anchors.left: baseInfoGroupBox.left
		anchors.right: baseInfoGroupBox.right
		anchors.bottom: root.bottom
		anchors.topMargin: 10
		rows: 5
		columns: 6
		
		Rectangle{
			Layout.columnSpan: 5
			Layout.rowSpan: 2
			Layout.fillHeight: true
			Layout.fillWidth: true
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "温度(°c)"
			}
		}
		
		Rectangle{
			Layout.fillHeight: true
			width: root.width / gridLayout.columnRatio
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "系统状态"
			}
		}
		
		Rectangle{
			Layout.fillHeight: true
			width: root.width / gridLayout.columnRatio
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "报警状态"
			}
		}
		
		Rectangle{
			Layout.columnSpan: 5
			Layout.rowSpan: 3
			Layout.fillHeight: true
			Layout.fillWidth: true
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "单体电压(mV)"
			}
		}
		
		Rectangle{
			Layout.fillHeight: true
			width: root.width / gridLayout.columnRatio
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "保护状态"
			}
		}
		
		Rectangle{
			Layout.fillHeight: true
			width: root.width / gridLayout.columnRatio
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "故障状态"
			}
		}
		
		Rectangle{
			Layout.fillHeight: true
			width: root.width / gridLayout.columnRatio
			radius: 10
			border.width: 1
			border.color:"black"
			
			GroupBox {
				anchors.fill: parent
				anchors.topMargin: 5
				anchors.bottomMargin: 5
				anchors.leftMargin: 5
				anchors.rightMargin: 5
				title: "控制"
			}
		}

	}
}
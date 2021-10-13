import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.2


Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10

	Timer {
        id: sendTimer
        interval: 1000; running: false; repeat: true
        onTriggered: {
			batteryStatus.recordOneBatteryItem()
        }
    }
	
	Connections{
            target: batteryRecordModel

            // 信号处理函数：保存文件失败时提示
            function onErrorMessage(errorMSG) {
                errorMessage.text = errorMSG
                errorMessage.visible = true
            }
     }

    // 提示用户出错的对话框，出错时再显示
    MessageDialog {
        id: errorMessage
        title: qsTr("错误")
        icon: StandardIcon.Warning
        visible: false
    }

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

		Connections{
			target: batteryRecordModel
			onRoleNamesChanged: {
				console.log(count)
				console.log(tabelView.columnCount)
				var roles = batteryRecordModel.getRoleNames()
				console.log(roles)
				var columnCount = tabelView.columnCount
				for (var i=0; i<(count-columnCount); i++) {
					var column = tabelView.addColumn( Qt.createQmlObject(
						"import QtQuick 2.2;import QtQuick.Controls 1.2;TableViewColumn {width: 100}",
						this) )
					column.role = roles[i+16]
					column.title = roles[i+16]
				}
			}

			Component.onCompleted: {

			}
		}

		TableView {
			id: tabelView
			anchors.fill: parent
			TableViewColumn {
				role: "time"
				title: "时间"
				width: 100
			}
			TableViewColumn {
				role: "voltage"
				title: "总电压"
				width: 100
			}
			TableViewColumn {
				role: "current"
				title: "总电流"
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
			TableViewColumn {
				role: "maxCellVoltage"
				title: "最高电压"
				width: 100
			}
			TableViewColumn {
				role: "maxCellVoltageNr"
				title: "最高电压序号"
				width: 100
			}
			TableViewColumn {
				role: "minCellVoltage"
				title: "最低电压"
				width: 100
			}
			TableViewColumn {
				role: "minCellVoltageNr"
				title: "最低电压序号"
				width: 100
			}
			TableViewColumn {
				role: "maxCellsVoltageDiff"
				title: "最大压差"
				width: 100
			}
			TableViewColumn {
				role: "maxCellTemperature"
				title: "最高温度"
				width: 100
			}
			TableViewColumn {
				role: "maxCellTemperatureNr"
				title: "最高温度序号"
				width: 100
			}
			TableViewColumn {
				role: "minCellTemperature"
				title: "最低温度"
				width: 100
			}
			TableViewColumn {
				role: "minCellTemperatureNr"
				title: "最低温度序号"
				width: 100
			}
			TableViewColumn {
				role: "nrThermals"
				title: "温度传感器数量"
				width: 100
			}
			TableViewColumn {
				role: "nrCells"
				title: "电芯数量"
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
		text: "开始记录"
		onClicked: {
			if (sendTimer.running) {
				sendTimer.running = false
				displayButton.text = "开始记录"
			}
			else {
				sendTimer.running = true
				displayButton.text = "停止记录"
			}
		}
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
		onClicked: {
			saveFileDialog.visible = true
		}
	}

	FileDialog {
		id: saveFileDialog
		title: "数据另存为"
		folder: shortcuts.desktop
		selectExisting: false
		nameFilters: ["CSV files (*.csv)"]
		onAccepted: {
			batteryStatus.saveRecordToFile(saveFileDialog.fileUrl)
		}
	}
}
import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.3
// import BatteryModel 1.0

Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10
	
	GroupBox {
		id: baseInfoGroupBox
		anchors.top: parent.top
		anchors.topMargin: 20
		anchors.leftMargin: 20
		anchors.rightMargin: 20
		width: parent.width
		height: 50
		title: "基本信息"
		
		Row {
			spacing: 50
			
			Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: "电压: " + batteryStatus.voltage +"V"
				}
			}
			
			Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: "电流: " + batteryStatus.current +"A"
				}
			}
			
			Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: "SOC: " + batteryStatus.soc +"%"
				}
			}
			
			Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: "SOH: " + batteryStatus.soh +"%"
				}
			}
			
			Rectangle {
				width: baseInfoGroupBox.width / 6.2
				height: 30
				color: "#e5e5e5"
				Text {
					anchors.centerIn: parent
					font.pointSize: 12
					text: "状态:" + batteryStatus.status
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
				anchors.margins: 5
				clip: true
				title: "温度(°c)"

				Rectangle {
				    width: parent.width
				    height: parent.height / 10
				    color: "lightgray"
				    radius: 3

				    Rectangle {
				        id: maxTemperatureRectangle
				        width: parent.width / 2
				        height: parent.height
				        color: "lightgray"
				        Text {
                            anchors.centerIn: parent
                            font.pointSize: 12
                            text: "最高温度(" + batteryStatus.maxCellTemperatureNr + "):" + batteryStatus.maxCellTemperature
                        }
				    }

				    Rectangle {
				        id: minTemperatureRectangle
				        anchors.left: maxTemperatureRectangle.right
				        width: parent.width / 2
				        height: parent.height
				        color: "lightgray"
				        Text {
                            anchors.centerIn: parent
                            font.pointSize: 12
                            text: "最低温度(" + batteryStatus.minCellTemperatureNr + "):" + batteryStatus.minCellTemperature
                        }
				    }
				}

				GridView {
                    id: temperatureView
                    anchors.fill: parent
                    anchors.topMargin: parent.height / 8
                    cellWidth: 120
                    cellHeight: 40

                    delegate: Rectangle {
                        width: temperatureView.cellWidth
                        height: temperatureView.cellHeight
                        Label {
                            id: temp_label
                            width: 40
                            text: "温度" + index
                        }

                        Label {
                            anchors.left: temp_label.right
                            anchors.leftMargin: 20
                            text: number
                            color: "blue"
                        }
                    }
                    model: batteryThermalModel

                }
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
				anchors.margins: 5
				title: "系统状态"
				
				Column {
					anchors.fill: parent
					anchors.topMargin: 20
					anchors.leftMargin: 5
					spacing: 20
					
					Row {
						spacing: 5
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "放电MOS"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "充电MOS"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "预充电MOS"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "加热"
						}
						
					}
					
					Row {
						spacing: 5
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "GPRS"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "充电器"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "负载"
						}
						
						Rectangle {
							width:20
							height:10
							color: "green"
						}
						Label {
							width:50
							height: 10
							text: "预留"
						}
						
					}
					
				}
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
				anchors.margins: 5
				title: "报警状态"
				
				TextArea {
					id: alarmText
                    anchors.fill: parent
					wrapMode: TextEdit.Wrap
					selectByMouse: true
					selectByKeyboard: true
					readOnly: true
					
					MouseArea {
						anchors.fill: parent
						propagateComposedEvents: true
						acceptedButtons: Qt.RightButton
						onClicked: {
							if (mouse.button == Qt.RightButton) {
								alarmContentMenu.popup()
							}
							mouse.accepted = false
						}
					}
					
					Menu {
						id: alarmContentMenu
						MenuItem {
							text: "全选"
							onTriggered: alarmText.selectAll()
						}

						MenuItem {
							text: "复制"
							onTriggered: alarmText.copy()
						}
					}

                }
				
				
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
				anchors.margins: 5
				title: "单体电压(mV)"
				
				Rectangle {
				    width: parent.width
				    height: parent.height / 10
				    color: "lightgray"
				    radius: 3

				    Rectangle {
				        id: maxCellVoltageRectangle
				        width: parent.width / 3
				        height: parent.height
				        color: "lightgray"
				        Text {
                            anchors.centerIn: parent
                            font.pointSize: 12
                            text: "最高电压(" + batteryStatus.maxCellVoltageNr + "):" + batteryStatus.maxCellVoltage + "V"
                        }
				    }

				    Rectangle {
				        id: minCellVoltageRectangle
				        anchors.left: maxCellVoltageRectangle.right
				        width: parent.width / 3
				        height: parent.height
				        color: "lightgray"
				        Text {
                            anchors.centerIn: parent
                            font.pointSize: 12
                            text: "最低电压(" + batteryStatus.minCellVoltageNr + "):" + batteryStatus.minCellVoltage + "V"
                        }
				    }
					
					Rectangle {
				        anchors.left: minCellVoltageRectangle.right
				        width: parent.width / 3
				        height: parent.height
				        color: "lightgray"
				        Text {
                            anchors.centerIn: parent
                            font.pointSize: 12
                            text: "最大压差:" + batteryStatus.maxCellsVoltageDiff + "V"
                        }
				    }
				
				}
				
				GridView {
                    id: cellsView
                    anchors.fill: parent
                    anchors.topMargin: parent.height / 4
                    cellWidth: 120
                    cellHeight: 40

                    delegate: Rectangle {
                        width: cellsView.cellWidth
                        height: cellsView.cellHeight
                        Label {
                            id: temp_label
                            width: 40
                            text: "电芯" + index
                        }

                        Label {
                            anchors.left: temp_label.right
                            anchors.leftMargin: 20
                            text: number
                            color: "blue"
                        }
                    }
                    model: batteryCellsVoltageModel

                }
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
				anchors.margins: 5
				title: "保护状态"
				
				TextArea {
					id: protectText
                    anchors.fill: parent
					wrapMode: TextEdit.Wrap
					selectByMouse: true
					selectByKeyboard: true
					readOnly: true
					
					MouseArea {
						anchors.fill: parent
						propagateComposedEvents: true
						acceptedButtons: Qt.RightButton
						onClicked: {
							if (mouse.button == Qt.RightButton) {
								protectContentMenu.popup()
							}
							mouse.accepted = false
						}
					}
					
					Menu {
						id: protectContentMenu
						MenuItem {
							text: "全选"
							onTriggered: protectText.selectAll()
						}

						MenuItem {
							text: "复制"
							onTriggered: protectText.copy()
						}
					}
                }
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
				anchors.margins: 5
				title: "故障状态"
				
				TextArea {
					id: defectText
                    anchors.fill: parent
					wrapMode: TextEdit.Wrap
					selectByMouse: true
					selectByKeyboard: true
					readOnly: true
					
					MouseArea {
						anchors.fill: parent
						propagateComposedEvents: true
						acceptedButtons: Qt.RightButton
						onClicked: {
							if (mouse.button == Qt.RightButton) {
								defectContentMenu.popup()
							}
							mouse.accepted = false
						}
					}
					
					Menu {
						id: defectContentMenu
						MenuItem {
							text: "全选"
							onTriggered: defectText.selectAll()
						}

						MenuItem {
							text: "复制"
							onTriggered: defectText.copy()
						}
					}
                }
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
				anchors.margins: 5
				title: "控制"
				
				Label {
                    id: label
                    x: 9
                    y: 19
                    text: qsTr("放电MOS")
                }

                Button {
                    id: button
                    x: 57
                    y: 14
                    text: qsTr("闭合")
                }

                Label {
                    id: label1
                    x: 160
                    y: 19
                    text: qsTr("休眠")
                }

                Button {
                    id: button1
                    x: 205
                    y: 14
                    text: qsTr("开")
                }

                Label {
                    id: label2
                    x: 9
                    y: 66
                    text: qsTr("充电MOS")
                }

                Button {
                    id: button2
                    x: 57
                    y: 61
                    text: qsTr("闭合")
                }

                Label {
                    id: label3
                    x: 160
                    y: 67
                    text: qsTr("复位")
                }

                Button {
                    id: button3
                    x: 205
                    y: 61
                    text: qsTr("开")
                    onClicked: {
                        batteryStatus.readBattery("battery_status")
                    }
                }
			}
		}

	}
}
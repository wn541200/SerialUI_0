import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Controls 1.2 as C12
import QtQuick.Controls 1.4 as C14

Rectangle {
	id: root
    anchors.fill: parent
    color: "#e5e5e5"
	anchors.topMargin: 10
	
	Grid{
		anchors.centerIn: parent
		spacing: 10
		columns: 2
	
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "产品设置"
				
				Label {
                    id: productLabel
                    width: 60
					height: productReadButton.height
                    text: "项目编号"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: productRectangle
					anchors.left: productLabel.right
					width: 160
					height: productReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: productIDTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
						text: systemSettings.projectId
					}
				}
				
				C12.Button {
                    id: productReadButton
					anchors.left: productRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
						systemSettings.readSystemSetting("projectId")
                    }
                }
				
				C12.Button {
                    id: productWriteButton
					anchors.left: productReadButton.right
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("projectId", productIDTextInput.text)
                    }
                }
				
				Label {
                    id: bmsLabel
                    width: 60
					height: bmsReadButton.height
					anchors.top: productLabel.bottom
					anchors.topMargin: 5
                    text: "BMS型号"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: bmsRectangle
					anchors.left: bmsLabel.right
					anchors.top: productLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: bmsReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: bmsIDTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
						text: systemSettings.bmsId
					}
				}
				
				C12.Button {
                    id: bmsReadButton
					anchors.left: bmsRectangle.right
					anchors.top: productLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
						systemSettings.readSystemSetting("bmsId")
                    }
                }
				
				C12.Button {
                    id: bmsWriteButton
					anchors.left: productReadButton.right
					anchors.top: productLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("bmsId", bmsIDTextInput.text)
                    }
                }
				
				Label {
                    id: snLabel
                    width: 60
					height: snReadButton.height
					anchors.top: bmsLabel.bottom
					anchors.topMargin: 5
                    text: "序列号"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: snRectangle
					anchors.left: snLabel.right
					anchors.top: bmsLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: snReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: snTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
						text: systemSettings.bmsSN
					}
				}
				
				C12.Button {
                    id: snReadButton
					anchors.left: snRectangle.right
					anchors.top: bmsLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
						systemSettings.readSystemSetting("bmsSN")
                    }
                }
				
				C12.Button {
                    id: snWriteButton
					anchors.left: snReadButton.right
                    anchors.top: bmsLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("bmsSN", snTextInput.text)
                    }
                }
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "电池设置"
				
				Label {
                    id: batteryLabel
                    width: 60
					height: batteryReadButton.height
                    text: "电芯数量"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: batteryRectangle
					anchors.left: batteryLabel.right
					width: 160
					height: batteryReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: batteryTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text:  systemSettings.cellCount
					}
				}
				
				C12.Button {
                    id: batteryReadButton
					anchors.left: batteryRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("countInfo")
                    }
                }
				
				Label {
                    id: cellLabel
                    width: 60
					height: cellWriteButton.height
					anchors.top: batteryLabel.bottom
					anchors.topMargin: 5
                    text: "温度数量"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: cellRectangle
					anchors.left: cellLabel.right
					anchors.top: batteryLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: cellTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text:  systemSettings.thermalCount
					}
				}
				
				C12.Button {
                    id: cellWriteButton
					anchors.left: cellRectangle.right
					anchors.top: batteryLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("countInfo", batteryTextInput.text + " " + cellTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				id: dateGroupBox
				anchors.fill: parent
				anchors.margins: 5
				title: "日期设置"
				clip: false
				
				property bool mpSelected: false
				
				Label {
                    id: productDateLabel
                    width: 60
					height: batteryReadButton.height
                    text: "生产日期"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: productDateRectangle
					anchors.left: productDateLabel.right
					width: 160
					height: batteryReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
						id: productDateTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
						readOnly: true
					}
				}
				
				C12.Button {
					anchors.right: productDateRectangle.right
					anchors.top: productDateRectangle.top
					width: cellWriteButton.height
					height: cellWriteButton.height
					iconSource: "images/ic_calendar.png"
                    onClicked: {
						calendarDialog.visible = true
						dateGroupBox.mpSelected = false
                    }
                }
				
				C12.Button {
                    id: productDateReadButton
					anchors.left: productDateRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                    }
                }
				
				Label {
                    id: mpDateLabel
                    width: 60
					height: cellWriteButton.height
					anchors.top: productDateLabel.bottom
					anchors.topMargin: 5
                    text: "出货日期"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: mpDateRectangle
					anchors.left: mpDateLabel.right
					anchors.top: productDateLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
						id: mpDateTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						readOnly: true
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
					anchors.right: mpDateRectangle.right
					anchors.top: mpDateRectangle.top
					width: cellWriteButton.height
					height: cellWriteButton.height
					iconSource: "images/ic_calendar.png"
                    onClicked: {
						calendarDialog.visible = true
						dateGroupBox.mpSelected = true
                    }
                }

				C12.Button {
                    id: mpDateWriteButton
					anchors.left: mpDateRectangle.right
					anchors.top: productDateLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("bmsMPDate", productDateTextInput.text + " " +mpDateTextInput.text)
                    }
                }
				
				Dialog {
					id: calendarDialog
					visible: false
					title: "选择日期"
					standardButtons: Dialog.Ok | Dialog.Cancel

					contentItem: Rectangle {
						C14.Calendar {
							id: calendar
							visible: true
							minimumDate: new Date(2020, 0, 1)
							maximumDate: new Date(2050, 0, 1)
							onClicked: {
							}
						}
					}
					
					onAccepted: {
						if (dateGroupBox.mpSelected)
                            mpDateTextInput.text = calendar.selectedDate.toLocaleDateString(Qt.locale("zh_CN"), "yyyy年MM月dd日")
						else
                            productDateTextInput.text = calendar.selectedDate.toLocaleDateString(Qt.locale("zh_CN"), "yyyy年MM月dd日")
					}
				}
				
				
			}
		}
		
		
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "均衡设置"
				
				Label {
                    id: enableDiffLabel
                    width: 85
					height: cellWriteButton.height
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
                    text: "开启压差"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: enableDiffLabelRectangle
					anchors.left: enableDiffLabel.right
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: balanceEnableDiffTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.balanceEnableVoltageDiff
					}
				}
				
				Label {
                    id: enableVoltageLabel
                    width: 85
					height: cellWriteButton.height
					anchors.left: enableDiffLabelRectangle.right
					anchors.topMargin: 5
					anchors.leftMargin: 20
                    text: "开启电压"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
                    id: enableVoltageRectangle
					anchors.left: enableVoltageLabel.right
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: balanceEnableVoltageTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.balanceEnableVoltage
					}
				}
				
				Label {
                    id: disableVoltageLabel
                    width: 85
					height: cellWriteButton.height
					anchors.top: enableVoltageRectangle.bottom
					anchors.topMargin: 5
                    text: "关闭电压"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: disableVoltageRectangle
					anchors.top: enableVoltageRectangle.bottom
					anchors.left: disableVoltageLabel.right
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: balanceDisableVoltageTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.balanceDisableVoltage
					}
				}
				
				
				C12.CheckBox {
                    id: checkBox
					anchors.left: enableVoltageLabel.left
					// anchors.top: enableVoltageRectangle.bottom
					anchors.verticalCenter: disableVoltageRectangle.verticalCenter
                    text: qsTr("使能")
                    checked: systemSettings.balanceEnableFlag==1 ? true : false
                }
				
				C12.Button {
                    id: balanceReadButton
					anchors.top: disableVoltageRectangle.bottom
					anchors.right: balanceWriteButton.left
					anchors.topMargin: 15
					anchors.rightMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("balanceInfo")
                    }
                }
				
				C12.Button {
                    id: balanceWriteButton
					anchors.top: disableVoltageRectangle.bottom
					anchors.right: enableVoltageRectangle.right
					anchors.topMargin: 15
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("balanceInfo", Number(checkBox.checked) + " "
                                                          + balanceEnableDiffTextInput.text + " "
                                                          + balanceEnableVoltageTextInput.text + " "
                                                          + balanceDisableVoltageTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "电阻设置"
				
				Label {
                    id: resistanceLabel
                    width: 80
					height: batteryReadButton.height
                    text: "采样电阻阻值"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: resistanceRectangle
					anchors.left: resistanceLabel.right
					width: 160
					height: batteryReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: resistanceTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.sampleResistanceValue
					}
				}
				
				C12.Button {
                    id: resistanceReadButton
					anchors.left: resistanceRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("resistance")
                    }
                }
				
				Label {
                    id: zeroCurrentLabel
                    width: 80
					height: cellWriteButton.height
					anchors.top: resistanceLabel.bottom
					anchors.topMargin: 5
                    text: "零电流AD值"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: zeroCurrentRectangle
					anchors.left: zeroCurrentLabel.right
					anchors.top: resistanceLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: zeroCurrentTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.zeroCurrentADCValue
					}
				}
				
				C12.Button {
                    id: zeroCurrentWriteButton
					anchors.left: zeroCurrentRectangle.right
					anchors.top: resistanceLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("resistance", resistanceTextInput.text + " " + zeroCurrentTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "循环设置"
				
				Label {
                    id: setCircleLabel
                    width: 85
					height: cellWriteButton.height
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
                    text: "设定循环次数"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: setCircleRectangle
					anchors.left: setCircleLabel.right
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: setCircleTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.chargingCircleSetting
					}
				}
				
				Label {
                    id: totalCircleLabel
                    width: 85
					height: cellWriteButton.height
					anchors.left: setCircleRectangle.right
					anchors.topMargin: 5
					anchors.leftMargin: 20
                    text: "累计循环次数"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: totalCircleRectangle
					anchors.left: totalCircleLabel.right
					// anchors.top: socLabel.bottom
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: totalCircleTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.totalChargingCirCle
					}
				}
				
				Label {
                    id: realCapacityLabel
                    width: 85
					height: cellWriteButton.height
					anchors.top: setCircleLabel.bottom
					anchors.topMargin: 5
                    text: "实际容量"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: realCapacityRectangle
					anchors.top: setCircleLabel.bottom
					anchors.left: realCapacityLabel.right
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: realCapacityTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.realCapacity
					}
				}
				
				Label {
                    id: setCapacityLabel
                    width: 85
					height: cellWriteButton.height
					anchors.top: setCircleLabel.bottom
					anchors.left: setCircleRectangle.right

					anchors.topMargin: 5
					anchors.leftMargin: 20
                    text: "设定容量"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: setCapacityRectangle
					anchors.left: setCapacityLabel.right
					anchors.top: setCircleLabel.bottom
					anchors.topMargin: 5
					width: 80
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: setCapacityTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.settingCapacity
					}
				}
				
				C12.Button {
                    id: capacityReadButton
					anchors.top: setCapacityRectangle.bottom
					anchors.right: capacityWriteButton.left
					anchors.topMargin: 10
					anchors.rightMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("circleSetting")
                    }
                }
				
				C12.Button {
                    id: capacityWriteButton
					anchors.top: setCapacityRectangle.bottom
					anchors.right: setCapacityRectangle.right
					anchors.topMargin: 10
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("circleSetting", setCircleTextInput.text + " "
                                                          + totalCircleTextInput.text + " "
                                                          + realCapacityTextInput.text + " "
                                                          + setCapacityTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "充放电系数"
				
				Label {
                    id: dischargingRatioLabel
                    width: 80
					height: productReadButton.height
                    text: "放电电流系数"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: dischargingRatioRectangle
					anchors.left: dischargingRatioLabel.right
					width: 120
					height: productReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: dischargingRatioTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text:  systemSettings.dischargingCurrentRatio
					}
				}
				
				C12.Button {
                    id: dischargingRatioReadButton
					anchors.left: dischargingRatioRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("dischargingCurrentRatio")
                    }
                }
				
				C12.Button {
                    id: dischargingRatioWriteButton
					anchors.left: dischargingRatioReadButton.right
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("dischargingCurrentRatio", dischargingRatioTextInput.text)
                    }
                }
				
				Label {
                    id: chargingRatioLabel
                    width: 80
					height: bmsReadButton.height
					anchors.top: dischargingRatioLabel.bottom
					anchors.topMargin: 5
                    text: "充电电流系数"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: chargingRatioRectangle
					anchors.left: chargingRatioLabel.right
					anchors.top: dischargingRatioLabel.bottom
					anchors.topMargin: 5
					width: 120
					height: bmsReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: chargingRatioTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text:  systemSettings.chargingCurrentRatio
					}
				}
				
				C12.Button {
                    id: chargingRatioReadButton
					anchors.left: chargingRatioRectangle.right
					anchors.top: dischargingRatioLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("chargingCurrentRatio")
                    }
                }
				
				C12.Button {
                    id: chargingRatioWriteButton
					anchors.left: chargingRatioReadButton.right
					anchors.top: dischargingRatioLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("chargingCurrentRatio", chargingRatioTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "soc / soh"
				
				Label {
                    id: socLabel
                    width: 60
					height: batteryReadButton.height
                    text: "SOC"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: socRectangle
					anchors.left: socLabel.right
					width: 160
					height: batteryReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: socTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
						text: systemSettings.soc
					}
				}
				
				C12.Button {
                    id: socReadButton
					anchors.left: socRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
						systemSettings.readSystemSetting("socSohSetting")
                    }
                }
				
				Label {
                    id: sohLabel
                    width: 60
					height: cellWriteButton.height
					anchors.top: socLabel.bottom
					anchors.topMargin: 5
                    text: "SOH"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: sohRectangle
					anchors.left: sohLabel.right
					anchors.top: socLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: sohTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.soh
					}
				}
				
				C12.Button {
                    id: sohWriteButton
					anchors.left: sohRectangle.right
					anchors.top: socLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("socSohSetting", socTextInput.text + " " + sohTextInput.text)
                    }
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "时间"
				
				C12.Button {
                    id: timeReadButton
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("读取模组时间")
                    onClicked: {
                        systemSettings.readSystemSetting("bmsRTCDate")
                    }
                }
				
				C12.Button {
                    id: timeWriteButton
					anchors.left: timeReadButton.right
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("写入系统时间")
                    onClicked: {
                         systemSettings.writeSystemSetting("bmsRTCDate" ,Qt.formatDateTime(new Date(), "yyyy-MM-dd hh:mm:ss"))
                    }
                }
				
				Label {
                    width: 60
					height: cellWriteButton.height
					anchors.top: timeWriteButton.bottom
					anchors.topMargin: 5
                    text: "XXXX-XX-XX"
					font.pointSize: 12
					verticalAlignment:  TextInput.AlignVCenter
                }
				
			}
		}
		
		Rectangle{
            width: root.width / 3
			height: root.height / 6
            radius: 10
            border.width: 1
            border.color:"black"

			C12.GroupBox {
				anchors.fill: parent
				anchors.margins: 5
				title: "版本设置"
				
				Label {
                    id: swVersionLabel
                    width: 60
					height: batteryReadButton.height
                    text: "软件版本"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: swVersionRectangle
					anchors.left: swVersionLabel.right
					width: 160
					height: batteryReadButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: swVersionTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.swVersion
					}
				}
				
				C12.Button {
                    id: swVersionReadButton
					anchors.left: swVersionRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                        systemSettings.readSystemSetting("version")
                    }
                }
				
				Label {
                    id: hwVersionLabel
                    width: 60
					height: cellWriteButton.height
					anchors.top: swVersionLabel.bottom
					anchors.topMargin: 5
                    text: "硬件版本"
					font.pointSize: 10
					verticalAlignment:  TextInput.AlignVCenter
                }
				
				Rectangle {
					id: hwVersionRectangle
					anchors.left: hwVersionLabel.right
					anchors.top: swVersionLabel.bottom
					anchors.topMargin: 5
					width: 160
					height: cellWriteButton.height
					color: "#e5e5e5"
					radius: 2
					border.width: 1
					border.color: "#353535"
					TextInput {
                        id: hwVersionTextInput
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
                        text: systemSettings.hwVersion
					}
				}
				
				C12.Button {
                    id: hwVersionWriteButton
					anchors.left: hwVersionRectangle.right
					anchors.top: swVersionLabel.bottom
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
                        systemSettings.writeSystemSetting("version", swVersionTextInput.text + " " + hwVersionTextInput.text)
                    }
                }
				
			}
		}
	}
	
}

import QtQuick 2.7
import QtQuick.Controls 2.2
import QtQuick.Controls 1.2 as C12

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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: productReadButton
					anchors.left: productRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                    }
                }
				
				C12.Button {
                    id: productWriteButton
					anchors.left: productReadButton.right
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: batteryReadButton
					anchors.left: batteryRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
				title: "日期设置"
				
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				
				C12.CheckBox {
                    id: checkBox
					anchors.left: enableVoltageLabel.left
					// anchors.top: enableVoltageRectangle.bottom
					anchors.verticalCenter: disableVoltageRectangle.verticalCenter
                    text: qsTr("使能")

                }
				
				C12.Button {
                    id: balanceReadButton
					anchors.top: disableVoltageRectangle.bottom
					anchors.right: balanceWriteButton.left
					anchors.topMargin: 15
					anchors.rightMargin: 10
                    text: qsTr("读取")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: resistanceReadButton
					anchors.left: resistanceRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: dischargingRatioReadButton
					anchors.left: dischargingRatioRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
                    }
                }
				
				C12.Button {
                    id: dischargingRatioWriteButton
					anchors.left: dischargingRatioReadButton.right
					anchors.leftMargin: 10
                    text: qsTr("设置")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: socReadButton
					anchors.left: socRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
                    }
                }
				
				C12.Button {
                    id: timeWriteButton
					anchors.left: timeReadButton.right
					anchors.topMargin: 5
					anchors.leftMargin: 10
                    text: qsTr("写入系统时间")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
					}
				}
				
				C12.Button {
                    id: swVersionReadButton
					anchors.left: swVersionRectangle.right
					anchors.leftMargin: 10
                    text: qsTr("读取")
                    onClicked: {
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
						anchors.fill: parent
						verticalAlignment: TextInput.AlignVCenter
						color: "black"
						leftPadding: 5
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
                    }
                }
				
			}
		}
	}
	
}
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(739, 558)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(-1, 0, 741, 561))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.initial_widget = QtWidgets.QWidget(self.layoutWidget)
        self.initial_widget.setStyleSheet("#initial_widget {\n"
"  background-color: #193DB7;\n"
"border-bottom-left-radius: 20%;\n"
"border-bottom-right-radius: 20%;\n"
"\n"
"}\n"
"\n"
"#initial_widget QLabel {\n"
"  color: white;\n"
"  border-radius: 50% 0 0 50%;\n"
"}\n"
"")
        self.initial_widget.setObjectName("initial_widget")
        self.frame = QtWidgets.QFrame(self.initial_widget)
        self.frame.setGeometry(QtCore.QRect(60, 20, 641, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(52, 20, 581, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.parameter_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.parameter_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.parameter_verticalLayout.setObjectName("parameter_verticalLayout")
        self.para_upper_frame = QtWidgets.QFrame(self.layoutWidget1)
        self.para_upper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para_upper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para_upper_frame.setObjectName("para_upper_frame")
        self.frame_8 = QtWidgets.QFrame(self.para_upper_frame)
        self.frame_8.setGeometry(QtCore.QRect(280, 10, 111, 71))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_8)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 40, 91, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_4.setObjectName("label_4")
        self.frame_11 = QtWidgets.QFrame(self.para_upper_frame)
        self.frame_11.setGeometry(QtCore.QRect(20, 10, 111, 71))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.comboBox = QtWidgets.QComboBox(self.frame_11)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.frame_11)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")
        self.frame_15 = QtWidgets.QFrame(self.para_upper_frame)
        self.frame_15.setGeometry(QtCore.QRect(140, 10, 111, 71))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_15)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 40, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame_15)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_7.setObjectName("label_7")
        self.frame_9 = QtWidgets.QFrame(self.para_upper_frame)
        self.frame_9.setGeometry(QtCore.QRect(420, 10, 120, 71))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_3.setGeometry(QtCore.QRect(8, 40, 101, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_3.setObjectName("label_3")
        self.parameter_verticalLayout.addWidget(self.para_upper_frame)
        self.para_lower_frame = QtWidgets.QFrame(self.layoutWidget1)
        self.para_lower_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para_lower_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para_lower_frame.setObjectName("para_lower_frame")
        self.frame_17 = QtWidgets.QFrame(self.para_lower_frame)
        self.frame_17.setGeometry(QtCore.QRect(290, 10, 111, 71))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_9.setGeometry(QtCore.QRect(10, 40, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_9 = QtWidgets.QLabel(self.frame_17)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_9.setObjectName("label_9")
        self.frame_18 = QtWidgets.QFrame(self.para_lower_frame)
        self.frame_18.setGeometry(QtCore.QRect(420, 10, 111, 71))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.comboBox_10 = QtWidgets.QComboBox(self.frame_18)
        self.comboBox_10.setGeometry(QtCore.QRect(10, 40, 101, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_10 = QtWidgets.QLabel(self.frame_18)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_10.setObjectName("label_10")
        self.frame_10 = QtWidgets.QFrame(self.para_lower_frame)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 111, 71))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 40, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.frame_16 = QtWidgets.QFrame(self.para_lower_frame)
        self.frame_16.setGeometry(QtCore.QRect(150, 10, 111, 71))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_16)
        self.comboBox_8.setGeometry(QtCore.QRect(10, 40, 91, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame_16)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_8.setObjectName("label_8")
        self.parameter_verticalLayout.addWidget(self.para_lower_frame)
        self.Save_pushButton = QtWidgets.QPushButton(self.initial_widget)
        self.Save_pushButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.Save_pushButton.setStyleSheet("border-radius: 10px;\n"
"")
        self.Save_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Save_pushButton.setIcon(icon)
        self.Save_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.Save_pushButton.setObjectName("Save_pushButton")
        self.start_pushButton = QtWidgets.QPushButton(self.initial_widget)
        self.start_pushButton.setGeometry(QtCore.QRect(340, 250, 91, 41))
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout.addWidget(self.initial_widget)
        self.evolution_widget = QtWidgets.QWidget(self.layoutWidget)
        self.evolution_widget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.evolution_widget.setObjectName("evolution_widget")
        self.frame_2 = QtWidgets.QFrame(self.evolution_widget)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 691, 161))
        self.frame_2.setStyleSheet("#frame_2 QWidget{\n"
"border: 2px solid #193DB7;\n"
"border-radius: 10px;\n"
"color:#193DB7;\n"
"}\n"
"\n"
"#frame_2 QSpinBox{\n"
"border: 5px solid #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#frame_2 QWidget{\n"
"  background-color: #193DB7;\n"
"\n"
"}\n"
"\n"
"#frame_2 QFrame{\n"
"  background-color: white;\n"
"\n"
"}\n"
"\n"
"#frame_2 SpinBox{\n"
"  background-color: white;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_9 = QtWidgets.QWidget(self.frame_2)
        self.widget_9.setStyleSheet("")
        self.widget_9.setObjectName("widget_9")
        self.frame_6 = QtWidgets.QFrame(self.widget_9)
        self.frame_6.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.play_pushButton = QtWidgets.QPushButton(self.frame_6)
        self.play_pushButton.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.play_pushButton.setStyleSheet("border-radius: 10px;")
        self.play_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/play-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pushButton.setIcon(icon1)
        self.play_pushButton.setObjectName("play_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(self.frame_6)
        self.stop_pushButton.setGeometry(QtCore.QRect(70, 20, 31, 31))
        self.stop_pushButton.setStyleSheet("border-radius: 10px;")
        self.stop_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-stop-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_pushButton.setIcon(icon2)
        self.stop_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.widget_9)
        self.spinBox.setGeometry(QtCore.QRect(30, 110, 91, 22))
        self.spinBox.setStyleSheet("background-color: white;\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.frame_2)
        self.widget_8.setObjectName("widget_8")
        self.frame_5 = QtWidgets.QFrame(self.widget_8)
        self.frame_5.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.play_pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.play_pushButton_2.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.play_pushButton_2.setStyleSheet("border-radius: 10px;")
        self.play_pushButton_2.setText("")
        self.play_pushButton_2.setIcon(icon1)
        self.play_pushButton_2.setObjectName("play_pushButton_2")
        self.stop_pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.stop_pushButton_2.setGeometry(QtCore.QRect(70, 20, 31, 31))
        self.stop_pushButton_2.setStyleSheet("border-radius: 10px;")
        self.stop_pushButton_2.setText("")
        self.stop_pushButton_2.setIcon(icon2)
        self.stop_pushButton_2.setIconSize(QtCore.QSize(25, 25))
        self.stop_pushButton_2.setObjectName("stop_pushButton_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget_8)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 110, 91, 22))
        self.spinBox_2.setStyleSheet("background-color: white;\n"
"")
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.widget_8)
        self.widget_7 = QtWidgets.QWidget(self.frame_2)
        self.widget_7.setObjectName("widget_7")
        self.frame_4 = QtWidgets.QFrame(self.widget_7)
        self.frame_4.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.play_pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.play_pushButton_3.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.play_pushButton_3.setStyleSheet("border-radius: 10px;")
        self.play_pushButton_3.setText("")
        self.play_pushButton_3.setIcon(icon1)
        self.play_pushButton_3.setObjectName("play_pushButton_3")
        self.stop_pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.stop_pushButton_3.setGeometry(QtCore.QRect(70, 20, 31, 31))
        self.stop_pushButton_3.setStyleSheet("border-radius: 10px;")
        self.stop_pushButton_3.setText("")
        self.stop_pushButton_3.setIcon(icon2)
        self.stop_pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.stop_pushButton_3.setObjectName("stop_pushButton_3")
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget_7)
        self.spinBox_3.setGeometry(QtCore.QRect(30, 110, 91, 22))
        self.spinBox_3.setStyleSheet("background-color: white;\n"
"")
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.frame_2)
        self.widget_6.setObjectName("widget_6")
        self.frame_3 = QtWidgets.QFrame(self.widget_6)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 120, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.play_pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.play_pushButton_4.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.play_pushButton_4.setStyleSheet("border-radius: 10px;")
        self.play_pushButton_4.setText("")
        self.play_pushButton_4.setIcon(icon1)
        self.play_pushButton_4.setObjectName("play_pushButton_4")
        self.stop_pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.stop_pushButton_4.setGeometry(QtCore.QRect(70, 20, 31, 31))
        self.stop_pushButton_4.setStyleSheet("border-radius: 10px;")
        self.stop_pushButton_4.setText("")
        self.stop_pushButton_4.setIcon(icon2)
        self.stop_pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.stop_pushButton_4.setObjectName("stop_pushButton_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget_6)
        self.spinBox_4.setGeometry(QtCore.QRect(30, 110, 91, 22))
        self.spinBox_4.setStyleSheet("background-color: white;\n"
"")
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout.addWidget(self.widget_6)
        self.evolve_pushButton = QtWidgets.QPushButton(self.evolution_widget)
        self.evolve_pushButton.setGeometry(QtCore.QRect(250, 190, 241, 31))
        self.evolve_pushButton.setStyleSheet("background-color: #193DB7;\n"
"color:white;")
        self.evolve_pushButton.setObjectName("evolve_pushButton")
        self.verticalLayout.addWidget(self.evolution_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_4.setItemText(0, _translate("Form", "2"))
        self.comboBox_4.setItemText(1, _translate("Form", "4"))
        self.comboBox_4.setItemText(2, _translate("Form", "6"))
        self.comboBox_4.setItemText(3, _translate("Form", "8"))
        self.label_4.setText(_translate("Form", "Steps"))
        self.comboBox.setItemText(0, _translate("Form", "8"))
        self.comboBox.setItemText(1, _translate("Form", "5"))
        self.comboBox.setItemText(2, _translate("Form", "4"))
        self.comboBox.setItemText(3, _translate("Form", "6"))
        self.label.setText(_translate("Form", "Num of Bars"))
        self.comboBox_7.setItemText(0, _translate("Form", "4"))
        self.comboBox_7.setItemText(1, _translate("Form", "2"))
        self.comboBox_7.setItemText(2, _translate("Form", "3"))
        self.comboBox_7.setItemText(3, _translate("Form", "5"))
        self.comboBox_7.setItemText(4, _translate("Form", "6"))
        self.comboBox_7.setItemText(5, _translate("Form", "7"))
        self.comboBox_7.setItemText(6, _translate("Form", "8"))
        self.label_7.setText(_translate("Form", "Num of Notes"))
        self.comboBox_3.setItemText(0, _translate("Form", "major"))
        self.comboBox_3.setItemText(1, _translate("Form", "minorM"))
        self.comboBox_3.setItemText(2, _translate("Form", "dorian"))
        self.comboBox_3.setItemText(3, _translate("Form", "phrygian"))
        self.comboBox_3.setItemText(4, _translate("Form", "lydian"))
        self.comboBox_3.setItemText(5, _translate("Form", "mixolydian"))
        self.comboBox_3.setItemText(6, _translate("Form", "aeolian"))
        self.comboBox_3.setItemText(7, _translate("Form", "locrian"))
        self.label_3.setText(_translate("Form", "Scale"))
        self.comboBox_9.setItemText(0, _translate("Form", "C"))
        self.comboBox_9.setItemText(1, _translate("Form", "C#"))
        self.comboBox_9.setItemText(2, _translate("Form", "Db"))
        self.comboBox_9.setItemText(3, _translate("Form", "D"))
        self.comboBox_9.setItemText(4, _translate("Form", "D#"))
        self.comboBox_9.setItemText(5, _translate("Form", "Eb"))
        self.comboBox_9.setItemText(6, _translate("Form", "E"))
        self.comboBox_9.setItemText(7, _translate("Form", "F#"))
        self.comboBox_9.setItemText(8, _translate("Form", "Gb"))
        self.comboBox_9.setItemText(9, _translate("Form", "G"))
        self.comboBox_9.setItemText(10, _translate("Form", "G#"))
        self.comboBox_9.setItemText(11, _translate("Form", "Ab"))
        self.comboBox_9.setItemText(12, _translate("Form", "A"))
        self.comboBox_9.setItemText(13, _translate("Form", "A#"))
        self.comboBox_9.setItemText(14, _translate("Form", "Bb"))
        self.label_9.setText(_translate("Form", "Chord Progression"))
        self.comboBox_10.setItemText(0, _translate("Form", "1"))
        self.comboBox_10.setItemText(1, _translate("Form", "0"))
        self.label_10.setText(_translate("Form", "Pauses"))
        self.comboBox_2.setItemText(0, _translate("Form", "C"))
        self.comboBox_2.setItemText(1, _translate("Form", "C#"))
        self.comboBox_2.setItemText(2, _translate("Form", "Db"))
        self.comboBox_2.setItemText(3, _translate("Form", "D"))
        self.comboBox_2.setItemText(4, _translate("Form", "D#"))
        self.comboBox_2.setItemText(5, _translate("Form", "Eb"))
        self.comboBox_2.setItemText(6, _translate("Form", "E"))
        self.comboBox_2.setItemText(7, _translate("Form", "F#"))
        self.comboBox_2.setItemText(8, _translate("Form", "F"))
        self.comboBox_2.setItemText(9, _translate("Form", "G"))
        self.comboBox_2.setItemText(10, _translate("Form", "G#"))
        self.comboBox_2.setItemText(11, _translate("Form", "Ab"))
        self.comboBox_2.setItemText(12, _translate("Form", "Bb"))
        self.label_2.setText(_translate("Form", "Key"))
        self.comboBox_8.setItemText(0, _translate("Form", "4"))
        self.comboBox_8.setItemText(1, _translate("Form", "2"))
        self.comboBox_8.setItemText(2, _translate("Form", "3"))
        self.comboBox_8.setItemText(3, _translate("Form", "6"))
        self.comboBox_8.setItemText(4, _translate("Form", "5"))
        self.label_8.setText(_translate("Form", "Root"))
        self.start_pushButton.setText(_translate("Form", "START"))
        self.evolve_pushButton.setText(_translate("Form", "Evolve A Generation"))
import resource_rc
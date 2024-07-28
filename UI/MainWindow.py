# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(902, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 900, 600))
        self.widget.setMinimumSize(QSize(900, 600))
        self.widget.setMaximumSize(QSize(900, 600))
        self.widget.setStyleSheet(u"#widget{\n"
"background-color:rgb(45,56,96);\n"
"border-radius:20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"background-color:rgb(17,30,70);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 24pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(209, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hiding = QPushButton(self.frame)
        self.hiding.setObjectName(u"hiding")
        self.hiding.setStyleSheet(u"#hiding{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon = QIcon()
        icon.addFile(u":/img/icon/\u7f29\u5c0f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hiding.setIcon(icon)
        self.hiding.setIconSize(QSize(23, 30))

        self.horizontalLayout_3.addWidget(self.hiding)

        self.enlarge = QPushButton(self.frame)
        self.enlarge.setObjectName(u"enlarge")
        self.enlarge.setStyleSheet(u"#enlarge{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon1 = QIcon()
        icon1.addFile(u":/img/icon/\u5c0f\u7a97.png", QSize(), QIcon.Normal, QIcon.Off)
        self.enlarge.setIcon(icon1)
        self.enlarge.setIconSize(QSize(23, 30))

        self.horizontalLayout_3.addWidget(self.enlarge)

        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"#close{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon2 = QIcon()
        icon2.addFile(u":/img/icon/\u5173\u95ed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(23, 30))

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(10)
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftBar = QWidget(self.widget_3)
        self.LeftBar.setObjectName(u"LeftBar")
        self.LeftBar.setMinimumSize(QSize(68, 0))
        self.LeftBar.setMaximumSize(QSize(68, 16777215))
        self.LeftBar.setStyleSheet(u"#LeftBar{\n"
"background-color:rgb(17,30,70);\n"
"border-bottom-left-radius:15px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.LeftBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.LeftBar)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy3)
        self.widget_4.setMinimumSize(QSize(160, 68))
        self.widget_4.setMaximumSize(QSize(160, 68))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(68, 68))
        self.frame_2.setMaximumSize(QSize(68, 68))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.LeftBar)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy4)
        self.widget_6.setMinimumSize(QSize(160, 0))
        self.widget_6.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.event = QPushButton(self.widget_6)
        self.event.setObjectName(u"event")
        self.event.setMinimumSize(QSize(60, 0))
        self.event.setMaximumSize(QSize(160, 16777215))
        self.event.setStyleSheet(u"#event{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon3 = QIcon()
        icon3.addFile(u":/img/icon/\u5f85\u529e full.png", QSize(), QIcon.Normal, QIcon.Off)
        self.event.setIcon(icon3)
        self.event.setIconSize(QSize(47, 47))

        self.verticalLayout_3.addWidget(self.event)

        self.add = QPushButton(self.widget_6)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(60, 0))
        self.add.setMaximumSize(QSize(160, 16777215))
        self.add.setStyleSheet(u"#add{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon4 = QIcon()
        icon4.addFile(u":/img/icon/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add.setIcon(icon4)
        self.add.setIconSize(QSize(43, 43))

        self.verticalLayout_3.addWidget(self.add)

        self.four = QPushButton(self.widget_6)
        self.four.setObjectName(u"four")
        self.four.setMinimumSize(QSize(60, 0))
        self.four.setMaximumSize(QSize(160, 16777215))
        self.four.setStyleSheet(u"#four{\n"
"	color:rgb(255,255,255);\n"
"	font: 26pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                background-color: rgb(45, 56, 96);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: rgb(17, 30, 70);\n"
"            }")
        icon5 = QIcon()
        icon5.addFile(u":/img/icon/\u5de5\u4f5c\u53f0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.four.setIcon(icon5)
        self.four.setIconSize(QSize(58, 58))

        self.verticalLayout_3.addWidget(self.four)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.LeftBar)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(160, 0))
        self.widget_7.setMaximumSize(QSize(160, 16777215))

        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.LeftBar)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget = QStackedWidget(self.widget_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.edit = QWidget()
        self.edit.setObjectName(u"edit")
        self.event_txt = QLineEdit(self.edit)
        self.event_txt.setObjectName(u"event_txt")
        self.event_txt.setGeometry(QRect(20, 40, 261, 41))
        self.event_txt.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.label_12 = QLabel(self.edit)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(500, 0, 101, 31))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.dateTimeEdit_2 = QDateTimeEdit(self.edit)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(500, 40, 261, 41))
        self.dateTimeEdit_2.setStyleSheet(u"font: 12pt \"Microsoft YaHei UI\";")
        self.label_13 = QLabel(self.edit)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 0, 91, 31))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.save_btn_2 = QPushButton(self.edit)
        self.save_btn_2.setObjectName(u"save_btn_2")
        self.save_btn_2.setGeometry(QRect(590, 460, 111, 31))
        self.save_btn_2.setStyleSheet(u"#save_btn_2{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 18pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                \n"
"	background-color: rgb(17, 30, 70);\n"
"            }\n"
"            QPushButton:pressed {\n"
"	\n"
"                background-color: rgb(45, 56, 96);\n"
"            }")
        self.label_14 = QLabel(self.edit)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 460, 101, 31))
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.label_15 = QLabel(self.edit)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 90, 71, 31))
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.textEdit = QTextEdit(self.edit)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 130, 751, 311))
        self.textEdit.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.layoutWidget = QWidget(self.edit)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 470, 436, 22))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.radioButton_4)

        self.layoutWidget1 = QWidget(self.edit)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(340, 40, 101, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_8.addWidget(self.checkBox)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.delete_btn = QPushButton(self.edit)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(710, 460, 101, 31))
        self.delete_btn.setStyleSheet(u"#delete_btn{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 18pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                \n"
"	background-color: rgb(17, 30, 70);\n"
"            }\n"
"            QPushButton:pressed {\n"
"	\n"
"                background-color: rgb(45, 56, 96);\n"
"            }")
        self.stackedWidget.addWidget(self.edit)
        self.event_2 = QWidget()
        self.event_2.setObjectName(u"event_2")
        self.gridLayout = QGridLayout(self.event_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list4 = QListWidget(self.event_2)
        self.list4.setObjectName(u"list4")
        self.list4.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.list4, 3, 1, 1, 1)

        self.list2 = QListWidget(self.event_2)
        self.list2.setObjectName(u"list2")
        self.list2.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.list2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.event_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.list3 = QListWidget(self.event_2)
        self.list3.setObjectName(u"list3")
        self.list3.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.list3, 3, 0, 1, 1)

        self.list1 = QListWidget(self.event_2)
        self.list1.setObjectName(u"list1")
        self.list1.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.list1, 1, 1, 1, 1)

        self.label_8 = QLabel(self.event_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_9 = QLabel(self.event_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.event_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.event_2)
        self.add_2 = QWidget()
        self.add_2.setObjectName(u"add_2")
        self.des_txt = QTextEdit(self.add_2)
        self.des_txt.setObjectName(u"des_txt")
        self.des_txt.setGeometry(QRect(9, 133, 796, 291))
        self.des_txt.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.label_3 = QLabel(self.add_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(9, 9, 101, 31))
        self.label_4 = QLabel(self.add_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 129, 31))
        self.status_check = QCheckBox(self.add_2)
        self.status_check.setObjectName(u"status_check")
        self.status_check.setGeometry(QRect(330, 50, 106, 41))
        self.status_check.setStyleSheet(u"font: 22pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255);")
        self.Event_txt = QLineEdit(self.add_2)
        self.Event_txt.setObjectName(u"Event_txt")
        self.Event_txt.setGeometry(QRect(10, 50, 291, 41))
        self.Event_txt.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.label_5 = QLabel(self.add_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 10, 121, 31))
        self.label_6 = QLabel(self.add_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 450, 141, 41))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft YaHei UI\";")
        self.dateTimeEdit = QDateTimeEdit(self.add_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(470, 50, 281, 41))
        self.dateTimeEdit.setStyleSheet(u"font: 16pt \"Microsoft YaHei UI\";")
        self.save_btn = QPushButton(self.add_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(650, 460, 141, 31))
        self.save_btn.setStyleSheet(u"#save_btn{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 18pt \"Microsoft YaHei UI\";\n"
"}\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-botton:5px;\n"
"}\n"
"QPushButton:hover {\n"
"                \n"
"			background-color: rgb(17, 30, 70);\n"
"            }\n"
"            QPushButton:pressed {\n"
"	\n"
"                background-color: rgb(45, 56, 96);\n"
"            }")
        icon6 = QIcon()
        icon6.addFile(u":/img/icon/\u90e8\u7f72.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon6)
        self.layoutWidget2 = QWidget(self.add_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(170, 460, 444, 22))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.RBtn1 = QRadioButton(self.layoutWidget2)
        self.RBtn1.setObjectName(u"RBtn1")
        self.RBtn1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.RBtn1)

        self.RBtn2 = QRadioButton(self.layoutWidget2)
        self.RBtn2.setObjectName(u"RBtn2")
        self.RBtn2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.RBtn2)

        self.RBtn3 = QRadioButton(self.layoutWidget2)
        self.RBtn3.setObjectName(u"RBtn3")
        self.RBtn3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.RBtn3)

        self.RBtn4 = QRadioButton(self.layoutWidget2)
        self.RBtn4.setObjectName(u"RBtn4")
        self.RBtn4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.RBtn4)

        self.label_11 = QLabel(self.add_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 50, 81, 41))
        self.label_11.setStyleSheet(u"font: 18pt \"Microsoft YaHei UI\";")
        self.stackedWidget.addWidget(self.add_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.closeBtn.clicked.connect(MainWindow.close)
        self.hiding.clicked.connect(MainWindow.showMinimized)
        self.enlarge.clicked.connect(MainWindow.showMaximized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"To Do", None))
        self.hiding.setText("")
        self.enlarge.setText("")
        self.closeBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.event.setText(QCoreApplication.translate("MainWindow", u" Event", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u" Add  ", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"   Four", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u622a\u6b62\u65f6\u95f4", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u4e8b\u4ef6", None))
        self.save_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u7f16\u8f91", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u8981\u7a0b\u5ea6", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5177\u4f53", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u4f1a\u5676", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u8fd8\u6d3b\u7740", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u8fd8\u6d3b\u7684\u597d\u597d\u7684", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u8fd8\u6d3b\u7684\u66f4\u597d", None))
        self.checkBox.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u4efb\u52a1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; font-style:italic; color:#ffffff;\">\u4e0d\u91cd\u8981\u4e0d\u7d27\u6025</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; font-style:italic; color:#ffffff;\">\u7d27\u6025</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; font-style:italic; color:#ffffff;\">\u91cd\u8981</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; font-style:italic; color:#ffffff;\">\u91cd\u8981\u7d27\u6025</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">\u4e8b\u9879</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">\u5177\u4f53</span></p></body></html>", None))
        self.status_check.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">\u622a\u6b62\u65f6\u95f4</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u91cd\u8981\u7a0b\u5ea6</p></body></html>", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.RBtn1.setText(QCoreApplication.translate("MainWindow", u"  \u4e0d\u505a\u6211\u4f1a\u5676", None))
        self.RBtn2.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u8fd8\u6d3b\u7740", None))
        self.RBtn3.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u8fd8\u6d3b\u7684\u597d\u597d\u7684", None))
        self.RBtn4.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u505a\u6211\u6d3b\u7684\u66f4\u597d", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">\u672a\u5b8c\u6210</span></p></body></html>", None))
    # retranslateUi


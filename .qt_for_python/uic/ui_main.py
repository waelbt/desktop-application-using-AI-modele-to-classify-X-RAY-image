# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 678)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(0, 68, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_toggle)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/image/img/Untitled-1.png);\n"
"background-color: rgb(0, 68, 255);\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/image/img/Untitled-2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/image/img/Untitled-2.png);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_page_1)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: rgb(0, 68, 255);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(250, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(0, 68, 255);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_page_2 = QPushButton(self.frame_left_menu)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/image/img/newtest.png);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/image/img/newtest2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"border-image: url(:/image/img/newtest2.png);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_left_menu)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	\n"
"	border-image: url(:/image/img/save1.png);\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"border-image: url(:/image/img/save2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"url(:/image/img/save2.png)\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_page_3)

        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(910, 618))
        self.stackedWidget.setMaximumSize(QSize(1000, 1000))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 590, 111, 21))
        self.label.setStyleSheet(u"color: rgb(170, 0, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"text-decoration-line: overline; ")
        self.warningbtn = QPushButton(self.page_1)
        self.warningbtn.setObjectName(u"warningbtn")
        self.warningbtn.setGeometry(QRect(330, 580, 281, 31))
        self.warningbtn.setStyleSheet(u"\n"
"QPushButton{\n"
"color:red;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
" \n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"text-decoration: underline;\n"
"}")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 10, 131, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgba(255, 255, 255,210);")
        self.logoutbtn = QPushButton(self.page_1)
        self.logoutbtn.setObjectName(u"logoutbtn")
        self.logoutbtn.setGeometry(QRect(850, 550, 51, 61))
        self.logoutbtn.setStyleSheet(u"\n"
"QPushButton {\n"
"border-image: url(:/image/59399.png);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 68, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 68, 255);\n"
"}")
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 130, 791, 51))
        self.label_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 255);")
        self.moreinfobtn = QPushButton(self.page_1)
        self.moreinfobtn.setObjectName(u"moreinfobtn")
        self.moreinfobtn.setGeometry(QRect(50, 190, 151, 31))
        self.moreinfobtn.setStyleSheet(u"\n"
"QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"text-decoration: underline;\n"
"}\n"
"QPushButton:pressed{\n"
"text-decoration: underline;\n"
"}")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(49, 229, 821, 191))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 801, 21))
        self.label_4.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 801, 31))
        self.label_5.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 50, 71, 21))
        self.label_6.setStyleSheet(u"color:red;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 611, 21))
        self.label_7.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 110, 211, 21))
        self.label_8.setStyleSheet(u"color:red;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 140, 801, 31))
        self.label_9.setStyleSheet(u"color: rgb(0, 85, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 160, 431, 221))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 68, 255);\n"
"color: rgb(85, 85, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(130, 0, 151, 41))
        self.label_10.setStyleSheet(u"color:red;\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.verticalLayoutWidget = QWidget(self.frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 49, 401, 161))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color:red;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_12)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Shell Dlg 2\";")

        self.verticalLayout_6.addWidget(self.label_14)

        self.closewframe = QPushButton(self.frame_2)
        self.closewframe.setObjectName(u"closewframe")
        self.closewframe.setGeometry(QRect(390, 10, 31, 23))
        self.closewframe.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.logoutbtn_2 = QPushButton(self.page_2)
        self.logoutbtn_2.setObjectName(u"logoutbtn_2")
        self.logoutbtn_2.setGeometry(QRect(850, 550, 51, 61))
        self.logoutbtn_2.setStyleSheet(u"\n"
"QPushButton {\n"
"border-image: url(:/image/59399.png);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 68, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 68, 255);\n"
"}")
        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(390, 10, 131, 31))
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgba(255, 255, 255,210);")
        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 60, 331, 461))
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 108), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.imag_cdr = QLabel(self.page_2)
        self.imag_cdr.setObjectName(u"imag_cdr")
        self.imag_cdr.setGeometry(QRect(80, 120, 244, 244))
        self.imag_cdr.setStyleSheet(u"background-color: rgb(170, 170, 255);color: rgb(0, 85, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.importbtn = QPushButton(self.page_2)
        self.importbtn.setObjectName(u"importbtn")
        self.importbtn.setGeometry(QRect(120, 400, 171, 41))
        self.importbtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 68, 255);\n"
"border-radius:5px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(130,170,90);\n"
"}")
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(430, 60, 461, 301))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 108), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(610, 70, 111, 21))
        self.label_20.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(470, 140, 381, 111))
        self.frame_3.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"color: rgb(255, 32, 3);\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 60, 111, 31))
        self.label_21.setStyleSheet(u"")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 10, 121, 41))
        self.pred_label = QLabel(self.frame_3)
        self.pred_label.setObjectName(u"pred_label")
        self.pred_label.setGeometry(QRect(130, 20, 211, 20))
        self.proba_label = QLabel(self.frame_3)
        self.proba_label.setObjectName(u"proba_label")
        self.proba_label.setGeometry(QRect(130, 70, 191, 21))
        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 370, 113, 20))
        self.preditct_btn = QPushButton(self.page_2)
        self.preditct_btn.setObjectName(u"preditct_btn")
        self.preditct_btn.setGeometry(QRect(610, 290, 91, 41))
        self.preditct_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 68, 255);\n"
"border-radius:5px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(130,170,90);\n"
"}")
        self.save_btn = QPushButton(self.page_2)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(320, 540, 171, 41))
        self.save_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 68, 255);\n"
"border-radius:5px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(130,170,90);\n"
"}")
        self.resulatframe = QFrame(self.page_2)
        self.resulatframe.setObjectName(u"resulatframe")
        self.resulatframe.setGeometry(QRect(250, -10, 421, 621))
        self.resulatframe.setStyleSheet(u"background-color: rgb(0, 68, 255);\n"
"\n"
"border-radius:20px;")
        self.resulatframe.setFrameShape(QFrame.StyledPanel)
        self.resulatframe.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.resulatframe)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(140, 20, 121, 31))
        self.label_23.setFont(font)
        self.label_23.setStyleSheet(u"color: rgba(255, 255, 255,210);")
        self.addtest = QPushButton(self.resulatframe)
        self.addtest.setObjectName(u"addtest")
        self.addtest.setGeometry(QRect(40, 530, 121, 41))
        self.addtest.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.cancelbtn = QPushButton(self.resulatframe)
        self.cancelbtn.setObjectName(u"cancelbtn")
        self.cancelbtn.setGeometry(QRect(230, 530, 121, 41))
        self.cancelbtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.close_btn = QPushButton(self.resulatframe)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(374, 20, 41, 23))
        self.close_btn.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.verticalLayoutWidget_2 = QWidget(self.resulatframe)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 70, 371, 431))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.idtest = QLineEdit(self.verticalLayoutWidget_2)
        self.idtest.setObjectName(u"idtest")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.idtest.setFont(font2)
        self.idtest.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.idtest)

        self.idclient = QLineEdit(self.verticalLayoutWidget_2)
        self.idclient.setObjectName(u"idclient")
        self.idclient.setFont(font2)
        self.idclient.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.idclient)

        self.nomprenon = QLineEdit(self.verticalLayoutWidget_2)
        self.nomprenon.setObjectName(u"nomprenon")
        self.nomprenon.setFont(font2)
        self.nomprenon.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.nomprenon)

        self.cinclient = QLineEdit(self.verticalLayoutWidget_2)
        self.cinclient.setObjectName(u"cinclient")
        self.cinclient.setFont(font2)
        self.cinclient.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.cinclient)

        self.path = QLineEdit(self.verticalLayoutWidget_2)
        self.path.setObjectName(u"path")
        self.path.setFont(font2)
        self.path.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.path)

        self.prediresutt = QLineEdit(self.verticalLayoutWidget_2)
        self.prediresutt.setObjectName(u"prediresutt")
        self.prediresutt.setFont(font2)
        self.prediresutt.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.prediresutt)

        self.proba = QLineEdit(self.verticalLayoutWidget_2)
        self.proba.setObjectName(u"proba")
        self.proba.setFont(font2)
        self.proba.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")
        self.proba.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_7.addWidget(self.proba)

        self.date = QLineEdit(self.verticalLayoutWidget_2)
        self.date.setObjectName(u"date")
        self.date.setFont(font2)
        self.date.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_7.addWidget(self.date)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.logoutbtn_3 = QPushButton(self.page_3)
        self.logoutbtn_3.setObjectName(u"logoutbtn_3")
        self.logoutbtn_3.setGeometry(QRect(850, 550, 51, 61))
        self.logoutbtn_3.setStyleSheet(u"\n"
"QPushButton {\n"
"border-image: url(:/image/59399.png);\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 68, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 68, 255);\n"
"}")
        self.tableWidget = QTableWidget(self.page_3)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem21)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 70, 841, 441))
        self.tableWidget.setMinimumSize(QSize(841, 441))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.videbtn = QPushButton(self.page_3)
        self.videbtn.setObjectName(u"videbtn")
        self.videbtn.setGeometry(QRect(540, 520, 121, 41))
        self.videbtn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.editbtn = QPushButton(self.page_3)
        self.editbtn.setObjectName(u"editbtn")
        self.editbtn.setGeometry(QRect(240, 520, 121, 41))
        self.editbtn.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_4 = QFrame(self.page_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(160, 230, 301, 141))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 68, 255);\n"
"\n"
"border-radius:20px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.close_btn_2 = QPushButton(self.frame_4)
        self.close_btn_2.setObjectName(u"close_btn_2")
        self.close_btn_2.setGeometry(QRect(240, 10, 41, 23))
        self.close_btn_2.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.idtest_2 = QLineEdit(self.frame_4)
        self.idtest_2.setObjectName(u"idtest_2")
        self.idtest_2.setGeometry(QRect(20, 50, 241, 24))
        self.idtest_2.setFont(font2)
        self.idtest_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")
        self.deletebtn_3 = QPushButton(self.frame_4)
        self.deletebtn_3.setObjectName(u"deletebtn_3")
        self.deletebtn_3.setGeometry(QRect(90, 90, 111, 41))
        self.deletebtn_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.deletebtn_4 = QPushButton(self.page_3)
        self.deletebtn_4.setObjectName(u"deletebtn_4")
        self.deletebtn_4.setGeometry(QRect(390, 520, 111, 41))
        self.deletebtn_4.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(0, 85, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(490, 230, 301, 141))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 68, 255);\n"
"\n"
"border-radius:20px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.close_btn_3 = QPushButton(self.frame_5)
        self.close_btn_3.setObjectName(u"close_btn_3")
        self.close_btn_3.setGeometry(QRect(240, 10, 41, 23))
        self.close_btn_3.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.idtest_3 = QLineEdit(self.frame_5)
        self.idtest_3.setObjectName(u"idtest_3")
        self.idtest_3.setGeometry(QRect(20, 50, 241, 24))
        self.idtest_3.setFont(font2)
        self.idtest_3.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")
        self.modibtn = QPushButton(self.frame_5)
        self.modibtn.setObjectName(u"modibtn")
        self.modibtn.setGeometry(QRect(90, 90, 111, 41))
        self.modibtn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.resulatframe_2 = QFrame(self.page_3)
        self.resulatframe_2.setObjectName(u"resulatframe_2")
        self.resulatframe_2.setGeometry(QRect(310, -20, 421, 621))
        self.resulatframe_2.setStyleSheet(u"background-color: rgb(0, 68, 255);\n"
"\n"
"border-radius:20px;")
        self.resulatframe_2.setFrameShape(QFrame.StyledPanel)
        self.resulatframe_2.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.resulatframe_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(140, 20, 121, 31))
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(u"color: rgba(255, 255, 255,210);")
        self.editbtnn = QPushButton(self.resulatframe_2)
        self.editbtnn.setObjectName(u"editbtnn")
        self.editbtnn.setGeometry(QRect(40, 530, 121, 41))
        self.editbtnn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.deletebtn_5 = QPushButton(self.resulatframe_2)
        self.deletebtn_5.setObjectName(u"deletebtn_5")
        self.deletebtn_5.setGeometry(QRect(230, 530, 121, 41))
        self.deletebtn_5.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(167, 155, 255);\n"
"border-radius:20px;\n"
"padding-top:5px;\n"
"color:rgb(226,234,216);\n"
"font: 25 14pt \"Yu Gothic Light\";\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(85, 170, 255);\n"
"\n"
"}")
        self.close_btn_4 = QPushButton(self.resulatframe_2)
        self.close_btn_4.setObjectName(u"close_btn_4")
        self.close_btn_4.setGeometry(QRect(374, 20, 41, 23))
        self.close_btn_4.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.verticalLayoutWidget_3 = QWidget(self.resulatframe_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(30, 70, 371, 431))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.idtest_4 = QLineEdit(self.verticalLayoutWidget_3)
        self.idtest_4.setObjectName(u"idtest_4")
        self.idtest_4.setFont(font2)
        self.idtest_4.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.idtest_4)

        self.idclient_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.idclient_2.setObjectName(u"idclient_2")
        self.idclient_2.setFont(font2)
        self.idclient_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.idclient_2)

        self.nomprenon_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.nomprenon_2.setObjectName(u"nomprenon_2")
        self.nomprenon_2.setFont(font2)
        self.nomprenon_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.nomprenon_2)

        self.cinclient_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.cinclient_2.setObjectName(u"cinclient_2")
        self.cinclient_2.setFont(font2)
        self.cinclient_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.cinclient_2)

        self.path_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.path_2.setObjectName(u"path_2")
        self.path_2.setFont(font2)
        self.path_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.path_2)

        self.prediresutt_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.prediresutt_2.setObjectName(u"prediresutt_2")
        self.prediresutt_2.setFont(font2)
        self.prediresutt_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.prediresutt_2)

        self.proba_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.proba_2.setObjectName(u"proba_2")
        self.proba_2.setFont(font2)
        self.proba_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")
        self.proba_2.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_8.addWidget(self.proba_2)

        self.date_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.date_2.setObjectName(u"date_2")
        self.date_2.setFont(font2)
        self.date_2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid white;\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:4px;")

        self.verticalLayout_8.addWidget(self.date_2)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_page_1.setText("")
        self.btn_page_2.setText("")
        self.btn_page_3.setText("")
        self.label.setText("")
        self.warningbtn.setText(QCoreApplication.translate("MainWindow", u"\u26a0Attention", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bienvenu", None))
        self.logoutbtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Notre application permettant la classification de la covid-19 via des images radiographiques", None))
        self.moreinfobtn.setText(QCoreApplication.translate("MainWindow", u"Plus d'information\n"
"", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notre application est une application desktop bas\u00e9e sur AI qui a pour but de classifier tout type ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"des images radiographiques relatives aux tests de covid-19,Preumonia et normal (non-infecter)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dataset:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"https://www.kaggle.com/tawsifurrahman/covid19-radiography-database", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"machine learning model:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"https://colab.research.google.com/drive/168cemZACIPJvefydgbjO15bvcCXCD2RX?usp=sharing", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u26a0Attention", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Vous ne pouvez pas le droit d'utiliser cette ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"application  pour des raisons m\u00e9dicales", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"car vous avez besoin beaucoup de donn\u00e9es", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"pour obtenir des r\u00e9sultats plus confiance.", None))
        self.closewframe.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.logoutbtn_2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"New Test", None))
        self.label_17.setText("")
        self.imag_cdr.setText(QCoreApplication.translate("MainWindow", u"import chest x-ray image", None))
        self.importbtn.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.label_18.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Les r\u00e9sultats", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Probabilit\u00e9:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9diction:", None))
        self.pred_label.setText(QCoreApplication.translate("MainWindow", u"-----------", None))
        self.proba_label.setText(QCoreApplication.translate("MainWindow", u"-----------", None))
        self.preditct_btn.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Sauvegarde", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"R\u00e9sultat \u00bb", None))
        self.addtest.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.cancelbtn.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.idtest.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Test", None))
        self.idclient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Client", None))
        self.nomprenon.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom Prenon", None))
        self.cinclient.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIN Client", None))
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path chest  x-ray image", None))
        self.prediresutt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Resultat", None))
        self.proba.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probabilit\u00e9", None))
        self.date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.logoutbtn_3.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Test", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID Client", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nom Prenon", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CIN Client", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Path", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resultat", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Probabilit\u00e9", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date de Test", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"15", None));
        self.videbtn.setText(QCoreApplication.translate("MainWindow", u"Vider ", None))
        self.editbtn.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.close_btn_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.idtest_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Test", None))
        self.deletebtn_3.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.deletebtn_4.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.close_btn_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.idtest_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Test", None))
        self.modibtn.setText(QCoreApplication.translate("MainWindow", u"modifier", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"R\u00e9sultat \u00bb", None))
        self.editbtnn.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.deletebtn_5.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.close_btn_4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.idtest_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Test", None))
        self.idclient_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Client", None))
        self.nomprenon_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nom Prenon", None))
        self.cinclient_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIN Client", None))
        self.path_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path chest  x-ray image", None))
        self.prediresutt_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Resultat", None))
        self.proba_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Probabilit\u00e9", None))
        self.date_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Date", None))
    # retranslateUi


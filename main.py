################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap
import sys 

# GUI FILE
login,_ = loadUiType('ui_main.ui')
class Login(QMainWindow , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.Btn_Toggle.clicked.connect(lambda: toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))

        # PAGE 2
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))

        # PAGE 3
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        def toggleMenu(self, maxWidth, enable):
            if enable:

                # GET WIDTH
                width = self.frame_left_menu.width()
                maxExtend = maxWidth
                standard = 70

                # SET MAX WIDTH
                if width == 70:
                    widthExtended = maxExtend
                else:
                    widthExtended = standard

                # ANIMATION
                self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
                self.animation.setDuration(400)
                self.animation.setStartValue(width)
                self.animation.setEndValue(widthExtended)
                self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animation.start()

def main():
        app= QApplication(sys.argv)
        window = Login()
        window.show()
        app.exec_()

if __name__ == '__main__':
    main()        


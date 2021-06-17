# PyQt5 libraries
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import MySQLdb
from PyQt5.uic import loadUiType
from PyQt5.QtGui import QPixmap
import sys ,res

login,_ = loadUiType('Loginpage.ui')
main,_ = loadUiType('ui_main.ui')

# Python libraries
import numpy as np
import datetime
import cv2
from PIL import  Image 
# Deep learning libraries
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow import keras
from keras.preprocessing.image import load_img
from keras.preprocessing import image

model = keras.models.load_model('covid19-2.h5')
classes = { 0:'Normal',
            1:'Preumonia', 
            2:'Covid',}
img_size=100

class Login(QMainWindow , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.loginbtn.clicked.connect(self.Handel_Login)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()

        username = self.username.text()
        password = self.password.text()

        sql = ''' SELECT * FROM user'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[1] and password == row[2]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()  
                             
            else:
                self.warning("failed","Email ou Mot de passe incorrect")
                
               

        
    def warning(self,title,warning):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(warning)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

class MainApp(QMainWindow , main):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.stackedWidget.setCurrentWidget(self.page_1)
        self.frame.hide()
        self.frame_2.hide()
        self.preditct_btn.hide()
        self.lineEdit.hide()
        self.resulatframe.hide()
        self.save_btn.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.resulatframe_2.hide()
        self.Show_All_Tests()

    def Handel_Buttons(self): 
        self.btn_page_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_page_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_page_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.logoutbtn.clicked.connect(self.logout)
        self.logoutbtn_3.clicked.connect(self.logout)
        self.logoutbtn_2.clicked.connect(self.logout)
        self.moreinfobtn.clicked.connect(self.info)
        self.warningbtn.clicked.connect(self.show_warning_message)
        self.closewframe.clicked.connect(self.hide_warning_message)
        self.importbtn.clicked.connect(self.getImage)
        self.preditct_btn.clicked.connect(self.classify)
        self.save_btn.clicked.connect(self.showsavepage)
        self.close_btn_2.clicked.connect(self.closeage1)
        self.deletebtn_4.clicked.connect(self.showdeletpage)
        self.deletebtn_3.clicked.connect(self.Delet_Test)
        self.addtest.clicked.connect(self.Add_New_Test)
        self.videbtn.clicked.connect(self.Vider)
        self.cancelbtn.clicked.connect(self.closesavepage)
        self.editbtn.clicked.connect(self.showmodpage)
        self.close_btn_3.clicked.connect(self.closeage2)
        self.modibtn.clicked.connect(self.showmod2page)
        self.modibtn.clicked.connect(self.show_data_modi_page)
        self.deletebtn_5.clicked.connect(self.closemod2page)
        self.editbtnn.clicked.connect(self.Edit_Test)
        self.close_btn_4.clicked.connect(self.closemod2page)
 ########################################
 ######### opening tabs #################
    def logout(self):
        self.window1 = Login()
        self.close()
        self.window1.show()

    def showsavepage(self):
        
        self.resulatframe.show() 
        lien=self.lineEdit.text()
        rst=self.pred_label.text()
        prbrest=self.proba_label.text()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        self.path.setText(lien)    
        self.prediresutt.setText(rst)
        self.date.setText(date)
        self.proba.setText(prbrest)
        self.idtest.setText('')
        self.idclient.setText('')
        self.nomprenon.setText('')
        self.cinclient.setText('')

    def show_warning_message(self):
        self.frame_2.show()

    def hide_warning_message(self):
        self.frame_2.hide()

    def closesavepage(self):
        self.resulatframe.hide()

    def closeage1(self):
        self.frame_4.hide()
       
    def showdeletpage(self):
        self.frame_4.show()

    def closeage2(self):
        self.frame_5.hide()
       
    def showmodpage(self):
        self.frame_5.show()

    def showmod2page(self):
        self.resulatframe_2.show()
        self.closeage2()

    def closemod2page(self):
        self.resulatframe_2.hide()
        
    def info(self): 
        self.label_7.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label_9.setTextInteractionFlags(Qt.TextSelectableByMouse)
        if self.moreinfobtn.text()=="Plus d'information":
            self.frame.show()
            self.moreinfobtn.setText("Moins d'information")
        else:
            self.frame.hide()
            self.moreinfobtn.setText("Plus d'information")

########################################          
############   Operation  ##############   
    def getImage(self):
            fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.jpeg *.png)")
            imagePath = fname[0]
            self.lineEdit.setText(imagePath)
            pixmap = QPixmap(imagePath)
            pixmap = pixmap.scaledToWidth(244)
            pixmap = pixmap.scaledToHeight(244)
            self.imag_cdr.setPixmap(QPixmap(pixmap))
            self.preditct_btn.show()


    def processing(self,image):
            
            image = np.array(image)
            if(image.ndim==3):
                    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            else :
                    gray=image
            gray=gray/255.
            resized=cv2.resize(gray,(img_size,img_size))
            reshape=resized.reshape(1,img_size,img_size)
            return reshape

    def classify(self):
            img_path=self.lineEdit.text()
            image = Image.open(img_path)
            image = self.processing(image)
            prediction = model.predict(image)
            result=np.argmax(prediction,axis=1)[0]
            accuracy=float(np.max(prediction,axis=1)[0])
            label=classes[result]
            self.pred_label.setText(label)
            proba = str(round(accuracy*100, 2))+'%'
            self.proba_label.setText(proba)
            self.save_btn.show()
    
    def Add_New_Test(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()
        idtest=self.idtest.text()     
        idClient=self.idclient.text()
        NomPrenom=self.nomprenon.text()
        CINClient=self.cinclient.text()
        lien=self.path.text()
        Resultat=self.prediresutt.text()
        ProbaResult=self.proba.text()
        Date=self.date.text()
        self.cur.execute('''
            INSERT INTO resultat(ID_Test,ID_Client,Nom_Prenon,CIN_Client,path,Resultat,ProbabilitéResResult,Date)
            VALUES (%s , %s , %s , %s , %s , %s ,%s , %s  )
        ''' ,(idtest,idClient,NomPrenom,CINClient,lien,Resultat,ProbaResult,Date))
        self.db.commit()
        self.statusBar().showMessage('Test ajouté')
        self.Show_All_Tests()
        self.closesavepage()

    def show_data_modi_page(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()

        idtest1=self.idtest_3.text()
        self.cur.execute(''' SELECT ID_Test,ID_Client,Nom_Prenon,CIN_Client,path,Resultat,ProbabilitéResResult,Date FROM resultat WHERE ID_Test = %s  ''',(idtest1))
        data = self.cur.fetchone()
        self.idtest_4.setText(str(data[0]))     
        self.idclient_2.setText(str(data[1]))
        self.nomprenon_2.setText(str(data[2]))
        self.cinclient_2.setText(str(data[3]))
        self.path_2.setText(str(data[4]))
        self.prediresutt_2.setText(str(data[5]))
        self.proba_2.setText(str(data[6]))
        self.date_2.setText(str(data[7]))
    def Edit_Test(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()
        idtest=self.idtest_4.text()     
        idClient=self.idclient_2.text()
        NomPrenom=self.nomprenon_2.text()
        CINClient=self.cinclient_2.text()
        lien=self.path_2.text()
        Resultat=self.prediresutt_2.text()
        ProbaResult=self.proba_2.text()
        Date=self.date_2.text()
        self.cur.execute('''
            UPDATE resultat SET ID_Test=%s ,ID_Client=%s ,Nom_Prenon=%s ,CIN_Client=%s ,path=%s ,Resultat=%s ,ProbabilitéResResult=%s ,Date=%s WHERE ID_Test = %s            
        ''', (idtest,idClient,NomPrenom,CINClient,lien,Resultat,ProbaResult,Date,idtest)) 
        self.db.commit()
        self.statusBar().showMessage('Test ajouté')
        self.Show_All_Tests()

        self.idtest_4.setText('')    
        self.idclient_2.setText('')
        self.nomprenon_2.setText('')
        self.cinclient_2.setText('')
        self.path_2.setText('')
        self.prediresutt_2.setText('')
        self.proba_2.setText('')
        self.date_2.setText('')
        self.showmod2page()
    def Delet_Test(self):    
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()

        idtest=self.idtest_2.text()
        warning = QMessageBox.warning(self , 'Supprimer le test' , "Voulez-vous vraiment supprimer ce test?" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM resultat WHERE ID_Test = %s '''
            self.cur.execute(sql , [(idtest)])
            self.db.commit()
            self.statusBar().showMessage('Test bien supprimé')
            self.Show_All_Tests()
        self.closeage1()

    def Show_All_Tests(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()  

        self.cur.execute(''' SELECT ID_Test,ID_Client,Nom_Prenon,CIN_Client,path,Resultat,ProbabilitéResResult,Date  FROM resultat''')
        data = self.cur.fetchall()

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.db.close()   

    def Vider(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='' , db='app')
        self.cur = self.db.cursor()

        warning = QMessageBox.warning(self , 'Vider le tableau' , "Voulez-vous vraiment vider ce tableau ?" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            self.cur.execute(''' TRUNCATE TABLE resultat ''')
            self.db.commit()
            self.statusBar().showMessage('Tableau bien vidé')
            self.Show_All_Tests()
    
        
    
def main():
        app= QApplication(sys.argv)
        window = Login()
        window.show()
        app.exec_()

if __name__ == '__main__':
    main()        

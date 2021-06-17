#Pyrcc5 input_file.qrc -o icons.py

# PyQt5 libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType
import sys
from PyQt5.QtGui import QPixmap

# Python libraries
import os
import numpy as np
import pandas as pd 
import random
import cv2
import matplotlib.pyplot as plt
import datetime 
from xlrd import *
from xlsxwriter import *


# Deep learning libraries
import keras.backend as K
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import tensorflow as tf
 



ui,_ = loadUiType('Projet.ui')
login,_ = loadUiType('Login.ui')

class Login(QMainWindow , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_Login)
        self.label.setVisible(False)

    def Handel_Login(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM user'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data  :
            if username == row[4] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.show()
                self.label.setText('Email ou Mot de passe incorrect')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = "System_DL"
        self.setupUi(self)
        self.Handel_Buttons()
        self.tabWidget.tabBar().setVisible(False)
        self.frame_3.hide()
        self.Go_To_Home()
        self.affichage()
        self.Show_All_Tests()
        self.Show_All_His()

        

    def Handel_Buttons(self): 

        self.pushButton_8.clicked.connect(self.Open_Entr_Tab)
        self.pushButton_9.clicked.connect(self.Open_FFT_Tab)
        self.pushButton_10.clicked.connect(self.Open_Test_Tab)
        self.pushButton_12.clicked.connect(self.Open_Histor_Tab)
        self.pushButton_11.clicked.connect(self.Open_Resultat_Tab)

        self.pushButton_6.clicked.connect(self.getImage)   
        self.pushButton_2.clicked.connect(self.getrep)
        self.pushButton_4.clicked.connect(self.getImageFFT)
        self.pushButton.clicked.connect(self.creer_mod)
        self.pushButton_3.clicked.connect(self.save_mod)
        self.pushButton_5.clicked.connect(self.con_fft)
        self.pushButton_7.clicked.connect(self.executer)

        self.pushButton_13.clicked.connect(self.Go_To_Home)
        self.pushButton_14.clicked.connect(self.Go_To_Home)
        self.pushButton_15.clicked.connect(self.Go_To_Home)
        self.pushButton_16.clicked.connect(self.Go_To_Home)
        self.pushButton_17.clicked.connect(self.Go_To_Home)
        
        self.pushButton_18.clicked.connect(self.Save)
        self.pushButton_25.clicked.connect(self.Open_Frame)
        self.pushButton_27.clicked.connect(self.Open_Frame)
        self.pushButton_24.clicked.connect(self.Close_Frame)
        self.pushButton_26.clicked.connect(self.logout)

        self.pushButton_21.clicked.connect(self.Add_New_Test)
        self.pushButton_20.clicked.connect(self.Show_All_Tests)
        self.pushButton_19.clicked.connect(self.Show_Test_By_id)
        self.pushButton_23.clicked.connect(self.Edit_Test)
        self.pushButton_22.clicked.connect(self.Delet_Test)
        self.pushButton_32.clicked.connect(self.Show_His_By_date)
        self.pushButton_33.clicked.connect(self.Show_All_His)
        self.pushButton_44.clicked.connect(self.Vider)
        self.pushButton_42.clicked.connect(self.Export_Tests)
        self.pushButton_43.clicked.connect(self.Export_his)


    ########################################
    ######### opening tabs #################
    def Open_Entr_Tab(self):
        self.tabWidget.show()
        self.tabWidget.setCurrentIndex(0)

    def Open_FFT_Tab(self):
        self.tabWidget.show()
        self.tabWidget.setCurrentIndex(1)

    def Open_Test_Tab(self):
        self.tabWidget.show()
        self.tabWidget.setCurrentIndex(2)

    def Open_Histor_Tab(self):
        self.tabWidget.show()
        self.tabWidget.setCurrentIndex(4)

    def Open_Resultat_Tab(self):
        self.tabWidget.show()
        self.tabWidget.setCurrentIndex(3)  

    def Open_Frame(self):
        self.frame_3.show()  

    def Close_Frame(self):
        self.frame_3.hide()    

    def Go_To_Home(self):
        self.Close_Frame()
        self.tabWidget.hide()

    def logout(self):
        self.window1 = Login()
        self.close()
        self.window1.show()    

    def Save(self):
        self.Open_Frame()
        lien=self.lineEdit_4.text()
        rst=self.lineEdit_6.text()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")

        self.lineEdit_11.setText(lien)    
        self.lineEdit_12.setText(rst)
        self.lineEdit_13.setText(date)
    ########################################          
    ######### DL Operation #################    

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.jpeg)")
        imagePath = fname[0]
        self.lineEdit_4.setText(imagePath)
        pixmap = QPixmap(imagePath)
        
        pixmap = pixmap.scaledToWidth(361)
        pixmap = pixmap.scaledToHeight(291)

        self.label_7.setPixmap(QPixmap(pixmap))

    def getImageFFT(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.gif *.jpeg)")
        imagePath = fname[0]
        print(imagePath)
        self.lineEdit_2.setText(imagePath)
        pixmap = QPixmap(imagePath)
        
        pixmap = pixmap.scaledToWidth(191)
        pixmap = pixmap.scaledToHeight(181)

        self.label.setPixmap(QPixmap(pixmap))

        img = cv2.imread(imagePath,0)
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        #af='EnFFT.jpg'
        #cv2.imwrite(af,magnitude_spectrum)

        pixmap = QPixmap("C:\\Users\\pc\\Documents\\Deep_learning\\PFE_2020\\single_pr\\EnFFT.jpg")
        pixmap = pixmap.scaledToWidth(191)
        pixmap = pixmap.scaledToHeight(181)
        self.label_14.setPixmap(QPixmap(pixmap))
        print("ok")    

    def getrep(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "All File (*.*)")
        imagePath = fname[0]
        self.lineEdit_5.setText(imagePath)
        pixmap = QPixmap(imagePath)
        #self.label_7.setPixmap(QPixmap(pixmap))    

    def affichage(self):
        imagePath = 'img_form/backg.jpg'
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToWidth(771)
        pixmap = pixmap.scaledToHeight(471)
        self.label_18.setPixmap(QPixmap(pixmap))
    

    def creer_mod(self):

        input_path = "./chest_xray/chest_xray/"
        #input_path = self.lineEdit_5.text()
        text='  '
        for _set in ['train', 'val', 'test']:

            n_normal = len(os.listdir(input_path + _set + '/NORMAL'))
            n_infect = len(os.listdir(input_path + _set + '/PNEUMONIA'))
            text=text+'   Set: {}, normal images: {}, pneumonia images: {}.   '.format(_set, n_normal, n_infect)                 
            #print(text)
        self.textEdit.setText(text) 

        def process_data(img_dims, batch_size):
            # Data generation objects
            train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.3, vertical_flip=True)
            test_val_datagen = ImageDataGenerator(rescale=1./255)
    
            # This is fed to the network in the specified batch sizes and image dimensions
            train_gen = train_datagen.flow_from_directory(
            directory=input_path+'train', 
            target_size=(img_dims, img_dims), 
            batch_size=batch_size, 
            class_mode='binary', 
            shuffle=True)

            test_gen = test_val_datagen.flow_from_directory(
            directory=input_path+'test', 
            target_size=(img_dims, img_dims), 
            batch_size=batch_size, 
            class_mode='binary', 
            shuffle=True)
    
            # I will be making predictions off of the test set in one batch size
            # This is useful to be able to get the confusion matrix
            test_data = []
            test_labels = []

            for cond in ['/NORMAL/', '/PNEUMONIA/']:
                for img in (os.listdir(input_path + 'test' + cond)):
                    img = plt.imread(input_path+'test'+cond+img)
                    img = cv2.resize(img, (img_dims, img_dims))
                    img = np.dstack([img, img, img])
                    img = img.astype('float32') / 255
                    if cond=='/NORMAL/':
                        label = 0
                    elif cond=='/PNEUMONIA/':
                        label = 1
                    test_data.append(img)
                    test_labels.append(label)
        
            test_data = np.array(test_data)
            test_labels = np.array(test_labels)
            return train_gen, test_gen, test_data, test_labels  

        img_dims = 150
        epochs = 10
        batch_size = 32

        # Getting the data
        train_gen, test_gen, test_data, test_labels = process_data(img_dims, batch_size)

        # Input layer
        inputs = Input(shape=(img_dims, img_dims, 3))

        x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(inputs)
        x = Conv2D(filters=16, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Second conv block
        x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Third conv block
        x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)

        # Fourth conv block
        x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)
        x = Dropout(rate=0.2)(x)

        # Fifth conv block
        x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = SeparableConv2D(filters=256, kernel_size=(3, 3), activation='relu', padding='same')(x)
        x = BatchNormalization()(x)
        x = MaxPool2D(pool_size=(2, 2))(x)
        x = Dropout(rate=0.2)(x)

        # FC layer
        x = Flatten()(x)
        x = Dense(units=512, activation='relu')(x)
        x = Dropout(rate=0.7)(x)
        x = Dense(units=128, activation='relu')(x)
        x = Dropout(rate=0.5)(x)
        x = Dense(units=64, activation='relu')(x)
        x = Dropout(rate=0.3)(x)

        # Output layer
        output = Dense(units=1, activation='sigmoid')(x)

        # Creating model and compiling
        model = Model(inputs=inputs, outputs=output)
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Callbacks
        checkpoint = ModelCheckpoint(filepath='best_weights.hdf5', save_best_only=True, save_weights_only=True)
        lr_reduce = ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=2, verbose=2, mode='max')
        early_stop = EarlyStopping(monitor='val_loss', min_delta=0.1, patience=1, mode='min')

        hist = model.fit_generator(
           train_gen, steps_per_epoch=train_gen.samples // batch_size, 
           epochs=epochs, validation_data=test_gen, 
           validation_steps=test_gen.samples // batch_size, callbacks=[checkpoint, lr_reduce])

        from sklearn.metrics import accuracy_score, confusion_matrix

        preds = model.predict(test_data)

        acc = accuracy_score(test_labels, np.round(preds))*100
        cm = confusion_matrix(test_labels, np.round(preds))
        tn, fp, fn, tp = cm.ravel()

        print('CONFUSION MATRIX ------------------')
        print(cm)

        print('\nTEST METRICS ----------------------')
        precision = tp/(tp+fp)*100
        recall = tp/(tp+fn)*100
        print('Accuracy: {}%'.format(acc))
        print('Precision: {}%'.format(precision))
        print('Recall: {}%'.format(recall))
        print('F1-score: {}'.format(2*precision*recall/(precision+recall)))

        print('\nTRAIN METRIC ----------------------')
        print('Train acc: {}'.format(np.round((hist.history['accuracy'][-1])*100, 2)))




    def save_mod(self):
        name = self.lineEdit.text()
        name ='model/' +name +'.h5'
        print(name)
        model.save(name)

    def con_fft(self):
        #path="C:/Users/pc/Documents/Deep_learning/PFE_2020/single_pr"
        #self.loading()
        path=self.lineEdit_2.text()
        dir=self.lineEdit_3.text()
        os.mkdir(dir)
        print("directory has created")
        for x in os.listdir(path):
            #p=os.path.abspath(x)
            p=path+'/'+x
            print(x)
            img = cv2.imread(p,0)
            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20*np.log(np.abs(fshift))
            #af=x+'EnFFT.jpg'
            af=dir+'/'+x
            cv2.imwrite(af,magnitude_spectrum)
        print("ok") 
        self.label_18.hide()   



    def executer(self):
        import numpy as np
        from keras.preprocessing import image
        import matplotlib.pyplot as plt
        from keras.models import load_model

        img_width=150
        img_height=150

        #img_path='single_pr/normal.jpeg' #change to location of chest x-ray
        img_path=self.lineEdit_4.text()
        
        if self.comboBox_4.currentText()=='En FFT':
            img = cv2.imread(img_path,0)
            f = np.fft.fft2(img)
            fshift = np.fft.fftshift(f)
            magnitude_spectrum = 20*np.log(np.abs(fshift))
            #af=x+'EnFFT.jpg'
            af='jfj/TestEnFFT.jpg'
            cv2.imwrite(af,magnitude_spectrum)

            img = image.load_img(af, target_size=(img_width, img_height))

            self.lineEdit_6.setText('Loading....')

            mdl='model/'+self.comboBox_3.currentText()
            model=load_model(mdl)
            img = image.img_to_array(img)
            x = np.expand_dims(img, axis=0) * 1./255
            score = model.predict(x)
            if score < 0.5:
                res='Normal'
            else:
                res='Pneumonia'
            if res=='Normal':
                score=1-score    
        
            print('Predicted:', score ,' ', res)
            score=score*100
            rlt=res +' WITH ' 'Predicted is : ' + str(score)  
            self.lineEdit_6.setText(rlt)    

        ################################
        else:

            img = image.load_img(img_path, target_size=(img_width, img_height))


            self.lineEdit_6.setText('Loading....')

            mdl='model/'+self.comboBox_3.currentText()
            model=load_model(mdl)
            img = image.img_to_array(img)
            x = np.expand_dims(img, axis=0) * 1./255
            score = model.predict(x)
            if score < 0.5:
                res='Normal'
            else:
                res='Pneumonia'
            if res=='Normal':
                score=1-score    
        
            print('Predicted:', score ,' ', res)
            score=score*100
            rlt=res +' WITH ' 'Predicted is : ' + str(score)  
            self.lineEdit_6.setText(rlt)                

    ########################################          
    ######### Test Management ##############
    
    def Add_New_Test(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()


        idClient=self.lineEdit_8.text()
        NomPrenom=self.lineEdit_9.text()
        CINClient=self.lineEdit_10.text()
        lien=self.lineEdit_11.text()
        Resultat=self.lineEdit_12.text()
        Date=self.lineEdit_13.text()
        Type=self.comboBox_4.currentText()
        Model=self.comboBox_3.currentText()

        self.cur.execute('''
            INSERT INTO test(idClient,NomPrenom,CINClient,lien,Resultat,Date,Type,Model)
            VALUES (%s , %s , %s , %s , %s , %s , %s , %s )
        ''' ,(idClient,NomPrenom,CINClient,lien,Resultat,Date,Type,Model))

        self.db.commit()
        self.statusBar().showMessage('Test bien ajouté')
        self.Show_All_Tests()

        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')


    def Show_All_Tests(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()  

        self.cur.execute(''' SELECT idtest,idClient,NomPrenom,CINClient,lien,Resultat,Date,Type,Model  FROM test''')
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


    def Show_Test_By_id(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()
        
        id=self.lineEdit_7.text()
        self.cur.execute(''' SELECT idtest,idClient,NomPrenom,CINClient,lien,Resultat,Date FROM test WHERE idClient = %s or NomPrenom = %s or CINClient = %s or Date = %s ''',(id,id,id,id))
 
        data = self.cur.fetchone()

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)
        
        self.frame_3.show()

        self.lineEdit_14.setText(str(data[0]))
        self.lineEdit_8.setText(data[1])
        self.lineEdit_9.setText(data[2])
        self.lineEdit_10.setText(data[3])
        self.lineEdit_11.setText(data[4])
        self.lineEdit_12.setText(data[5])
        self.lineEdit_13.setText(data[6])

        self.cur.execute(''' SELECT idtest,idClient,NomPrenom,CINClient,lien,Resultat,Date,Type,Model FROM test WHERE idClient = %s or NomPrenom = %s or CINClient = %s ''',(id,id,id))
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


    def Edit_Test(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        idtest=self.lineEdit_14.text()
        idClient=self.lineEdit_8.text()
        NomPrenom=self.lineEdit_9.text()
        CINClient=self.lineEdit_10.text()
        lien=self.lineEdit_11.text()
        Resultat=self.lineEdit_12.text()
        Date=self.lineEdit_13.text()

        self.cur.execute('''
            UPDATE test SET idtest=%s ,idClient=%s ,NomPrenom=%s ,CINClient=%s ,lien=%s ,Resultat=%s ,Date=%s WHERE idtest = %s            
        ''', (idtest,idClient,NomPrenom,CINClient,lien,Resultat , Date, idtest))    

        self.db.commit()
        self.statusBar().showMessage('Test bien modifié')  
        self.Show_All_Tests()

        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')

    def Delet_Test(self):    
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        idtest=self.lineEdit_14.text()
        warning = QMessageBox.warning(self , 'Supprimer le test' , "Voulez-vous vraiment supprimer ce test?" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM test WHERE idtest = %s '''
            self.cur.execute(sql , [(idtest)])
            self.db.commit()
            self.statusBar().showMessage('Test bien supprimé')
            self.Show_All_Tests()
        self.Close_Frame()

    ########################################          
    ######### Histoire Management ##########
     
    def Add_New_His(self):
        pass

    def Show_All_His(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT *  FROM historique ''')
        data = self.cur.fetchall()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.db.close() 

    def Show_His_By_date(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        id=self.lineEdit_16.text()
        
        self.cur.execute(''' SELECT *  FROM historique WHERE date = %s or id = %s ''' , (id,id))
        data = self.cur.fetchall()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.db.close() 

    def Vider(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='root' , db='hospital')
        self.cur = self.db.cursor()

        warning = QMessageBox.warning(self , 'Vider le tableau' , "Voulez-vous vraiment vider ce tableau ?" , QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            self.cur.execute(''' TRUNCATE TABLE test ''')
            self.db.commit()
            self.statusBar().showMessage('Tableau bien vidé')


    ########################################
    ######### Export Data #################

    def Export_Tests(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT idClient,NomPrenom,CINClient,lien,Resultat,Date,Type,Model FROM test''')
        data = self.cur.fetchall()

        wb = Workbook('all_tests.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'id Client')
        sheet1.write(0,1 , 'Nom Prenom')
        sheet1.write(0,2 , 'CIN Client')
        sheet1.write(0,3 , 'Lien')
        sheet1.write(0,4 , 'Resultat')
        sheet1.write(0,5 , 'Date')
        sheet1.write(0,6 , 'Type')
        sheet1.write(0,7 , 'Model')

        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Rapport de test creé avec succès')            

    def Export_his(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='root', db='hospital')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT *  FROM historique ''')
        data = self.cur.fetchall()

        wb = Workbook('all_Historique.xlsx')
        sheet1 = wb.add_worksheet()

        sheet1.write(0,0 , 'id ')
        sheet1.write(0,1 , 'Opération')
        sheet1.write(0,2 , 'Date')
 

        row_number = 1
        for row in data :
            column_number = 0
            for item in row :
                sheet1.write(row_number , column_number , str(item))
                column_number += 1
            row_number += 1

        wb.close()
        self.statusBar().showMessage('Rapport de Historique creé avec succès')



def main():
        app= QApplication(sys.argv)
        window = Login()
        window.show()
        app.exec_()

if __name__ == '__main__':
    main()        

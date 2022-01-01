from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
from ui_mainwindow import Ui_MainWindow

import re

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.right_image = QPixmap('img/right.jpg')
        self.wrong_image = QPixmap('img/wrong.jpg')

        #Slots Connections
        self.ui.ipLE.textChanged.connect(self.enable_ip_bt)
        self.ui.macLE.textChanged.connect(self.enable_mac_bt)
        self.ui.timeLE.textChanged.connect(self.enable_time_bt)
        self.ui.emailLE.textChanged.connect(self.enable_email_bt)
        self.ui.floatLE.textChanged.connect(self.enable_float_bt)
        self.ui.dateLE.textChanged.connect(self.enable_date_bt)

        self.ui.validateIpBT.clicked.connect(self.validate_ip_address)
        self.ui.validateMacBT.clicked.connect(self.validate_mac_address)
        self.ui.validateTimeBT.clicked.connect(self.validate_time)
        self.ui.validateEmailBT.clicked.connect(self.validate_email)
        self.ui.validateFloatBT.clicked.connect(self.validate_float)
        self.ui.validateDateBT.clicked.connect(self.validate_date)
    
    @pyqtSlot()
    def enable_ip_bt(self):
        self.ui.ipPM.clear()
        if self.ui.ipLE.text():
            self.ui.validateIpBT.setEnabled(True)
        else:
            self.ui.validateIpBT.setEnabled(False)
    
    @pyqtSlot()
    def enable_mac_bt(self):
        self.ui.macPM.clear()
        if self.ui.macLE.text():
            self.ui.validateMacBT.setEnabled(True)
        else:
            self.ui.validateMacBT.setEnabled(False)
    
    @pyqtSlot()
    def enable_time_bt(self):
        self.ui.timePM.clear()
        if self.ui.timeLE.text():
            self.ui.validateTimeBT.setEnabled(True)
        else:
            self.ui.validateTimeBT.setEnabled(False)
    
    @pyqtSlot()
    def enable_email_bt(self):
        self.ui.emailPM.clear()
        if self.ui.emailLE.text():
            self.ui.validateEmailBT.setEnabled(True)
        else:
            self.ui.validateEmailBT.setEnabled(False)
    
    @pyqtSlot()
    def enable_float_bt(self):
        self.ui.floatPM.clear()
        if self.ui.floatLE.text():
            self.ui.validateFloatBT.setEnabled(True)
        else:
            self.ui.validateFloatBT.setEnabled(False)
    
    @pyqtSlot()
    def enable_date_bt(self):
        self.ui.datePM.clear()
        if self.ui.dateLE.text():
            self.ui.validateDateBT.setEnabled(True)
        else:
            self.ui.validateDateBT.setEnabled(False)
    
    def validate_ip_address(self):
        text = self.ui.ipLE.text()
        match = re.search("^(((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]?))\\.){3}((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]?))$", text)
        if match:
            self.ui.ipPM.setPixmap(self.right_image)
        else:
            self.ui.ipPM.setPixmap(self.wrong_image)

    def validate_mac_address(self):
        text = self.ui.macLE.text()
        match = re.search("^(([0-9A-F]|[0-9a-f]){2}[:-]){5}([0-9A-F]|[0-9a-f]){2}$", text)
        if match:
            self.ui.macPM.setPixmap(self.right_image)
        else:
            self.ui.macPM.setPixmap(self.wrong_image)
    
    def validate_time(self):
        text = self.ui.timeLE.text()
        match = re.search("^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$", text)
        if match:
            self.ui.timePM.setPixmap(self.right_image)
        else:
            self.ui.timePM.setPixmap(self.wrong_image)
    
    def validate_email(self):
        text = self.ui.emailLE.text()
        match = re.search("^([0-9a-zA-Z-_]\\.?)+@[0-9a-zA-Z]+(\\.[0-9a-zA-Z]{2,3})+$", text)
        if match:
            self.ui.emailPM.setPixmap(self.right_image)
        else:
            self.ui.emailPM.setPixmap(self.wrong_image)
    
    def validate_float(self):
        text = self.ui.floatLE.text()
        match = re.search("^[0-9]*\\.[0-9]+$", text)
        if match:
            self.ui.floatPM.setPixmap(self.right_image)
        else:
            self.ui.floatPM.setPixmap(self.wrong_image)

    def validate_date(self):
        text = self.ui.dateLE.text()
        match = re.search("^((31[/](0?[13578]|1[02]))|((29|30)[/](0?[13-9]|1[0-2])))[/]((\\d\\d\\d\\d))$|^((2[89][/](0?2)[/](\\d\\d\\d\\d)))$|^(0?[0-9]|1[0-9]|2[0-8])[/](0?[1-9]|1[0-2])[/](\\d?\\d?\\d?\\d)$", text)
        if match:
            self.ui.datePM.setPixmap(self.right_image)
        else:
            self.ui.datePM.setPixmap(self.wrong_image)


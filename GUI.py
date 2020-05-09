

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
import time
from ScanProcess.ScanFile import *
from ScanProcess.ScanURL import *

############
class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()

        self.Form = Form
        self.count=0
        #SetupBackground
        # self.Form = QtWidgets.QWidget()
        # Back_color = QtGui.QPalette()
        #
        # gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        # gradient.setColorAt(1.0, QtGui.QColor(6, 57, 84, 60))
        # gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        #
        # Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        # self.Form.setPalette(Back_color)
        #set plain text
        self.ABOUT_ME = QtWidgets.QPlainTextEdit(self.Form)
        self.ABOUT_ME.setGeometry(QtCore.QRect(0, 0, 0, 0))
        #
        #
        #setupsize
        self.Form.setObjectName("Form")
        self.Form.resize(1000, 600)
        self.Form.setMinimumSize(QtCore.QSize(1000, 600))
        self.Form.setMaximumSize(QtCore.QSize(1000, 600))
        #Idont wanna set lay out so i dicided to lock this
        #set window icon
        # self.ABOUT_ME = QtWidgets.QPlainTextEdit(self.Form)
        #self.ABOUT_ME.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.ABOUT_ME.setObjectName("ABOUT_ME")
        # self.ABOUT_ME.setGeometry(QtCore.QRect(0, 0, 0, 0))
        #set out put file scan
        self.OUT_PUT_FileScan = QtWidgets.QPlainTextEdit(self.Form)
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.OUT_PUT_FileScan.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.OUT_PUT_FileScan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.OUT_PUT_FileScan.setTabChangesFocus(False)
        self.OUT_PUT_FileScan.setReadOnly(True)
        self.OUT_PUT_FileScan.setObjectName("OUT_PUT_FileScan")
        ####
        self.OUT_PUT_URL = QtWidgets.QPlainTextEdit(self.Form)
        self.OUT_PUT_URL.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.OUT_PUT_URL.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.OUT_PUT_URL.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.OUT_PUT_URL.setTabChangesFocus(False)
        self.OUT_PUT_URL.setReadOnly(True)
        self.OUT_PUT_URL.setObjectName("OUT_PUT_URL")
        ####

        #Set up File scan ui

        self.CHOOSE_FILE = QtWidgets.QPushButton(self.Form)
        self.CHOOSE_FILE.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.CHOOSE_FILE.clicked.connect(self.openFileNameDialog)
        ##set up button scan with file name
        ### create layout
        self.widget_File_scan = QtWidgets.QWidget(self.Form)
        self.widget_File_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.widget_File_scan.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_File_scan)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.File_CHOOSE_EDIT = QtWidgets.QLineEdit(self.widget_File_scan)
        self.File_CHOOSE_EDIT.setObjectName("File_CHOOSE_EDIT")
        self.horizontalLayout.addWidget(self.File_CHOOSE_EDIT)
        self.Scan_FILE_Button = QtWidgets.QPushButton(self.widget_File_scan)
        self.Scan_FILE_Button.setStyleSheet("background-color:#dddddd;")
        self.Scan_FILE_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon/Scan.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Scan_FILE_Button.setIcon(icon4)
        self.Scan_FILE_Button.setIconSize(QtCore.QSize(45, 21))
        self.Scan_FILE_Button.setObjectName("Scan_FILE_Button")
        self.horizontalLayout.addWidget(self.Scan_FILE_Button)
        ##########set url scan


        self.widget_URl_scan = QtWidgets.QWidget(self.Form)
        self.widget_URl_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.widget_URl_scan.setObjectName("widget2")

        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.widget_URl_scan)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        self.URL_EDIT = QtWidgets.QLineEdit(self.widget_URl_scan)
        self.URL_EDIT.setObjectName("URL_EDIT")
        self.horizontalLayout2.addWidget(self.URL_EDIT)
        self.Scan_URL_Button = QtWidgets.QPushButton(self.widget_URl_scan)
        self.Scan_URL_Button.setStyleSheet("background-color:#dddddd;")
        self.Scan_URL_Button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon/Url2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Scan_URL_Button.setIcon(icon5)
        self.Scan_URL_Button.setIconSize(QtCore.QSize(45, 21))
        self.Scan_URL_Button.setObjectName("Scan_URL_Button")
        self.horizontalLayout2.addWidget(self.Scan_URL_Button)
        ####
        self.Scan_URL_Button.setAutoDefault(True)
        self.URL_EDIT.returnPressed.connect(self.ScanURL_Process)



        ##connect to SanFile_Proccess()
        self.Scan_FILE_Button.clicked.connect(self.SanFile_Proccess)

        #
        self.frame = QtWidgets.QFrame(self.Form)
        self.frame.setGeometry(QtCore.QRect(-80, -130, 134, 591))
        self.frame.setStyleSheet("background-color: #274472;border-radius: 60px; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(80, 170, 54, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BUTTON_HOME = QtWidgets.QPushButton(self.widget)
        self.BUTTON_HOME.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUTTON_HOME.setStyleSheet("border-style: outset; border-width: 0px; border-radius: 15px;border-color: black;padding: 4px;")
        self.BUTTON_HOME.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BUTTON_HOME.setIcon(icon)
        self.BUTTON_HOME.setIconSize(QtCore.QSize(40, 40))
        self.BUTTON_HOME.setObjectName("BUTTON_HOME")
        self.verticalLayout.addWidget(self.BUTTON_HOME)
        self.BUTTON_FILE_SCAN = QtWidgets.QPushButton(self.widget)
        self.BUTTON_FILE_SCAN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUTTON_FILE_SCAN.setStyleSheet("border-style: outset;border-width: 0px;border-radius: 15px;border-color: black;padding: 4px;")
        self.BUTTON_FILE_SCAN.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BUTTON_FILE_SCAN.setIcon(icon1)
        self.BUTTON_FILE_SCAN.setIconSize(QtCore.QSize(40, 40))
        self.BUTTON_FILE_SCAN.setObjectName("BUTTON_FILE_SCAN")
        self.verticalLayout.addWidget(self.BUTTON_FILE_SCAN)
        self.BUTTON_URL_SCAN = QtWidgets.QPushButton(self.widget)
        self.BUTTON_URL_SCAN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUTTON_URL_SCAN.setStyleSheet("border-style: outset;border-width: 0px;border-radius: 15px;border-color: black;padding: 4px;")
        self.BUTTON_URL_SCAN.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon/Url2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BUTTON_URL_SCAN.setIcon(icon2)
        self.BUTTON_URL_SCAN.setIconSize(QtCore.QSize(40, 40))
        self.BUTTON_URL_SCAN.setObjectName("BUTTON_URL_SCAN")
        self.verticalLayout.addWidget(self.BUTTON_URL_SCAN)
        self.BUTTON_HELP = QtWidgets.QPushButton(self.widget)
        self.BUTTON_HELP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUTTON_HELP.setStyleSheet("border-style: outset;border-width: 0px;border-radius: 15px;border-color: black;padding: 4px;")
        self.BUTTON_HELP.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BUTTON_HELP.setIcon(icon3)
        self.BUTTON_HELP.setIconSize(QtCore.QSize(40, 40))
        self.BUTTON_HELP.setObjectName("BUTTON_HELP")
        self.verticalLayout.addWidget(self.BUTTON_HELP)
        self.frame_2 = QtWidgets.QFrame(self.Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 581, 1001, 30))
        self.frame_2.setStyleSheet("background-color: #9da993;border-width: 0px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.BUTTON_HOME.clicked.connect(self.on_click_Home)
        self.BUTTON_FILE_SCAN.clicked.connect(self.on_click_File)
        self.BUTTON_URL_SCAN.clicked.connect(self.on_click_Url)
        self.BUTTON_HELP.clicked.connect(self.on_click_About)
        self.Label_HELLO = QtWidgets.QLabel(self.Form)
        self.Label_HELLO.setGeometry(QtCore.QRect(400, 100, 400, 120))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(238, 238, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        self.Label_HELLO.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Label_HELLO.setFont(font)
        self.Label_HELLO.setObjectName("Label_HELLO")
        self.Label_HELLO.setText('HELLO !!')
        Back_color = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        gradient.setColorAt(1.0, QtGui.QColor(6, 57, 84, 60))
        gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        self.Form.setPalette(Back_color)
        self.Scan_URL_Button.clicked.connect(self.ScanURL_Process)
        self.URL_EDIT.setPlaceholderText("Type your URl here...")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.Form)

        self.Form.show()
    def Animation_OUTPUT_URL(self):
        self.OUT_PUT_URL.setGeometry(QtCore.QRect(290, 300, 541, 210))
        self.URL_Out_animation = QtCore.QPropertyAnimation(self.OUT_PUT_URL, b"geometry")
        self.URL_Out_animation.setDuration(300)
        self.URL_Out_animation.setStartValue(QtCore.QRect(290, 300, 541, 0))
        self.URL_Out_animation.setEndValue(QtCore.QRect(290, 300, 541, 210))
        self.URL_Out_animation.start()


    def ScanURL_Process(self):
        #print('im here')
        Url_input =self.URL_EDIT.text()
        self.URL_EDIT.clear()
        #print(Url_input)
        if Url_input=="":
            QtWidgets.QMessageBox.question(self, 'Message', 'Enter a URL please', QtWidgets.QMessageBox.Yes)

        else:
            self.Animation_OUTPUT_URL()
            self.OUT_PUT_URL.insertPlainText("Checking {} ....\n".format(Url_input))
            self.ScanURL_PROCESSSSSS(Url_input)
    def ScanURL_PROCESSSSSS(self, Url):
        A = ScanURL(Url)
        #print(Url)
        status_code =A.status_code
        #print(status_code)
        if status_code==200:
            count_malicious=0
            self.OUT_PUT_URL.insertPlainText('Status Code: 200\nPrepare for Scaning URL....\nScaning......\n')
            A.Scan()
            B=A.dat
            #print(B)
            if B !={}:
                for i in B:
                    if B[i]['result']!='clean':
                        if B[i]['result']!='unrated':
                            count_malicious+=1

                    C = B[i]['result']
                    self.OUT_PUT_URL.insertPlainText(i)
                    self.OUT_PUT_URL.insertPlainText(': ')
                    self.OUT_PUT_URL.insertPlainText(C)
                    self.OUT_PUT_URL.insertPlainText('\n')
                if count_malicious==0:
                    QtWidgets.QMessageBox.question(self, 'Message', 'You are good to go', QtWidgets.QMessageBox.Yes)
                else:
                    QtWidgets.QMessageBox.warning(self, 'Warning', 'This is malicious!!!', QtWidgets.QMessageBox.Yes)
        else:
            self.ERROR_URL(status_code)
    def ERROR_URL(self, status_code):
        Error_URL ={409:'AlreadyExistsError : The resource already exists.',
                    401:'AuthenticationRequiredError :The operation requires an authenticated user. Verify that you have provided your API key.\nUserNotActiveError : The user account is not active. Make sure you properly activated your account by following the link sent to your email.\nWrongCredentialsError:The provided API key is incorrect.',
                    400:'BadRequestError:The API request is invalid or malformed. The message usually provides details about why the request is not valid.\nInvalidArgumentError: Some of the provided arguments is incorrect. ',
                    403:'ForbiddenError: You are not allowed to perform the requested operation.',
                    404:'NotFoundError: The requested resource was not found.',
                    429:'QuotaExceededError: You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.\nTooManyRequestsError:Too many requests.',
                    503:'TransientError: Transient server error. Retry might work.',
                    'I Hate Bugs': 'SOme thing wrong...:(((('}
        if status_code in Error_URL:
            #print(Error_URL[status_code])
            EEE=Error_URL[status_code]
            self.OUT_PUT_URL.insertPlainText(EEE+'\n')
        else:
            #print(Error_URL['I Hate Bugs'])
            EEE=Error_URL['I Hate Bugs']
            self.OUT_PUT_URL.insertPlainText(EEE+'\n')

    def SanFile_Proccess(self):
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(290, 300, 541, 210))

        if self.File_INPUT=='':
            self.OUT_PUT_FileScan.insertPlainText("Enter a file please...\n")
            #self.SanFile_Proccess()
        else:
            self.OUT_PUT_FileScan.insertPlainText('Starting Scan File...\nPlease Wait for the process')
            self.OUT_PUT_FileScan.insertPlainText('\n....\n\n\n')

            a=FileScan(self.File_INPUT)
            KQ = a.result
            if KQ != {}:
                for i in KQ:
                    self.OUT_PUT_FileScan.insertPlainText(i+'    :  ')
                    p=KQ[i]['result']
                    if p==None:
                        self.OUT_PUT_FileScan.insertPlainText('None\n')
                    else:

                        self.OUT_PUT_FileScan.insertPlainText(p)
                        self.OUT_PUT_FileScan.insertPlainText('\n')
            else:
                self.OUT_PUT_FileScan.insertPlainText("Please Try again in a min... :(")

    def setupUi_Home(self):
        # SetupBackground
        self.OUT_PUT_URL.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.widget_URl_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.widget_File_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ABOUT_ME.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.CHOOSE_FILE.setGeometry(QtCore.QRect(0, 0, 0, 0))

        Back_color = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        gradient.setColorAt(1.0, QtGui.QColor(6, 57, 84, 60))
        gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        self.Form.setPalette(Back_color)
        #
        ###Set Label

        self.Label_HELLO.setText('SCAN ME')
        self.Animation()
    def setupUi_File(self):
        #Set up open file:
        self.OUT_PUT_URL.setGeometry(QtCore.QRect(0, 0, 0, 0))

        # SetupBackground
        self.widget_URl_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ABOUT_ME.setGeometry(QtCore.QRect(0, 0, 0, 0))
        #self.widget_File_scan.setGeometry(QtCore.QRect(290, 220, 541, 48))
        self.Animation_ScanFILE_FILENAME()

        Back_color = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        gradient.setColorAt(1.0, QtGui.QColor(6, 57, 84, 160))
        gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        self.Form.setPalette(Back_color)
        #
        icon_OpenFile_Button = QtGui.QIcon()
        icon_OpenFile_Button.addPixmap(QtGui.QPixmap("Icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CHOOSE_FILE.setIcon(icon_OpenFile_Button)
        self.CHOOSE_FILE.setIconSize(QtCore.QSize(40, 40))
        ###Set Label

        self.Label_HELLO.setText('SCAN FILE')
        self.Animation()
        self.Animation_Button_OpenFile()
        # self.CHOOSE_FILE.setGeometry(QtCore.QRect(730, 220, 131, 27))
        self.CHOOSE_FILE.setStyleSheet("background-color: #274472;")#border-radius: 10px;")
        #self.CHOOSE_FILE.setDisabled(False)

        #Open File
        # self.openFileNameDialog()
    def URL_Animation(self):
        self.anim_FileScan_Filename = QtCore.QPropertyAnimation(self.widget_URl_scan, b"geometry")
        self.anim_FileScan_Filename.setDuration(300)
        self.anim_FileScan_Filename.setStartValue(QtCore.QRect(290, 240, 0, 48))
        self.anim_FileScan_Filename.setEndValue(QtCore.QRect(290, 240, 541, 48))
        self.anim_FileScan_Filename.start()
    def Animation_ScanFILE_FILENAME(self):
        self.OUT_PUT_URL.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.File_INPUT=''

        self.File_CHOOSE_EDIT.clear()
        self.File_CHOOSE_EDIT.setPlaceholderText('Choose your File to Scan...')
        self.anim_FileScan_Filename = QtCore.QPropertyAnimation(self.widget_File_scan, b"geometry")
        self.anim_FileScan_Filename.setDuration(300)
        self.anim_FileScan_Filename.setStartValue(QtCore.QRect(290, 240, 0, 48))
        self.anim_FileScan_Filename.setEndValue(QtCore.QRect(290, 240, 541, 48))
        self.anim_FileScan_Filename.start()

    def setupUi_Url(self):
        # SetupBackground
        self.URL_Animation()
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(0, 0, 0, 0))


        self.widget_File_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ABOUT_ME.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.CHOOSE_FILE.setGeometry(QtCore.QRect(0, 0, 0, 0))

        Back_color = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        gradient.setColorAt(1.0, QtGui.QColor(6, 57, 184, 60))
        gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        self.Form.setPalette(Back_color)
        #
        ###Set Label
        self.Label_HELLO.setText('SCAN URL')
        self.Animation()
        ###
        ###
    def setupUi_About(self):
        # SetupBackground
        self.widget_URl_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.OUT_PUT_FileScan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.widget_File_scan.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.CHOOSE_FILE.setGeometry(QtCore.QRect(0, 0, 0, 0))


        self.ABOUT_ME.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ABOUT_ME.setObjectName("ABOUT_ME")
        self.ABOUT_ME.clear()
        self.ABOUT_ME.insertPlainText('''
        Hello World!!!
                  -J4mes-
        --------------ndd-
        This is "Scan Me" Tool, which help us Scan and Analysis File , URL , IP ...
        by Using API from Virustotal. 
        You can visit Virustotal here: https://www.virustotal.com
        --------------ndd-
        How to USE:
        First of all you have to go the Virustotal page.
        Login and take the API key in here: https://www.virustotal.com
        If you dont have an account, you can create one here:
        https://www.virustotal.com/gui/join-us
        PAY ATTENTION: This is your personal key. Do not disclose it to anyone that
        you do not trust, do not embed it in scripts or software from which it can 
        be easily retrieved if you care about its confidentiality.
        -------------ndd-
        The overview of API here:
        https://developers.virustotal.com/v3.0/reference#overview
        
        
        
        
        
        
        
        
        ''')

        #
        ###Set Label
        self.ABOUT_ME.setReadOnly(True)

        self.Label_HELLO.setText('ABOUT ME')
        self.Animation()
        self.Animation_ABout_me()
        # self.ABOUT_ME.setGeometry(QtCore.QRect(190, 170, 21, 41))
        # self.ABOUT_ME.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        Back_color = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1200, 0, 0, 1200)
        gradient.setColorAt(1.0, QtGui.QColor(116, 57, 84, 60))
        gradient.setColorAt(0.0, QtGui.QColor(5, 111, 146))
        Back_color.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        self.Form.setPalette(Back_color)

        ###

    def Animation_Button_OpenFile(self):
        self.anim_OpenFile_Button = QtCore.QPropertyAnimation(self.CHOOSE_FILE, b"geometry")
        self.anim_OpenFile_Button.setDuration(300)
        self.anim_OpenFile_Button.setStartValue(QtCore.QRect(490, 175, 90, 0))
        self.anim_OpenFile_Button.setEndValue(QtCore.QRect(490, 175, 90, 40))
        self.anim_OpenFile_Button.start()

    def Animation_ABout_me(self):

        self.anim_AboutMe = QtCore.QPropertyAnimation(self.ABOUT_ME, b"geometry")
        self.anim_AboutMe.setDuration(500)
        self.anim_AboutMe.setStartValue(QtCore.QRect(190, 170, 21, 41))
        self.anim_AboutMe.setEndValue(QtCore.QRect(190, 170, 675, 331))
        self.anim_AboutMe.start()

    def Animation(self):

        self.anim = QtCore.QPropertyAnimation(self.Label_HELLO, b"geometry")
        self.anim.setDuration(500)
        self.anim.setStartValue(QtCore.QRect(400, 100, 400, 120))
        self.anim.setEndValue(QtCore.QRect(400, 50, 400, 120))
        self.anim.start()

    def on_click_Home(self):
        self.setupUi_Home()

    def on_click_File(self):


        self.setupUi_File()

    def on_click_Url(self):


        self.setupUi_Url()

    def on_click_About(self):


        self.setupUi_About()


    def openFileNameDialog(self):

        #self.CHOOSE_FILE.setDisabled(True)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self , "FileName", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            #print(fileName)
            self.File_CHOOSE_EDIT.clear()
            self.File_CHOOSE_EDIT.setText(fileName)
            self.File_INPUT=fileName
        else:
            self.File_INPUT=''
            #print('no file')

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "ScanMEEEEEEEEEEEEEEEEEEEEE"))





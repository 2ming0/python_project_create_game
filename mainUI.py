from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import draw as drawing

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.pencolor = QColor(0,0,0)
        self.brushcolor = QColor(255,255,255)

        self.drawtype = 0

        # formbox = QHBoxLayout()
        # self.setLayout(formbox)
 
        #     # 좌, 우 레이아웃박스
        # left = QVBoxLayout()
        # right = QVBoxLayout()


        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.setWindowTitle('추리반에 잠입한 화가')

        self.MainWindow.setObjectName("추리반에 잠입한 화가")
        self.MainWindow.resize(990, 706)

        self.central=QtWidgets.QWidget(self.MainWindow)

        self.stackedWidget=QtWidgets.QStackedWidget(self.central)
        self.stackedWidget.setGeometry(0,0,990, 705)



        self.PageMain=QtWidgets.QWidget()
        self.PageMain.setObjectName("PageMain")

        self.main_background = QtWidgets.QLabel(self.PageMain)
        self.main_background.setGeometry(0, 0, 990, 705)
        self.main_background.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/game_main.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.main_background.setPixmap(qpixmapvar)
        self.main_background.setObjectName("main_background")


        self.main_doumBtn = QtWidgets.QPushButton(self.PageMain)
        self.main_doumBtn.setGeometry(QtCore.QRect(150, 520, 231, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_doumBtn.setFont(font)
        self.main_doumBtn.setCheckable(False)
        self.main_doumBtn.setObjectName("main_doumBtn")

        self.main_startBtn = QtWidgets.QPushButton(self.PageMain)
        self.main_startBtn.setGeometry(QtCore.QRect(400, 520, 231, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_startBtn.setFont(font)
        icon = QtGui.QIcon.fromTheme("tordusvlf")
        self.main_startBtn.setIcon(icon)
        self.main_startBtn.setObjectName("main_startBtn")
        self.main_exitBtn = QtWidgets.QPushButton(self.PageMain)
        self.main_exitBtn.setGeometry(QtCore.QRect(650, 520, 231, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_exitBtn.setFont(font)
        self.main_exitBtn.setObjectName("main_exitBtn")

        self.MainWindow.setCentralWidget(self.central)

        
        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)




        self.PageDoum=QtWidgets.QWidget() #doumpage
        self.PageDoum.setObjectName("PageDoum")

        self.doum_back = QtWidgets.QLabel(self.PageDoum)
        self.doum_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.doum_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/doum.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.doum_back.setPixmap(qpixmapvar)
        self.doum_back.setObjectName("doum_back")


        self.doum_gotoMain = QtWidgets.QPushButton(self.PageDoum)
        self.doum_gotoMain.setGeometry(QtCore.QRect(70, 600, 181, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.doum_gotoMain.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/image/return-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doum_gotoMain.setIcon(icon)
        self.doum_gotoMain.setObjectName("doum_gotoMain")

        self.retranslateDialog(self.PageDoum)
        QtCore.QMetaObject.connectSlotsByName(self.PageDoum)




        self.PageSetPerson=QtWidgets.QWidget() #setpersonpage
        self.PageSetPerson.setObjectName("PageSetPerson")

        self.setperson_back = QtWidgets.QLabel(self.PageSetPerson)
        self.setperson_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.setperson_back.setFont(font)
        self.setperson_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/blackboard.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.setperson_back.setPixmap(qpixmapvar)
        self.setperson_back.setObjectName("doum_back")


        self.setperson_setbutton = QtWidgets.QSpinBox(self.PageSetPerson)
        self.setperson_setbutton.setGeometry(QtCore.QRect(450, 340, 111, 101))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.setperson_setbutton.setFont(font)
        self.setperson_setbutton.setStyleSheet("")
        self.setperson_setbutton.setMinimum(3)
        self.setperson_setbutton.setMaximum(8)
        # self.setperson_setbutton.valueChanged.connect(self.spinBoxChanged)
        self.setperson_setbutton.setObjectName("setperson_setbutton")

        self.setperson_label = QtWidgets.QLabel(self.PageSetPerson)
        self.setperson_label.setGeometry(QtCore.QRect(260, 210, 501, 121))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.setperson_label.setFont(font)
        self.setperson_label.setStyleSheet("color:rgb(255, 255, 127)")
        self.setperson_label.setObjectName("setperson_label")

        self.setperson_okBtn = QtWidgets.QPushButton(self.PageSetPerson)
        self.setperson_okBtn.setGeometry(QtCore.QRect(460, 460, 93, 28))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setperson_okBtn.setFont(font)
        self.setperson_okBtn.setStyleSheet("")
        self.setperson_okBtn.setObjectName("setperson_okBtn")

        self.retranslateDialog1(self.PageSetPerson)
        QtCore.QMetaObject.connectSlotsByName(self.PageSetPerson)




        self.PageKeyword=QtWidgets.QWidget() #keywordpage
        self.PageKeyword.setObjectName("PageKeyword")

        self.keyword_back = QtWidgets.QLabel(self.PageKeyword)
        self.keyword_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.keyword_back.setText("")


        qpixmapvar=QPixmap()
        qpixmapvar.load("image/keyword_select.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.keyword_back.setPixmap(qpixmapvar)
        self.keyword_back.setObjectName("keyword_back")


        self.keyword_jobBtn = QtWidgets.QToolButton(self.PageKeyword)
        self.keyword_jobBtn.setGeometry(QtCore.QRect(150, 210, 151, 121))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_jobBtn.setFont(font)
        self.keyword_jobBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_jobBtn.setObjectName("keyword_jobBtn")
        self.keyword_foodBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_foodBtn.setGeometry(QtCore.QRect(320, 200, 151, 161))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_foodBtn.setFont(font)
        self.keyword_foodBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_foodBtn.setObjectName("keyword_foodBtn")
        self.keyword_objBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_objBtn.setGeometry(QtCore.QRect(500, 210, 161, 141))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_objBtn.setFont(font)
        self.keyword_objBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_objBtn.setObjectName("keyword_objBtn")
        self.keyword_movieBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_movieBtn.setGeometry(QtCore.QRect(680, 210, 151, 151))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_movieBtn.setFont(font)
        self.keyword_movieBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_movieBtn.setObjectName("keyword_movieBtn")
        self.keyword_idiomBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_idiomBtn.setGeometry(QtCore.QRect(140, 390, 191, 181))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_idiomBtn.setFont(font)
        self.keyword_idiomBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_idiomBtn.setObjectName("keyword_idiomBtn")
        self.keyword_sayingBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_sayingBtn.setGeometry(QtCore.QRect(360, 400, 181, 171))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_sayingBtn.setFont(font)
        self.keyword_sayingBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_sayingBtn.setObjectName("keyword_sayingBtn")
        self.keyword_sportsBtn = QtWidgets.QPushButton(self.PageKeyword)
        self.keyword_sportsBtn.setGeometry(QtCore.QRect(560, 400, 261, 181))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.keyword_sportsBtn.setFont(font)
        self.keyword_sportsBtn.setStyleSheet("background:transparent;\n"
"color:rgb(0, 0, 0)")
        self.keyword_sportsBtn.setObjectName("keyword_sportsBtn")

        self.retranslateDialog2(self.PageKeyword)
        QtCore.QMetaObject.connectSlotsByName(self.PageSetPerson)




        self.PageCuriosity=QtWidgets.QWidget() #pageCuriosity
        self.PageCuriosity.setObjectName("PageCuriosity")

        
        self.PageCuriosity.resize(990, 705)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PageCuriosity.setFont(font)
        self.curiosity_back = QtWidgets.QLabel(self.PageCuriosity)
        self.curiosity_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.curiosity_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/Curiosity_back.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.curiosity_back.setPixmap(qpixmapvar)
        self.curiosity_back.setObjectName("Curiosity_back")



        self.curiosity_okBtn = QtWidgets.QPushButton(self.PageCuriosity)
        self.curiosity_okBtn.setGeometry(QtCore.QRect(360, 480, 271, 131))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.curiosity_okBtn.setFont(font)
        self.curiosity_okBtn.setObjectName("curiosity_okBtn")

        self.retranslateDialog3(self.PageCuriosity)
        QtCore.QMetaObject.connectSlotsByName(self.PageCuriosity)



        self.PageArtist=QtWidgets.QWidget() #PageArtist
        self.PageArtist.setObjectName("PageArtist")

        self.PageArtist.resize(990, 705)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PageArtist.setFont(font)
        self.artist_back = QtWidgets.QLabel(self.PageArtist)
        self.artist_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.artist_back.setText("")


        qpixmapvar=QPixmap()
        qpixmapvar.load("image/artist_back.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.artist_back.setPixmap(qpixmapvar)
        self.artist_back.setObjectName("artist_back")

        self.artist_text = QtWidgets.QTextBrowser(self.PageArtist)
        self.artist_text.setGeometry(QtCore.QRect(430, 300, 291, 151))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.artist_text.setFont(font)
        self.artist_text.setObjectName("artist_text")

        self.artist_backBtn = QtWidgets.QPushButton(self.PageArtist)
        self.artist_backBtn.setGeometry(QtCore.QRect(40, 600, 181, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.artist_backBtn.setFont(font)
        self.artist_backBtn.setObjectName("artist_backBtn")

        self.retranslateDialog5(self.PageArtist)
        QtCore.QMetaObject.connectSlotsByName(self.PageArtist)


        self.Pagemmy=QtWidgets.QWidget() #mmy
        self.Pagemmy.setObjectName("Pagemmy")

        self.Pagemmy.resize(990, 705)
        self.mmy_back = QtWidgets.QLabel(self.Pagemmy)
        self.mmy_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.mmy_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/mystery_back.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.mmy_back.setPixmap(qpixmapvar)
        self.mmy_back.setObjectName("Curiosity_back")

        self.mmy_label = QtWidgets.QLabel(self.Pagemmy)
        self.mmy_label.setGeometry(QtCore.QRect(280, 490, 651, 111))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.mmy_label.setFont(font)
        self.mmy_label.setObjectName("mmy_label")

        self.mmy_btn = QtWidgets.QPushButton(self.Pagemmy)
        self.mmy_btn.setGeometry(QtCore.QRect(40, 600, 181, 81))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.mmy_btn.setFont(font)
        self.mmy_btn.setObjectName("mmy_btn")

        self.retranslateDialog4(self.Pagemmy)
        QtCore.QMetaObject.connectSlotsByName(self.Pagemmy)


        self.PageVote=QtWidgets.QWidget() #Pagevote
        self.PageVote.setObjectName("PageVote")

        self.label = QtWidgets.QLabel(self.PageVote)
        self.label.setGeometry(QtCore.QRect(0, 0, 990, 704))
        self.label.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/blackboard.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.label.setPixmap(qpixmapvar)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.PageVote)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 211, 174))
        self.label_2.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint2.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 174)
        self.label_2.setPixmap(qpixmapvar)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.PageVote)
        self.label_3.setGeometry(QtCore.QRect(280, 140, 211, 173))
        self.label_3.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint2.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 173)
        self.label_3.setPixmap(qpixmapvar)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.PageVote)
        self.label_4.setGeometry(QtCore.QRect(500, 140, 211, 175))
        self.label_4.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint3.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 175)
        self.label_4.setPixmap(qpixmapvar)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.PageVote)
        self.label_5.setGeometry(QtCore.QRect(720, 140, 211, 174))
        self.label_5.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint4.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 174)
        self.label_5.setPixmap(qpixmapvar)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.PageVote)
        self.label_6.setGeometry(QtCore.QRect(60, 380, 211, 174))
        self.label_6.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint5.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 174)
        self.label_6.setPixmap(qpixmapvar)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.PageVote)
        self.label_7.setGeometry(QtCore.QRect(280, 380, 211, 173))
        self.label_7.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint6.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 173)
        self.label_7.setPixmap(qpixmapvar)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.PageVote)
        self.label_8.setGeometry(QtCore.QRect(500, 380, 211, 176))
        self.label_8.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint7.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 176)
        self.label_8.setPixmap(qpixmapvar)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.PageVote)
        self.label_9.setGeometry(QtCore.QRect(720, 380, 211, 173))
        self.label_9.setText("")
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/paint8.jpg")
        qpixmapvar=qpixmapvar.scaled(211, 173)
        self.label_9.setPixmap(qpixmapvar)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.PageVote)
        self.label_10.setGeometry(QtCore.QRect(80, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.PageVote)
        self.label_11.setGeometry(QtCore.QRect(290, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.PageVote)
        self.label_12.setGeometry(QtCore.QRect(510, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.PageVote)
        self.label_13.setGeometry(QtCore.QRect(730, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.PageVote)
        self.label_14.setGeometry(QtCore.QRect(70, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.PageVote)
        self.label_15.setGeometry(QtCore.QRect(290, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.PageVote)
        self.label_16.setGeometry(QtCore.QRect(510, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.PageVote)
        self.label_17.setGeometry(QtCore.QRect(730, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:rgb(255, 255, 127)")
        self.label_17.setObjectName("label_17")
        self.vote_input = QtWidgets.QLineEdit(self.PageVote)
        self.vote_input.setGeometry(QtCore.QRect(340, 610, 211, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vote_input.setFont(font)
        self.vote_input.setObjectName("vote_input")
        self.vote_inputBtn = QtWidgets.QPushButton(self.PageVote)
        self.vote_inputBtn.setGeometry(QtCore.QRect(560, 610, 101, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.vote_inputBtn.setFont(font)
        self.vote_inputBtn.setObjectName("vote_inputBtn")

        self.retranslateDialog6(self.PageVote)
        QtCore.QMetaObject.connectSlotsByName(self.PageVote)



        self.PageMysteryWin=QtWidgets.QWidget() #PageMysteryWin
        self.PageMysteryWin.setObjectName("PageMysteryWin")

        self.PageMysteryWin.resize(990, 705)
        self.result_mysteryWin_back = QtWidgets.QLabel(self.PageMysteryWin)
        self.result_mysteryWin_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.result_mysteryWin_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/blackboard.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.result_mysteryWin_back.setPixmap(qpixmapvar)
        self.result_mysteryWin_back.setObjectName("result_mysteryWin_back")

        self.result_mysteryWin_title = QtWidgets.QLabel(self.PageMysteryWin)
        self.result_mysteryWin_title.setGeometry(QtCore.QRect(260, 80, 471, 171))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.result_mysteryWin_title.setFont(font)
        self.result_mysteryWin_title.setStyleSheet("color:rgb(255, 255, 127)")
        self.result_mysteryWin_title.setObjectName("result_mysteryWin_title")
        self.result_mysteryWin_text = QtWidgets.QLabel(self.PageMysteryWin)
        self.result_mysteryWin_text.setGeometry(QtCore.QRect(140, 220, 441, 111))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result_mysteryWin_text.setFont(font)
        self.result_mysteryWin_text.setStyleSheet("color:rgb(255, 255, 255)")
        self.result_mysteryWin_text.setObjectName("result_mysteryWin_text")
        self.result_mysteryWin_input = QtWidgets.QLineEdit(self.PageMysteryWin)
        self.result_mysteryWin_input.setGeometry(QtCore.QRect(130, 320, 571, 91))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.result_mysteryWin_input.setFont(font)
        self.result_mysteryWin_input.setObjectName("result_mysteryWin_input")
        self.result_mysteryWin_inputBtn = QtWidgets.QPushButton(self.PageMysteryWin)
        self.result_mysteryWin_inputBtn.setGeometry(QtCore.QRect(730, 340, 131, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕OTF ExtraBold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.result_mysteryWin_inputBtn.setFont(font)
        self.result_mysteryWin_inputBtn.setObjectName("result_mysteryWin_inputBtn")

        self.retranslateDialog7(self.PageMysteryWin)
        QtCore.QMetaObject.connectSlotsByName(self.PageMysteryWin)



        self.PageMysteryfinalWin=QtWidgets.QWidget() #PageMysteryfinalWin
        self.PageMysteryfinalWin.setObjectName("PageMysteryfinalWin")

        self.PageMysteryfinalWin.resize(990, 705)
        self.result_mysteryfinalWin_back = QtWidgets.QLabel(self.PageMysteryfinalWin)
        self.result_mysteryfinalWin_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.result_mysteryfinalWin_back.setText("")

        qpixmapvar=QPixmap()
        qpixmapvar.load("image/mysteryWin.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.result_mysteryfinalWin_back.setPixmap(qpixmapvar)
        self.result_mysteryfinalWin_back.setObjectName("result_mysteryfinalWin_back")

        self.retranslateDialog8(self.PageMysteryfinalWin)
        QtCore.QMetaObject.connectSlotsByName(self.PageMysteryfinalWin)


        self.PageArtistfinalWin=QtWidgets.QWidget() #PageArtistfinalWin
        self.PageArtistfinalWin.setObjectName("PageArtistfinalWin")

        self.PageArtistfinalWin.resize(990, 705)
        self.result_artistfinalWin_back = QtWidgets.QLabel(self.PageArtistfinalWin)
        self.result_artistfinalWin_back.setGeometry(QtCore.QRect(0, 0, 990, 705))
        self.result_artistfinalWin_back.setText("")
        
        qpixmapvar=QPixmap()
        qpixmapvar.load("image/artistWin.jpg")
        qpixmapvar=qpixmapvar.scaled(990, 705)
        self.result_artistfinalWin_back.setPixmap(qpixmapvar)
        self.result_artistfinalWin_back.setObjectName("result_artistfinalWin_back") 

        self.retranslateDialog9(self.PageArtistfinalWin)
        QtCore.QMetaObject.connectSlotsByName(self.PageArtistfinalWin)

        

        self.PageDraw=QtWidgets.QWidget() #Pagedraw
        self.PageDraw.setObjectName("PageDraw")

        # self.right = QVBoxLayout()
    
        # self.view.setGeometry(QtCore.QRect(240, 20, 741, 671))

        self.formLayoutWidget = QtWidgets.QWidget(self.PageDraw)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 20, 641, 571))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.groupBox1 = QtWidgets.QGroupBox(self.PageDraw)
        self.groupBox1.setGeometry(QtCore.QRect(20, 20, 201, 151))
        self.groupBox1.setObjectName("groupBox1")
        self.line = QtWidgets.QRadioButton(self.groupBox1)
        self.line.setGeometry(QtCore.QRect(10, 30, 108, 19))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.line.setFont(font)
        self.line.setObjectName("line")
        self.curve = QtWidgets.QRadioButton(self.groupBox1)
        self.curve.setGeometry(QtCore.QRect(10, 60, 108, 19))
        self.curve.setObjectName("curve")
        self.rectangle = QtWidgets.QRadioButton(self.groupBox1)
        self.rectangle.setGeometry(QtCore.QRect(10, 90, 108, 19))
        self.rectangle.setObjectName("rectangle")
        self.ellipse = QtWidgets.QRadioButton(self.groupBox1)
        self.ellipse.setGeometry(QtCore.QRect(10, 120, 108, 19))
        self.ellipse.setObjectName("ellipse")
        self.groupBox2 = QtWidgets.QGroupBox(self.PageDraw)
        self.groupBox2.setGeometry(QtCore.QRect(20, 190, 201, 121))
        self.drawType = 0



        self.groupBox2.setObjectName("groupBox2")
        self.choose_thick = QtWidgets.QComboBox(self.groupBox2)
        self.choose_thick.setGeometry(QtCore.QRect(103, 31, 91, 31))
        self.choose_thick.setObjectName("choose_thick")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.choose_thick.addItem("")
        self.thickness = QtWidgets.QPlainTextEdit(self.groupBox2)
        self.thickness.setGeometry(QtCore.QRect(10, 30, 61, 31))
        self.thickness.setAutoFillBackground(False)
        self.thickness.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.thickness.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.thickness.setFrameShadow(QtWidgets.QFrame.Plain)
        self.thickness.setBackgroundVisible(True)
        self.thickness.setObjectName("thickness")
        self.color = QtWidgets.QPlainTextEdit(self.groupBox2)
        self.color.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.color.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.color.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.color.setObjectName("color")
        self.choose_color = QtWidgets.QPushButton(self.groupBox2)
        self.choose_color.setGeometry(QtCore.QRect(102, 70, 91, 31))
        self.choose_color.setStyleSheet("background-color: rgb(0,0,0)")
        self.choose_color.setObjectName("choose_color")
        self.groupBox3 = QtWidgets.QGroupBox(self.PageDraw)
        self.groupBox3.setGeometry(QtCore.QRect(20, 330, 201, 81))



        self.groupBox3.setObjectName("groupBox3")
        self.choose_brush = QtWidgets.QPushButton(self.groupBox3)
        self.choose_brush.setGeometry(QtCore.QRect(100, 30, 91, 31))
        self.choose_brush.setStyleSheet("background-color: rgb(255,255,255)")
        self.choose_brush.setObjectName("choose_brush")
        self.brush = QtWidgets.QPlainTextEdit(self.groupBox3)
        self.brush.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.brush.setStyleSheet("background-color:rgb(240, 240, 240)")
        self.brush.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.brush.setObjectName("brush")
        self.groupBox4 = QtWidgets.QGroupBox(self.PageDraw)
        self.groupBox4.setGeometry(QtCore.QRect(20, 430, 201, 71))



        self.groupBox4.setObjectName("groupBox4")
        self.eraser = QtWidgets.QCheckBox(self.groupBox4)
        self.eraser.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.eraser.setObjectName("eraser")
        self.erase_all = QtWidgets.QPushButton(self.groupBox4)
        self.erase_all.setGeometry(QtCore.QRect(100, 30, 93, 28))
        self.erase_all.setObjectName("erase_all")
        self.groupBox5 = QtWidgets.QGroupBox(self.PageDraw)
        self.groupBox5.setGeometry(QtCore.QRect(20, 520, 201, 71))



        self.groupBox5.setObjectName("groupBox5")
        self.finish = QtWidgets.QPushButton(self.groupBox5)
        self.finish.setGeometry(QtCore.QRect(22, 30, 161, 28))
        self.finish.setObjectName("finish")

        self.retranslateDialog10(self.PageDraw)
        QtCore.QMetaObject.connectSlotsByName(self.PageDraw)

        self.rightWidget = QtWidgets.QWidget(self.PageDraw)
        self.rightWidget.setGeometry(QtCore.QRect(240, 20, 641, 571))
        self.rightWidget.setObjectName("formLayoutWidget")
        self.right = QtWidgets.QFormLayout(self.rightWidget)
        self.right.setContentsMargins(0, 0, 0, 0)
        self.right.setObjectName("formLayout")

        self.PageDraw.resize(900, 705)
        # self.canvas = QtWidgets.QGraphicsView(self.PageDraw)
        # self.canvas.setGeometry(QtCore.QRect(240, 20, 741, 671))
        # self.canvas.setInteractive(False)
        # self.canvas.setObjectName("canvas")  #그리기 캔버스
        self.view = CView(self)
        self.right.addWidget(self.view)
        

        
        self.stackedWidget.addWidget(self.PageMain)
        self.stackedWidget.addWidget(self.Pagemmy)
        self.stackedWidget.addWidget(self.PageDoum)
        self.stackedWidget.addWidget(self.PageSetPerson)
        self.stackedWidget.addWidget(self.PageKeyword)
        self.stackedWidget.addWidget(self.PageCuriosity)
        self.stackedWidget.addWidget(self.PageArtist)
        self.stackedWidget.addWidget(self.PageVote)
        self.stackedWidget.addWidget(self.PageMysteryWin)
        self.stackedWidget.addWidget(self.PageMysteryfinalWin)
        self.stackedWidget.addWidget(self.PageArtistfinalWin)
        self.stackedWidget.addWidget(self.PageDraw)

        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("self.MainWindow", "self.MainWindow"))
        self.main_doumBtn.setText(_translate("self.MainWindow", "도움말"))
        self.main_startBtn.setText(_translate("self.MainWindow", "시작"))
        self.main_exitBtn.setText(_translate("self.MainWindow", "게임 종료"))

    def retranslateDialog(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.doum_gotoMain.setText(_translate("Dialog", "메인 화면으로"))

    def retranslateDialog1(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.setperson_label.setText(_translate("Dialog", "플레이 할 플레이어 수를 선택하세요"))
        self.setperson_okBtn.setText(_translate("Dialog", "확인"))

    def retranslateDialog2(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.keyword_jobBtn.setText(_translate("Dialog", "직업"))
        self.keyword_foodBtn.setText(_translate("Dialog", "음식"))
        self.keyword_objBtn.setText(_translate("Dialog", "사물"))
        self.keyword_movieBtn.setText(_translate("Dialog", "영화"))
        self.keyword_idiomBtn.setText(_translate("Dialog", "사자성어"))
        self.keyword_sayingBtn.setText(_translate("Dialog", "속담"))
        self.keyword_sportsBtn.setText(_translate("Dialog", "스포츠/운동"))
        
    def retranslateDialog3(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.curiosity_okBtn.setText(_translate("Dialog", "확인하기"))

    def retranslateDialog4(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mmy_label.setText(_translate("Dialog", "diiiiiiiiiiiiiiiiii"))
        self.mmy_btn.setText(_translate("Dialog", "확인완료"))

    def retranslateDialog5(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.artist_backBtn.setText(_translate("Dialog", "확인완료"))

    def retranslateDialog6(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_10.setText(_translate("Dialog", "1번"))
        self.label_11.setText(_translate("Dialog", "2번"))
        self.label_12.setText(_translate("Dialog", "3번"))
        self.label_13.setText(_translate("Dialog", "4번"))
        self.label_14.setText(_translate("Dialog", "5번"))
        self.label_15.setText(_translate("Dialog", "6번"))
        self.label_16.setText(_translate("Dialog", "7번"))
        self.label_17.setText(_translate("Dialog", "8번"))
        self.vote_inputBtn.setText(_translate("Dialog", "입력"))

    def retranslateDialog7(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.result_mysteryWin_title.setText(_translate("Dialog", "화가 검거에 성공했습니다!"))
        self.result_mysteryWin_text.setText(_translate("Dialog", "화가는 예상되는 제시어를 입력해주세요!"))
        self.result_mysteryWin_inputBtn.setText(_translate("Dialog", "입력"))

    def retranslateDialog8(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.result_mysteryfinalWin_title.setText(_translate("Dialog", "추리반의 최종 승리 !"))

    def retranslateDialog9(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        # self.result_artistfinalWin_title.setText(_translate("Dialog", "화가의 최종 승리 !"))

    def retranslateDialog10(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox1.setTitle(_translate("Dialog", "그리기 종류"))
        self.line.setText(_translate("Dialog", "line"))
        self.curve.setText(_translate("Dialog", "Curve"))
        self.rectangle.setText(_translate("Dialog", "Rectangle"))
        self.ellipse.setText(_translate("Dialog", "Ellipse"))
        self.groupBox2.setTitle(_translate("Dialog", "펜 설정"))
        self.choose_thick.setItemText(0, _translate("Dialog", "1"))
        self.choose_thick.setItemText(1, _translate("Dialog", "2"))
        self.choose_thick.setItemText(2, _translate("Dialog", "3"))
        self.choose_thick.setItemText(3, _translate("Dialog", "4"))
        self.choose_thick.setItemText(4, _translate("Dialog", "5"))
        self.choose_thick.setItemText(5, _translate("Dialog", "6"))
        self.choose_thick.setItemText(6, _translate("Dialog", "7"))
        self.choose_thick.setItemText(7, _translate("Dialog", "8"))
        self.choose_thick.setItemText(8, _translate("Dialog", "9"))
        self.choose_thick.setItemText(9, _translate("Dialog", "19"))
        self.choose_thick.setItemText(10, _translate("Dialog", "11"))
        self.choose_thick.setItemText(11, _translate("Dialog", "12"))
        self.choose_thick.setItemText(12, _translate("Dialog", "13"))
        self.choose_thick.setItemText(13, _translate("Dialog", "14"))
        self.choose_thick.setItemText(14, _translate("Dialog", "15"))
        self.choose_thick.setItemText(15, _translate("Dialog", "16"))
        self.choose_thick.setItemText(16, _translate("Dialog", "17"))
        self.choose_thick.setItemText(17, _translate("Dialog", "18"))
        self.choose_thick.setItemText(18, _translate("Dialog", "19"))
        self.choose_thick.setItemText(19, _translate("Dialog", "20"))
        self.thickness.setPlainText(_translate("Dialog", "선굵기"))
        self.color.setPlainText(_translate("Dialog", "선 색상"))
        self.choose_color.setText(_translate("Dialog", " "))
        self.groupBox3.setTitle(_translate("Dialog", "붓 설정"))
        self.choose_brush.setText(_translate("Dialog", " "))
        self.brush.setPlainText(_translate("Dialog", "붓색상"))
        self.groupBox4.setTitle(_translate("Dialog", "지우개"))
        self.eraser.setText(_translate("Dialog", "지우개"))
        self.erase_all.setText(_translate("Dialog", "모두 지우기"))
        self.groupBox5.setTitle(_translate("Dialog", "그리기 완료"))
        self.finish.setText(_translate("Dialog", "완료"))


# class CWidget(QWidget): 

#         def __init__(self):
#             # super().__init__()
#             # super(CWidget, self).__init__()
#             self.PageDraw = QtWidgets.QWidget()
#             self.PageDraw.setObjectName("PageDraw")
#             self.PageDraw.resize(990, 706)

#             self.central=QtWidgets.QWidget(self.PageDraw)

#             self.formbox = QHBoxLayout()
#             self.setLayout(self.formbox)
 
#             # 좌, 우 레이아웃박스
#             self.left = QVBoxLayout()
#             self.right = QVBoxLayout()
 
#             # 그룹박스1 생성 및 좌 레이아웃 배치
#             self.gb = QGroupBox('그리기 종류')        
#             self.left.addWidget(self.gb)
 
#             # 그룹박스1 에서 사용할 레이아웃
#             self.box = QVBoxLayout()
#             self.gb.setLayout(self.box)        
 
#             # 그룹박스 1 의 라디오 버튼 배치
#             self.text = ['line', 'Curve', 'Rectange', 'Ellipse']
#             self.radiobtns = []
 
#             for i in range(len(self.text)):
#                 self.radiobtns.append(QRadioButton(self.text[i], self))
#                 self.radiobtns[i].clicked.connect(self.radioClicked)
#                 self.box.addWidget(self.radiobtns[i])
 
#             self.radiobtns[0].setChecked(True)
#             self.drawType = 0
         
#             # 그룹박스2
#             self.gb = QGroupBox('펜 설정')        
#             self.left.addWidget(self.gb)        
 
#             self.grid = QGridLayout()      
#             self.gb.setLayout(self.grid)        
 
#             self.label = QLabel('선굵기')
#             self.grid.addWidget(self.label, 0, 0)
 
#             self.combo = QComboBox()
#             self.grid.addWidget(self.combo, 0, 1)       
 
#             for i in range(1, 21):
#                 self.combo.addItem(str(i))
 
#             self.label = QLabel('선색상')
#             self.grid.addWidget(self.label, 1,0)        
         
#             self.pencolor = QColor(0,0,0)
#             self.penbtn = QPushButton()        
#             self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
#             self.penbtn.clicked.connect(self.showColorDlg)
#             self.grid.addWidget(self.penbtn,1, 1)
         
 
#             # 그룹박스3
#             self.gb = QGroupBox('붓 설정')        
#             self.left.addWidget(self.gb)
 
#             self.hbox = QHBoxLayout()
#             self.gb.setLayout(self.hbox)
 
#             self.label = QLabel('붓색상')
#             self.hbox.addWidget(self.label)                
 
#             self.brushcolor = QColor(255,255,255)
#             self.brushbtn = QPushButton()        
#             self.brushbtn.setStyleSheet('background-color: rgb(255,255,255)')
#             self.brushbtn.clicked.connect(self.showColorDlg)
#             self.hbox.addWidget(self.brushbtn)
 
#             # 그룹박스4
#             self.gb = QGroupBox('지우개')        
#             self.left.addWidget(self.gb)
 
#             self.hbox = QHBoxLayout()
#             self.gb.setLayout(self.hbox)        
         
#             self.checkbox  = QCheckBox('지우개')
#             self.checkbox.stateChanged.connect(self.checkClicked)
#             self.hbox.addWidget(self.checkbox)

#             self.erasebtn = QPushButton('모두 지우기')
#             self.erasebtn.clicked.connect(self.eraseClicked)
#             self.hbox.addWidget(self.erasebtn)

#             # 그룹박스5
#             # gb = QGroupBox('제한시간')
#             # left.addWidget(gb)

#             # hbox = QHBoxLayout()
#             # gb.setLayout(hbox)
            
#             # self.pbar = QProgressBar(self)
#             # self.timer = QBasicTimer()
#             # self.step = 0

#             # self.timer.start(300, self) #30초

#             # hbox.addWidget(self.pbar)

#             #그룹박스6
#             self.gb = QGroupBox('그리기 완료')
#             self.left.addWidget(self.gb)

#             self.hbox = QHBoxLayout()
#             self.gb.setLayout(self.hbox)

#             self.draw_finishbtn = QPushButton('완료')
#             self.draw_finishbtn.clicked.connect(self.drawFinished)
#             self.hbox.addWidget(self.draw_finishbtn)

#             # self.timer = QTimer(self)
#             # self.timer.setInterval(30000)
#             # self.timer.timeout.connect(self.timeout)


#             # self.lcd = QLCDNumber()
#             # self.lcd.display('')
#             # self.lcd.setDigitCount(8)

#             self.subLayout = QHBoxLayout()

#             #hbox.addWidget(self.lcd)

 
       
#             self.left.addStretch(1)        
          
#             # 우 레이아웃 박스에 그래픽 뷰 추가
#             self.view = CView(self)       
#             self.right.addWidget(self.view)        
 
#             # 전체 폼박스에 좌우 박스 배치
#             self.formbox.addLayout(left)
#             self.formbox.addLayout(right)
 
#             self.formbox.setStretchFactor(left, 0)
#             self.formbox.setStretchFactor(right, 1)
         
#             self.setGeometry(100, 100, 800, 500)


#             self.stackedWidget=QtWidgets.QStackedWidget(self.central)
#             self.stackedWidget.setGeometry(0,0,990, 705)
#             # self.initUI()



#             self.stackedWidget.addWidget(self.PageDraw)

#             # self.timer = QTimer(self)
#             # self.timer.start(10000) #일단 10초로 설정 ..
#             # self.timer.timeout.connect(self.close_drawpage)

#         def close_drawpage(self):
#             self.close()
 
#         # def initUI(self):
#         #     # 전체 폼 박스
#         #     formbox = QHBoxLayout()
#         #     self.setLayout(formbox)
 
#         #     # 좌, 우 레이아웃박스
#         #     left = QVBoxLayout()
#         #     right = QVBoxLayout()
 
#         #     # 그룹박스1 생성 및 좌 레이아웃 배치
#         #     gb = QGroupBox('그리기 종류')        
#         #     left.addWidget(gb)
 
#         #     # 그룹박스1 에서 사용할 레이아웃
#         #     box = QVBoxLayout()
#         #     gb.setLayout(box)        
 
#         #     # 그룹박스 1 의 라디오 버튼 배치
#         #     text = ['line', 'Curve', 'Rectange', 'Ellipse']
#         #     self.radiobtns = []
 
#         #     for i in range(len(text)):
#         #         self.radiobtns.append(QRadioButton(text[i], self))
#         #         self.radiobtns[i].clicked.connect(self.radioClicked)
#         #         box.addWidget(self.radiobtns[i])
 
#         #     self.radiobtns[0].setChecked(True)
#         #     self.drawType = 0
         
#         #     # 그룹박스2
#         #     gb = QGroupBox('펜 설정')        
#         #     left.addWidget(gb)        
 
#         #     grid = QGridLayout()      
#         #     gb.setLayout(grid)        
 
#         #     label = QLabel('선굵기')
#         #     grid.addWidget(label, 0, 0)
 
#         #     self.combo = QComboBox()
#         #     grid.addWidget(self.combo, 0, 1)       
 
#         #     for i in range(1, 21):
#         #         self.combo.addItem(str(i))
 
#         #     label = QLabel('선색상')
#         #     grid.addWidget(label, 1,0)        
         
#         #     self.pencolor = QColor(0,0,0)
#         #     self.penbtn = QPushButton()        
#         #     self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
#         #     self.penbtn.clicked.connect(self.showColorDlg)
#         #     grid.addWidget(self.penbtn,1, 1)
         
 
#         #     # 그룹박스3
#         #     gb = QGroupBox('붓 설정')        
#         #     left.addWidget(gb)
 
#         #     hbox = QHBoxLayout()
#         #     gb.setLayout(hbox)
 
#         #     label = QLabel('붓색상')
#         #     hbox.addWidget(label)                
 
#         #     self.brushcolor = QColor(255,255,255)
#         #     self.brushbtn = QPushButton()        
#         #     self.brushbtn.setStyleSheet('background-color: rgb(255,255,255)')
#         #     self.brushbtn.clicked.connect(self.showColorDlg)
#         #     hbox.addWidget(self.brushbtn)
 
#         #     # 그룹박스4
#         #     gb = QGroupBox('지우개')        
#         #     left.addWidget(gb)
 
#         #     hbox = QHBoxLayout()
#         #     gb.setLayout(hbox)        
         
#         #     self.checkbox  = QCheckBox('지우개')
#         #     self.checkbox.stateChanged.connect(self.checkClicked)
#         #     hbox.addWidget(self.checkbox)

#         #     self.erasebtn = QPushButton('모두 지우기')
#         #     self.erasebtn.clicked.connect(self.eraseClicked)
#         #     hbox.addWidget(self.erasebtn)

#         #     # 그룹박스5
#         #     # gb = QGroupBox('제한시간')
#         #     # left.addWidget(gb)

#         #     # hbox = QHBoxLayout()
#         #     # gb.setLayout(hbox)
            
#         #     # self.pbar = QProgressBar(self)
#         #     # self.timer = QBasicTimer()
#         #     # self.step = 0

#         #     # self.timer.start(300, self) #30초

#         #     # hbox.addWidget(self.pbar)

#         #     #그룹박스6
#         #     gb = QGroupBox('그리기 완료')
#         #     left.addWidget(gb)

#         #     hbox = QHBoxLayout()
#         #     gb.setLayout(hbox)

#         #     self.draw_finishbtn = QPushButton('완료')
#         #     self.draw_finishbtn.clicked.connect(self.drawFinished)
#         #     hbox.addWidget(self.draw_finishbtn)

#         #     # self.timer = QTimer(self)
#         #     # self.timer.setInterval(30000)
#         #     # self.timer.timeout.connect(self.timeout)


#         #     # self.lcd = QLCDNumber()
#         #     # self.lcd.display('')
#         #     # self.lcd.setDigitCount(8)

#         #     subLayout = QHBoxLayout()

#         #     #hbox.addWidget(self.lcd)

 
       
#         #     left.addStretch(1)        
          
#         #     # 우 레이아웃 박스에 그래픽 뷰 추가
#         #     self.view = CView(self)       
#         #     right.addWidget(self.view)        
 
#         #     # 전체 폼박스에 좌우 박스 배치
#         #     formbox.addLayout(left)
#         #     formbox.addLayout(right)
 
#         #     formbox.setStretchFactor(left, 0)
#         #     formbox.setStretchFactor(right, 1)
         
#         #     self.setGeometry(100, 100, 800, 500) 


         
#         def radioClicked(self):
#             for i in range(len(self.radiobtns)):
#                 if self.radiobtns[i].isChecked():
#                     self.drawType = i                
#                     break
 
#         def checkClicked(self):
#             pass
             
#         def eraseClicked(self):
#             for i in self.view.scene.items():
#                 self.view.scene.removeItem(i)



#         def showColorDlg(self):       
         
#             # 색상 대화상자 생성      
#             color = QColorDialog.getColor()
 
#             sender = self.sender()
 
#             # 색상이 유효한 값이면 참, QFrame에 색 적용
#             if sender == self.penbtn and color.isValid():           
#                 self.pencolor = color
#                 self.penbtn.setStyleSheet('background-color: {}'.format( color.name()))
#             else:
#                 self.brushcolor = color
#                 self.brushbtn.setStyleSheet('background-color: {}'.format( color.name()))

#         def showModal(self):
#             return super().exec_()

#             # "C:\Users\yygs3\OneDrive\Desktop\파이썬기반응용프로그래밍\추리반에 잠입한 화가\image"

#         def drawFinished(self):
#             img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
#             img.save('D:\\drawing.png')   
#             self.close()
 
 
         
# #     # QGraphicsView display QGraphicsScene
class CView(QGraphicsView):
    
        def __init__(self, parent):
 
            super().__init__(parent)     
              
            self.scene = QGraphicsScene()        
            self.setScene(self.scene)
 
            self.items = []
         
            self.start = QPointF()
            self.end = QPointF()
 
            self.setRenderHint(QPainter.HighQualityAntialiasing)
        
 
        def moveEvent(self, e):
            rect = QRectF(self.rect())
            rect.adjust(0,0,-2,-2)
 
            self.scene.setSceneRect(rect)
 
        def mousePressEvent(self, e):
 
            if e.button() == Qt.LeftButton:
                # 시작점 저장
                self.start = e.pos()
                self.end = e.pos()        
 
        def mouseMoveEvent(self, e):  
         
            # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴 
            if e.buttons() & Qt.LeftButton:           
 
                self.end = e.pos()
 
                if self.parent().eraser.isChecked():
                    pen = QPen(QColor(255,255,255), 10)
                    path = QPainterPath()
                    path.moveTo(self.start)
                    path.lineTo(self.end)
                    self.scene.addPath(path, pen)
                    self.start = e.pos()
                    return None
 
                pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
                # 직선 그리기
                if self.parent().drawType == 0:

                    print("1")
                 
                    # 장면에 그려진 이전 선을 제거            
                    if len(self.items) > 0:
                        self.scene.removeItem(self.items[-1])
                        del(self.items[-1])                
 
                    # 현재 선 추가
                    line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())                
                    self.items.append(self.scene.addLine(line, pen))
 
                # 곡선 그리기
                if self.parent().drawType == 1:
 
                    # Path 이용
                    path = QPainterPath()
                    path.moveTo(self.start)
                    path.lineTo(self.end)
                    self.scene.addPath(path, pen)
 
                # Line 이용
                #line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                #self.scene.addLine(line, pen)
                 
                    # 시작점을 다시 기존 끝점으로
                    self.start = e.pos()
 
                # 사각형 그리기
                if self.parent().drawType == 2:
                    brush = QBrush(self.parent().brushcolor)
 
                    if len(self.items) > 0:
                        self.scene.removeItem(self.items[-1])
                        del(self.items[-1])
 
 
                    rect = QRectF(self.start, self.end)
                    self.items.append(self.scene.addRect(rect, pen, brush))
                 
                # 원 그리기
                if self.parent().drawType == 3:
                    brush = QBrush(self.parent().brushcolor)
 
                    if len(self.items) > 0:
                        self.scene.removeItem(self.items[-1])
                        del(self.items[-1])
 
 
                    rect = QRectF(self.start, self.end)
                    self.items.append(self.scene.addEllipse(rect, pen, brush))
 
 
        def mouseReleaseEvent(self, e):        
 
            if e.button() == Qt.LeftButton:
 
                if self.parent().eraser.isChecked():
                    return None
 
                pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
                if self.parent().drawType == 0:
 
                    self.items.clear()
                    line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                 
                    self.scene.addLine(line, pen)
 
                if self.parent().drawType == 2:
 
                    brush = QBrush(self.parent().brushcolor)
 
                    self.items.clear()
                    rect = QRectF(self.start, self.end)
                    self.scene.addRect(rect, pen, brush)
 
                if self.parent().drawType == 3:
 
                    brush = QBrush(self.parent().brushcolor)
 
                    self.items.clear()
                    rect = QRectF(self.start, self.end)
                    self.scene.addEllipse(rect, pen, brush)


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mainUI
import sys

import random

# import draw
    

class main_window():

    def __init__(self):

        self.answers = []
        self.correct_answer = ""
        self.i = 0
        self.voting = []
        self.maxi = 0


        app = QApplication(sys.argv)

        self.mainUI=mainUI.Ui_MainWindow()
        # self.drawUI=mainUI.CWidget()

        self.mainUI.MainWindow.show()

        # self.view = CView(self)
        # self.mainUI.right.addWidget(self.view)


        self.btnEvent()

        app.exec_()

    def btnEvent(self):
        self.mainUI.main_doumBtn.clicked.connect(self.clicked_doumBtn)

        self.mainUI.main_startBtn.clicked.connect(self.clicked_startBtn)
        self.mainUI.main_exitBtn.clicked.connect(self.clicked_exitBtn)
        
        self.mainUI.doum_gotoMain.clicked.connect(self.clicked_gotoMain)

        self.mainUI.setperson_okBtn.clicked.connect(self.clicked_setperson_okBtn)

        self.mainUI.keyword_jobBtn.clicked.connect(self.select_job)
        self.mainUI.keyword_foodBtn.clicked.connect(self.select_food)
        self.mainUI.keyword_objBtn.clicked.connect(self.select_obj)
        self.mainUI.keyword_idiomBtn.clicked.connect(self.select_idiom)
        self.mainUI.keyword_sayingBtn.clicked.connect(self.select_saying)
        self.mainUI.keyword_sportsBtn.clicked.connect(self.select_sports)
        self.mainUI.keyword_movieBtn.clicked.connect(self.select_movie)

        self.mainUI.setperson_setbutton.valueChanged.connect(self.spinBoxChanged)

        self.mainUI.curiosity_okBtn.clicked.connect(self.clicked_curiosity_okBtn)

        self.mainUI.mmy_label.setText(self.correct_answer)
        self.mainUI.mmy_label.repaint()
        self.mainUI.mmy_btn.clicked.connect(self.clicked_mmy)
        self.mainUI.artist_backBtn.clicked.connect(self.clicked_artist_backBtn)

        self.mainUI.vote_inputBtn.clicked.connect(self.clicked_inputBtn)

        self.mainUI.result_mysteryWin_inputBtn.clicked.connect(self.clicked_result_mysteryWin_inputBtn)


        self.mainUI.line.clicked.connect(self.radioclicked_line)
        self.mainUI.curve.clicked.connect(self.radioclicked_curve)
        self.mainUI.rectangle.clicked.connect(self.radioclicked_rectangle)
        self.mainUI.ellipse.clicked.connect(self.radioclicked_ellipse)

        self.mainUI.choose_color.clicked.connect(self.showColorDlg)
        self.mainUI.choose_brush.clicked.connect(self.showColorDlg)

        self.mainUI.eraser.stateChanged.connect(self.checkClicked)
        self.mainUI.erase_all.clicked.connect(self.eraseClicked)

        self.mainUI.finish.clicked.connect(self.drawFinished)

    def eraseClicked(self):
        for i in self.mainUI.view.scene.items():
            self.mainUI.view.scene.removeItem(i)

    def checkClicked(self):
        pass

    def showColorDlg(self):
        color = QColorDialog.getColor()
        sender = self.mainUI.sender()

        if sender == self.mainUI.choose_color and color.isValid():           
            self.mainUI.pencolor = color
            self.mainUI.choose_color.setStyleSheet('background-color: {}'.format( color.name()))
        else:
            self.mainUI.brushcolor = color
            self.mainUI.choose_brush.setStyleSheet('background-color: {}'.format( color.name()))

    def drawFinished(self):
            img = QPixmap(self.mainUI.view.grab(self.mainUI.view.sceneRect().toRect()))
            img.save('C:\\Users\\yygs3\\OneDrive\\Desktop\\파이썬기반응용프로그래밍\\추리반에 잠입한 화가\\image\\drawing.jpg')   
            self.close()

    def radioclicked_line(self):
        if self.mainUI.line.isChecked():
            self.mainUI.drawtype = 0

    def radioclicked_curve(self):
        if self.mainUI.curve.isChecked():
            self.mainUI.drawtype = 1

    def radioclicked_rectangle(self):
        if self.mainUI.rectangle.isChecked():
            self.mainUI.drawtype = 2

    def radioclicked_ellipse(self):
        if self.mainUI.ellipse.isChecked():
            self.mainUI.drawtype = 3

    def showModal(self):
            return super().exec_()  

    def draw(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.drawUI.PageDraw)

    def clicked_result_mysteryWin_inputBtn(self):
        text = self.mainUI.result_mysteryWin_input.text()

        if text == self.correct_answer:
            self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageArtistfinalWin)
        else:
            self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageMysteryfinalWin)

    def clicked_inputBtn(self):
        
        text = self.mainUI.vote_input.text()
        self.voting.append(int(text))
        self.mainUI.vote_input.clear()
        print(self.voting)

        if len(self.voting) == self.val:
            self.voteCount()
            print(self.max_num)

            if self.max_num == self.mafia:
                self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageMysteryWin)

            else:
                self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageArtistfinalWin)

    def voteCount(self):
        self.max_num = max(set(self.voting), key=self.voting.count)
        
    def clicked_mmy(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def clicked_artist_backBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def clicked_startdraw(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.draw)
    

    def clicked_doumBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageDoum)
        # self.hide()
        # self.doum_window = QDialog()
        # self.doum_window.exec()
        # self.show()

    def clicked_startBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageSetPerson)

    def clicked_exitBtn(self):
        self.mainUI.close()

    def clicked_gotoMain(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageMain)

    def clicked_setperson_okBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageKeyword)

        mafiaList = []
        for index in range(1,self.val+1):
            mafiaList.append(index)

        print(mafiaList)

        self.mafia = random.choice(mafiaList)

        # self.mafia = 4

        print("범인번호",self.mafia)

    def clicked_curiosity_okBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.Pagemmy)
        self.i += 1

        if self.i == self.mafia:
            self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageArtist)

        if self.i == self.val+1:
            self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageDraw)

    def clicked_mystery_backBtn(self):
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageKeyword)
        print("1")
        # self.i += 1

        # if self.i == 3:
        #     self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageArtist)




    def select_job(self):
        # self.load_job()
        self.answers = ["판사","조향사","영양사","공무원","가사도우미","댄서","가수","배우","성악가","유튜버","교사","인터넷 강사","플로리스트","여행가이드","감독","작가",
        "PD","한의사","의사","해녀","변호사","천문학자","교수","버스 운전사","디자이너","웹툰작가","과학자","간호사","개발자","경찰관","수의사","모델","바텐더","소방관","사서"]
        self.subject = "직업"
        self.correct_answer = random.choice(self.answers)

        # self.mainUI.mmy_label.setText("조향사")
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)
    
    def select_food(self):
        # self.load_food()
        self.answers = ["떡볶이","라면","볶음밥","김밥","비빔밥","덮밥","김치말이국수","칼국수","냉면","짜장면","잡채","떡","김치","갈비찜","떡갈비","육회","장조림","제육볶음",
        "보쌈","순대","닭갈비","닭강정","닭발","치킨","삼계탕","게장","매운탕","물회","계란말이","국밥","갈비탕","감자탕","된장찌개","김치찌개"]
        self.subject = "음식"
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def select_obj(self):
        # self.load_obj()
        self.answers = ["체온기","폴라로이드 사진","카메라","핸드폰","충전기","수석","샴푸","린스","에센스","대야","명함","향초","손난로","히터","에어컨","선풍기","전기장판",
        "안마의자","소파","티비","비데","수세미","냄비","밥솥","핸드크림","흔들의자","선크림","편지 봉투","수건","이어폰","노트북","볼펜","샤프","마우스","키오스크"]
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.subject = "사물"
        self.mainUI.artist_text.setText(self.subject)
        
        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def select_idiom(self):
        # self.load_idiom()
        self.answers = ["감언이설","감지덕지","갑론을박","개과천선","결초보은","고군분투","고진감래","과대망상","과유불급","구사일생","권선징악","근묵자흑","금의환향","금시초문",
        "기상천외","기진맥진","노심초사","다다익선","도원결의","동문서답","동상이몽","무념무상","무용지물","박장대소","반신반의","배은망덕","박발백중","선남선녀","설상가상","속수무책",
        "승승장구","아비규환","엄동설한","역지사지","유유상종","일취월장","자업자득","전광석화","전전긍긍","죽마고우","천진난만","칠전팔기","토사구팽","포복절도"]
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.subject = "사자성어"
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def select_saying(self):
        # self.load_saying()
        self.answers = ["호랑이도 제 말하면 온다","사촌이 땅을 사면 배가 아프다","다 된 죽에 코 빠뜨린다","아닌 밤중에 홍두깨","개구리 올챙이 적 생각 못 한다",
        "똥 묻은 개가 겨 묻은 개 나무란다","벼룩도 낯짝이 있다","가루는 칠수록 고와지고","말은 할수록 거칠어진다","우물 안 개구리","콩 심은 데 콩 나고 팥 심은 데 팥 난다",
        "어물전 망신은 꼴뚜기가 시킨다","쥐구멍에도 볕 들 날 있다","달면 삼키고 쓰면 뱉는다","사공이 많으면 배가 산으로 간다","먼 사촌보다 가까운 이웃이 낫다",
        "서당 개 삼 년에 풍월한다","다섯 손가락 깨물어서 아프지 않은 손가락이 없다","하룻강아지 범 무서운 줄 모른다","까마귀 날자 배 떨어진다","천 리 길도 한 걸음부터",
        "개똥도 약에 쓰려면 없다","낫 놓고 기역자도 모른다","누워서 떡 먹기","도둑이 제 발 저린다","닭 잡아먹고 오리발 내민다","등잔 밑이 어둡다","마른 하늘에 날벼락",
        "배보다 배꼽이 크다","뱁새가 황새 따라가면 다리가 찢어진다","비온 뒤 땅이 굳는다","오르지 못할 나무는 쳐다보지도 마라","원수는 외나무 다리에서 만난다",
        "벼는 익을수록 고개를 숙인다","고래 싸움에 새우등 터진다"]
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.subject = "속담"
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def select_sports(self):
        # self.load_sports()
        self.answers = ["마라톤","높이뛰기","멀리뛰기","축구","농구","배구","야구","당구","골프","배드민턴","테니스","수영","수구","태권도","유도","복싱","주짓수","스케이팅",
        "스키","스노우 보드","피구","킨볼","오래 달리기","등산","줄넘기","댄스","요가","필라테스","탁구","클라이밍"]
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.subject = "스포츠"
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def select_movie(self):
        # self.load_movie()
        self.answers = ["명량","극한직업","신과함께","국제시장","어벤져스","겨울왕국","아바타","베테랑","괴물","도둑들","7번방의 선물","암살","알라딘","광해 왕이 된 남자",
        "왕의 남자","택시 운전사","태극기 휘날리며","부산행","해운대","변호인","실미도","기생충","인터스텔라","보헤미안 랩소디","검사외전","엑시트","설국열차","관상","아이언맨",
        "해적","수상한 그녀","국가대표","백두산","스파이더맨","웰컴 투 동막골","공조","히말라야","미션임파서블","밀정","써니","1987","터널","럭키","은밀하게 위대하게","타짜",
        "늑대소년","군함도","전우치","킹스맨","레미제라블","청년경찰","쥬라기 월드","해리포터","반지의 제왕"]
        self.correct_answer = random.choice(self.answers)
        self.mainUI.mmy_label.setText(self.correct_answer)
        self.subject = "영화"
        self.mainUI.artist_text.setText(self.subject)

        self.mainUI.stackedWidget.setCurrentWidget(self.mainUI.PageCuriosity)

    def spinBoxChanged(self):
        self.val = self.mainUI.setperson_setbutton.value()
        print(self.val)


# class CView(QGraphicsView):
#     def __init__(self,parent):
#         super().__init__(parent)       
#         self.scene = QGraphicsScene()        
#         self.setScene(self.scene)
 
#         self.items = []
         
#         self.start = QPointF()
#         self.end = QPointF()
 
#         self.setRenderHint(QPainter.HighQualityAntialiasing)

#     def moveEvent(self, e):
#             rect = QRectF(self.rect())
#             rect.adjust(0,0,-2,-2)        

#     def mousePressEvent(self, e):
 
#             if e.button() == Qt.LeftButton:
#                 # 시작점 저장
#                 self.start = e.pos()
#                 self.end = e.pos()        
 
#     def mouseMoveEvent(self, e):  
         
#         # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴 
#         if e.buttons() & Qt.LeftButton:           
 
#             self.end = e.pos()
 
#             if self.main_window().checkbox.isChecked():
#                 pen = QPen(QColor(255,255,255), 10)
#                 path = QPainterPath()
#                 path.moveTo(self.start)
#                 path.lineTo(self.end)
#                 self.scene.addPath(path, pen)
#                 self.start = e.pos()
#                 return None
 
#             pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
#             # 직선 그리기
#             if self.parent().drawType == 0:
                 
#                 # 장면에 그려진 이전 선을 제거            
#                 if len(self.items) > 0:
#                     self.scene.removeItem(self.items[-1])
#                     del(self.items[-1])                
 
#                  # 현재 선 추가
#                 line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())                
#                 self.items.append(self.scene.addLine(line, pen))
 
#                 # 곡선 그리기
#             if self.parent().drawType == 1:

#                 print("1")
 
#                     # Path 이용
#                 path = QPainterPath()
#                 path.moveTo(self.start)
#                 path.lineTo(self.end)
#                 self.scene.addPath(path, pen)
 
#             # Line 이용
#             #line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
#             #self.scene.addLine(line, pen)
                 
#                 # 시작점을 다시 기존 끝점으로
#                 self.start = e.pos()
 
#             # 사각형 그리기
#             if self.parent().drawType == 2:
#                 brush = QBrush(self.parent().brushcolor)
 
#                 if len(self.items) > 0:
#                     self.scene.removeItem(self.items[-1])
#                     del(self.items[-1])
 
 
#                 rect = QRectF(self.start, self.end)
#                 self.items.append(self.scene.addRect(rect, pen, brush))
                 
#             # 원 그리기
#             if self.parent().drawType == 3:
#                 brush = QBrush(self.parent().brushcolor)
 
#                 if len(self.items) > 0:
#                     self.scene.removeItem(self.items[-1])
#                     del(self.items[-1])
 
 
#                 rect = QRectF(self.start, self.end)
#                 self.items.append(self.scene.addEllipse(rect, pen, brush))

#     def mouseReleaseEvent(self, e):        
 
#         if e.button() == Qt.LeftButton:
 
#             if self.parent().checkbox.isChecked():
#                 return None
 
#             pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex())
 
#             if self.parent().drawType == 0:
 
#                 self.items.clear()
#                 line = QLineF(self.start.x(), self.start.y(), self.end.x(), self.end.y())
                 
#                 self.scene.addLine(line, pen)
 
#             if self.parent().drawType == 2:
 
#                 brush = QBrush(self.parent().brushcolor)
 
#                 self.items.clear()
#                 rect = QRectF(self.start, self.end)
#                 self.scene.addRect(rect, pen, brush)
 
#             if self.parent().drawType == 3:
 
#                 brush = QBrush(self.parent().brushcolor)
 
#                 self.items.clear()
#                 rect = QRectF(self.start, self.end)
#                 self.scene.addEllipse(rect, pen, brush)
    

        
# class doum_window(QMainWindow, doum_window_ui):

#     def __init__(self):
#         super(doum_window, self).__init__()
#         self.initUi()
#         self.show()

        

#     def initUi(self):
#         self.setupUi(self)
#         self.doum_gotoMain.clicked.connect(self.clicked_gotoMain)

#     def clicked_gotoMain(self):
#         self.close()

if __name__ == '__main__':
    myWindow = main_window()
    #myWindow.setWindowTitle('추리반에 잠입한 화가')

    
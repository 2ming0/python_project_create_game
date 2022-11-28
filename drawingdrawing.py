import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import main_window
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
"""class draw():
    def __init__(self):
        super(draw,self).__init__()
        self.CWidget()
        self.show()"""

    
class CWidget(QWidget): 

        def __init__(self):
            super().__init__()
            self.initUI()

        def close_drawpage(self):
            self.close()
 
        def initUI(self):
            # 전체 폼 박스
            formbox = QHBoxLayout()
            self.setLayout(formbox)
 
            # 좌, 우 레이아웃박스
            left = QVBoxLayout()
            right = QVBoxLayout()
 
            # 그룹박스1 생성 및 좌 레이아웃 배치
            gb = QGroupBox('그리기 종류')        
            left.addWidget(gb)
 
            # 그룹박스1 에서 사용할 레이아웃
            box = QVBoxLayout()
            gb.setLayout(box)        
 
            # 그룹박스 1 의 라디오 버튼 배치
            text = ['line', 'Curve', 'Rectange', 'Ellipse']
            self.radiobtns = []
 
            for i in range(len(text)):
                self.radiobtns.append(QRadioButton(text[i], self))
                self.radiobtns[i].clicked.connect(self.radioClicked)
                box.addWidget(self.radiobtns[i])
 
            self.radiobtns[0].setChecked(True)
            self.drawType = 0
         
            # 그룹박스2
            gb = QGroupBox('펜 설정')        
            left.addWidget(gb)        
 
            grid = QGridLayout()      
            gb.setLayout(grid)        
 
            label = QLabel('선굵기')
            grid.addWidget(label, 0, 0)
 
            self.combo = QComboBox()
            grid.addWidget(self.combo, 0, 1)       
 
            for i in range(1, 21):
                self.combo.addItem(str(i))
 
            label = QLabel('선색상')
            grid.addWidget(label, 1,0)        
         
            self.pencolor = QColor(0,0,0)
            self.penbtn = QPushButton()        
            self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
            self.penbtn.clicked.connect(self.showColorDlg)
            grid.addWidget(self.penbtn,1, 1)
         
 
            # 그룹박스3
            gb = QGroupBox('붓 설정')        
            left.addWidget(gb)
 
            hbox = QHBoxLayout()
            gb.setLayout(hbox)
 
            label = QLabel('붓색상')
            hbox.addWidget(label)                
 
            self.brushcolor = QColor(255,255,255)
            self.brushbtn = QPushButton()        
            self.brushbtn.setStyleSheet('background-color: rgb(255,255,255)')
            self.brushbtn.clicked.connect(self.showColorDlg)
            hbox.addWidget(self.brushbtn)
 
            # 그룹박스4
            gb = QGroupBox('지우개')        
            left.addWidget(gb)
 
            hbox = QHBoxLayout()
            gb.setLayout(hbox)        
         
            self.checkbox  = QCheckBox('지우개')
            self.checkbox.stateChanged.connect(self.checkClicked)
            hbox.addWidget(self.checkbox)

            self.erasebtn = QPushButton('모두 지우기')
            self.erasebtn.clicked.connect(self.eraseClicked)
            hbox.addWidget(self.erasebtn)

            #그룹박스5
            gb = QGroupBox('그리기 완료')
            left.addWidget(gb)

            hbox = QHBoxLayout()
            gb.setLayout(hbox)

            self.draw_finishbtn = QPushButton('완료')

            self.count = 1
            self.draw_finishbtn.clicked.connect(self.drawFinished)
            hbox.addWidget(self.draw_finishbtn)

            subLayout = QHBoxLayout()

            left.addStretch(1)        
          
            # 우 레이아웃 박스에 그래픽 뷰 추가
            self.view = CView(self)       
            right.addWidget(self.view)        
 
            # 전체 폼박스에 좌우 박스 배치
            formbox.addLayout(left)
            formbox.addLayout(right)
 
            formbox.setStretchFactor(left, 0)
            formbox.setStretchFactor(right, 1)
         
            self.setGeometry(100, 100, 800, 500) 


        def radioClicked(self):
            for i in range(len(self.radiobtns)):
                if self.radiobtns[i].isChecked():
                    self.drawType = i                
                    break
 
        def checkClicked(self):
            pass
             
        def eraseClicked(self):
            for i in self.view.scene.items():
                self.view.scene.removeItem(i)



        def showColorDlg(self):       
         
            # 색상 대화상자 생성      
            color = QColorDialog.getColor()
 
            sender = self.sender()
 
            # 색상이 유효한 값이면 참, QFrame에 색 적용
            if sender == self.penbtn and color.isValid():           
                self.pencolor = color
                self.penbtn.setStyleSheet('background-color: {}'.format( color.name()))
            else:
                self.brushcolor = color
                self.brushbtn.setStyleSheet('background-color: {}'.format( color.name()))

        def showModal(self):
            return super().exec_()

        def drawFinished(self):
            if self.count == 1:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing1.jpg') 
                self.count += 1  
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
            elif self.count == 2:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing2.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 3:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing3.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 4:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing4.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 5:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing5.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 6:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing6.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 7:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing7.jpg')   
                for i in self.view.scene.items():
                    self.view.scene.removeItem(i)
                self.count += 1

            elif self.count == 8:
                img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))
                img.save('C:\\Users\\betty\\OneDrive\\바탕 화면\\추리반에 잠입한 화가\\drawing8.jpg')   
                self.close()


                                       
    # QGraphicsView display QGraphicsScene
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
 
                if self.parent().checkbox.isChecked():
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
 
                if self.parent().checkbox.isChecked():
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
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())
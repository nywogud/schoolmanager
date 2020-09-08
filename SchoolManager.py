import sys
import re

from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.total_rank = []
        self.sub1_rank = []
        self.sub2_rank = []
        self.sub3_rank = []
        self.sub4_rank = []

    def initUI(self):

        self.label1 = QLabel('성명', self)
        self.label1.move(20, 13)
        self.qle1 = QLineEdit(self)
        self.qle1.move(60, 9)
        self.qle1.resize(80, 20)
        self.label1_1 = QLabel('※ \'Tab\'키를 눌러 이동합니다.', self)
        self.label1_1.move(165, 14)

        self.label2 = QLabel('언어영역', self)
        self.label2.move(20, 53)
        self.qle2 = QLineEdit(self)
        self.qle2.move(100, 49)
        self.qle2.resize(80, 20)

        self.label3 = QLabel('수리영역', self)
        self.label3.move(200, 53)
        self.qle3 = QLineEdit(self)
        self.qle3.move(270, 49)
        self.qle3.resize(80, 20)

        self.label4 = QLabel('사회탐구영역', self)
        self.label4.move(20, 93)
        self.qle4 = QLineEdit(self)
        self.qle4.move(100, 89)
        self.qle4.resize(80, 20)

        self.label5 = QLabel('외국어영역', self)
        self.label5.move(200, 93)
        self.qle5 = QLineEdit(self)
        self.qle5.move(270, 89)
        self.qle5.resize(80, 20)

        self.label6 = QLabel('※ 성적란에는 소수 값 포함 숫자만 입력하세요.', self)
        self.label6.move(95, 128)

        self.btn = QPushButton('저장', self)
        self.btn.move(20, 150)
        self.btn.resize(100, 25)
        self.btn.clicked.connect(self.input_data)

        self.btn14 = QPushButton('수정', self)
        self.btn14.move(130, 150)
        self.btn14.resize(100, 25)
        self.btn14.setToolTip("데이터를 수정하려는 경우 학생 이름을 성명란에, 점수를 성적란에 모두 입력 후 \'수정\' 버튼을 누르세요.")
        self.btn14.clicked.connect(self.amend_input_data)

        self.label14 = QLabel('데이터 삭제 : ', self)
        self.label14.move(20, 200)

        self.label15 = QLabel('이름', self)
        self.label15.move(100, 200)
        self.qle6 = QLineEdit(self)
        self.qle6.move(140, 195)
        self.qle6.resize(80, 20)

        self.btn15 = QPushButton('데이터 삭제하기', self)
        self.btn15.move(235, 192)
        self.btn15.resize(108, 25)
        self.btn15.clicked.connect(self.delete_data)
        self.btn15.setToolTip("자료를 삭제할 경우 성명란에 학생이름만 입력 후 \'데이터 삭제하기\' 버튼을 누르세요.")

        self.btn1 = QPushButton('통계 보기', self)
        self.btn1.move(240, 150)
        self.btn1.resize(100, 25)
        self.btn1.clicked.connect(self.statistic)

        self.setWindowTitle('성적관리')
        self.move(100, 100)
        self.setFixedSize(370, 240)
        self.show()

    def input_data(self):

        # 하나라도 빈문자열인 경우
        if self.qle1.text() == '' or self.qle2.text() == '' or self.qle3.text() == '' or self.qle4.text() == '' or self.qle5.text() == '':
            self.qmb1 = QMessageBox()
            self.qmb1.setWindowTitle("알림창")
            self.qmb1.setIcon(QMessageBox.Information)
            self.qmb1.setText("입력오류")
            self.qmb1.setInformativeText("성명란 혹은 모든 성적란에 자료를 입력하지 않았습니다.")
            self.qmb1.exec_()

        # 소수점 대신 콤마(,)를 사용한 경우
        elif self.qle2.text().find(',') != -1 or self.qle3.text().find(',') != -1 or self.qle4.text().find(
                ',') != -1 or self.qle5.text().find(',') != -1:
            self.qmb2 = QMessageBox()
            self.qmb2.setWindowTitle("알림창")
            self.qmb2.setIcon(QMessageBox.Information)
            self.qmb2.setText("입력오류")
            self.qmb2.setInformativeText("성적란에 입력된 점수가 콤마(,)를 포함하고 있습니다. 소수점을 정확히 입력하세요.")
            self.qmb2.exec_()

        # 성적란에 숫자가 아닌 문자를 입력한 경우
        elif bool(re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle2.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle3.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle4.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle5.text())):
            self.qmb3 = QMessageBox()
            self.qmb3.setWindowTitle("알림창")
            self.qmb3.setIcon(QMessageBox.Information)
            self.qmb3.setText("입력오류")
            self.qmb3.setInformativeText("성적란에 숫자와 소수점 이외의 값을 입력했습니다.")
            self.qmb3.exec_()

        else:

            try:

                self.file = open("C:\\schoolmanager.txt", 'r', encoding='utf8')
                self.line2 = self.file.readline()
                self.file.close()

                self.line2_list = self.line2.split(',')
                self.line2_list.pop(-1)

                if self.line2_list[self.line2_list.index(self.qle1.text())] == self.qle1.text():

                    self.qmb10 = QMessageBox()
                    self.qmb10.setWindowTitle("알림창")
                    self.qmb10.setIcon(QMessageBox.Information)
                    self.qmb10.setText("입력오류")
                    self.qmb10.setInformativeText("같은 이름의 학생 데이터가 이미 저장돼 있습니다.")
                    self.qmb10.exec_()

                else:
                    f = open("C:\\schoolmanager.txt", 'a', encoding='utf8')
                    content = "{},{},{},{},{},".format(self.qle1.text(), self.qle2.text(), self.qle3.text(),self.qle4.text(), self.qle5.text())
                    f.write(content)
                    f.close()

                    self.qmb14 = QMessageBox()
                    self.qmb14.setWindowTitle("알림창")
                    self.qmb14.setText("저장완료")
                    self.qmb14.setInformativeText("자료 저장이 완료됐습니다. \'통계보기\' 버튼을 눌러 성적을 확인하세요. ")
                    self.qmb14.exec_()

            except:

                try:

                    f = open("C:\\schoolmanager.txt", 'a', encoding='utf8')
                    content = "{},{},{},{},{},".format(self.qle1.text(), self.qle2.text(), self.qle3.text(),self.qle4.text(), self.qle5.text())
                    f.write(content)
                    f.close()

                    self.qmb16 = QMessageBox()
                    self.qmb16.setWindowTitle("알림창")
                    self.qmb16.setText("저장완료")
                    self.qmb16.setInformativeText("자료 저장이 완료됐습니다. \'통계보기\' 버튼을 눌러 성적을 확인하세요. ")
                    self.qmb16.exec_()

                except:

                    f = open("C:\\schoolmanager.txt", 'w', encoding='utf8')
                    content = "{},{},{},{},{},".format(self.qle1.text(), self.qle2.text(), self.qle3.text(), self.qle4.text(), self.qle5.text())
                    f.write(content)
                    f.close()

                    self.qmb16 = QMessageBox()
                    self.qmb16.setWindowTitle("알림창")
                    self.qmb16.setText("저장완료")
                    self.qmb16.setInformativeText("자료 저장이 완료됐습니다. \'통계보기\' 버튼을 눌러 성적을 확인하세요. ")
                    self.qmb16.exec_()


    def statistic(self):

        try:
            self.readfile = open("C:\\schoolmanager.txt", 'r', encoding='utf8')
            data_temp = self.readfile.readline()  # 파일 읽어오기
            self.readfile.close()
            list = []

            data = data_temp
            list = data.split(',')  # 문자열을 리스트로 변환
            list.pop(-1)

            list_1 = []
            for i in range(len(list)):  # 2차원 리스트로 전환
                if i % 5 == 0:
                    list_1.append(
                        [list[i], float(list[i + 1]), float(list[i + 2]), float(list[i + 3]), float(list[i + 4])])

            sub1 = []  # 언어영역
            sub2 = []  # 수리영역
            sub3 = []  # 사회탐구영역
            sub4 = []  # 외국어영역

            for i in range(len(list_1)):
                sub1.append([list_1[i][0], list_1[i][1]])  # sub1 = [['학생',sub1 점수],...] 2차원 배열
                sub2.append([list_1[i][0], list_1[i][2]])  # sub2 = [['학생',sub2 점수],...] 2차원 배열
                sub3.append([list_1[i][0], list_1[i][3]])  # sub3 = [['학생',sub3 점수],...] 2차원 배열
                sub4.append([list_1[i][0], list_1[i][4]])  # sub4 = [['학생',sub4 점수],...] 2차원 배열

            temp = []  # 전과목 평균
            for j in range(len(list_1)):
                temp.append([list_1[j][0], round((list_1[j][1] + list_1[j][2] + list_1[j][3] + list_1[j][4]) / 4,
                                                 2)])  # temp = [['학생', 전과목 평균],....]

            self.total_rank = self.rank(
                temp)  # self.total_rank = [[김아무개, 전과목 평균, 등수], ...[하아무개, 전과목 평균, 등수, 총원]] 총원 : self.total_rank[-1][-1]
            self.sub1_rank = self.rank(
                sub1)  # self.sub1_rank = [[김아무개, 국어, 등수], ...[하아무개, 국어 성적, 등수, 총원]] 총원 : self.sub1_rank[-1][-1]
            self.sub2_rank = self.rank(
                sub2)  # self.sub2_rank = [[김아무개, 수리, 등수], ...[하아무개, 수학 성적, 등수, 총원]] 총원 : self.sub2_rank[-1][-1]
            self.sub3_rank = self.rank(
                sub3)  # self.sub3_rank = [[김아무개, 사회, 등수], ...[하아무개, 사회 성적, 등수, 총원]] 총원 : self.sub3_rank[-1][-1]
            self.sub4_rank = self.rank(
                sub4)  # self.sub4_rank = [[김아무개, 영어, 등수], ...[하아무개, 영어 성적, 등수, 총원]] 총원 : self.sub4_rank[-1][-1]

            # 등수 - 숫자를 문자로 표현해 라벨에 넣기

            self.ex_1 = MyApp_1()

        except:

            self.qmb13 = QMessageBox()
            self.qmb13.setWindowTitle("알림창")
            self.qmb13.setIcon(QMessageBox.Information)
            self.qmb13.setText("오류발생")
            self.qmb13.setInformativeText("저장된 자료가 없어 통계를 확인할 수 없습니다. 자료를 먼저 입력하세요.")
            self.qmb13.exec_()

    def rank(self, lst):

        for x in range(len(lst)):
            indicator = 1
            for y in range(len(lst)):

                if lst[y][1] > lst[x][1]:
                    indicator = indicator + 1

            lst[x].insert(2, indicator)
        people = len(lst)
        lst[x].insert(3, people)
        return lst

    def amend_input_data(self):

        if self.qle1.text() == '' or self.qle2.text() == '' or self.qle3.text() == '' or self.qle4.text() == '' or self.qle5.text() == '':

            self.qmb5 = QMessageBox()
            self.qmb5.setWindowTitle("알림창")
            self.qmb5.setIcon(QMessageBox.Information)
            self.qmb5.setText("입력오류")
            self.qmb5.setInformativeText("성명란 혹은 모든 성적란에 자료를 입력하지 않았습니다.")
            self.qmb5.exec_()

        elif self.qle2.text().find(',') != -1 or self.qle3.text().find(',') != -1 or self.qle4.text().find(
                ',') != -1 or self.qle5.text().find(',') != -1:

            self.qmb6 = QMessageBox()
            self.qmb6.setWindowTitle("알림창")
            self.qmb6.setIcon(QMessageBox.Information)
            self.qmb6.setText("입력오류")
            self.qmb6.setInformativeText("성적란에 입력된 점수가 콤마(,)를 포함하고 있습니다. 소수점을 정확히 입력하세요.")
            self.qmb6.exec_()

        elif bool(re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle2.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle3.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle4.text())) or bool(
                re.sub('[^`~!@#$%^&*()_+\-=\\\|{}\"\'\[\]a-zA-Zㄱ-힗]', '', self.qle5.text())):

            self.qmb7 = QMessageBox()
            self.qmb7.setWindowTitle("알림창")
            self.qmb7.setIcon(QMessageBox.Information)
            self.qmb7.setText("입력오류")
            self.qmb7.setInformativeText("성적란에 숫자와 소수점 이외의 값을 입력했습니다.")
            self.qmb7.exec_()

        else:
            try:

                f = open("C:\\schoolmanager.txt", 'r', encoding='utf8')
                self.line = f.readline()
                f.close()
                self.line_1 = self.line.split(',')
                self.line_1.pop(-1)

                self.checkbool = True

                for h in range(len(self.line_1)):
                    if self.line_1[h] == self.qle1.text():
                        # a[a.index('바꿀 문자')] = '바뀐 문자'
                        self.line_1[self.line_1.index(self.qle1.text()) + 1] = self.qle2.text()
                        self.line_1[self.line_1.index(self.qle1.text()) + 2] = self.qle3.text()
                        self.line_1[self.line_1.index(self.qle1.text()) + 3] = self.qle4.text()
                        self.line_1[self.line_1.index(self.qle1.text()) + 4] = self.qle5.text()

                        self.newline = ''
                        for n in range(len(self.line_1)):
                            self.newline_temp = "{},".format(self.line_1[n])
                            self.newline += self.newline_temp

                        f = open("C:\\schoolmanager.txt", 'w', encoding='utf8')  # 파일 새로 쓰기
                        f.write(self.newline)
                        f.close()

                        self.qmb9 = QMessageBox()
                        self.qmb9.setWindowTitle("알림창")
                        self.qmb9.setText("저장완료")
                        self.qmb9.setInformativeText("자료 저장이 완료됐습니다. \'통계보기\' 버튼을 눌러 성적을 확인하세요. ")
                        self.qmb9.exec_()
                        self.checkbool = False
                        break

                if self.checkbool:
                    self.qmb8 = QMessageBox()
                    self.qmb8.setWindowTitle("알림창")
                    self.qmb8.setIcon(QMessageBox.Information)
                    self.qmb8.setText("입력오류")
                    self.qmb8.setInformativeText("찾고자 하는 학생이 없습니다. 통계보기를 다시 참조하세요.")
                    self.qmb8.exec_()

            except:
                self.qmb17 = QMessageBox()
                self.qmb17.setWindowTitle("알림창")
                self.qmb17.setIcon(QMessageBox.Information)
                self.qmb17.setText("입력오류")
                self.qmb17.setInformativeText("저장된 데이터가 없습니다. 먼저 자료를 입력하세요.")
                self.qmb17.exec_()

    def delete_data(self):

        try:

            if self.qle6.text() == '':

                self.qmb5 = QMessageBox()
                self.qmb5.setWindowTitle("알림창")
                self.qmb5.setIcon(QMessageBox.Information)
                self.qmb5.setText("입력오류")
                self.qmb5.setInformativeText("성명란에 삭제할 학생 이름을 입력하지 않았습니다.")
                self.qmb5.exec_()

            else:

                f = open("C:\\schoolmanager.txt", 'r', encoding='utf8')
                self.line3 = f.readline()
                f.close()

                if self.line3.find(self.qle6.text()) == -1:

                    self.qmb11 = QMessageBox()
                    self.qmb11.setWindowTitle("알림창")
                    self.qmb11.setIcon(QMessageBox.Information)
                    self.qmb11.setText("입력오류")
                    self.qmb11.setInformativeText("찾고자 하는 학생이 없습니다. 통계보기를 다시 참조하세요.")
                    self.qmb11.exec_()

                else:

                    self.line3_1 = self.line3.split(',')
                    self.line3_1.pop(-1)
                    # del a[a.index('1')+1] 리스트 요소 삭제
                    del self.line3_1[self.line3_1.index(self.qle6.text()) + 1]
                    del self.line3_1[self.line3_1.index(self.qle6.text()) + 1]
                    del self.line3_1[self.line3_1.index(self.qle6.text()) + 1]
                    del self.line3_1[self.line3_1.index(self.qle6.text()) + 1]
                    del self.line3_1[self.line3_1.index(self.qle6.text())]

                    self.newline3_1 = ''
                    for n in range(len(self.line3_1)):
                        self.newline3_temp = "{},".format(self.line3_1[n])
                        self.newline3_1 += self.newline3_temp

                    f = open("C:\\schoolmanager.txt", 'w', encoding='utf8')  # 파일 새로 쓰기
                    f.write(self.newline3_1)
                    f.close()

                    self.qmb12 = QMessageBox()
                    self.qmb12.setWindowTitle("알림창")
                    self.qmb12.setText("삭제완료")
                    self.qmb12.setInformativeText("데이터를 삭제하고 저장을 완료했습니다.")
                    self.qmb12.exec_()
        except:

            self.qmb15 = QMessageBox()
            self.qmb15.setWindowTitle("알림창")
            self.qmb15.setIcon(QMessageBox.Information)
            self.qmb15.setText("입력오류")
            self.qmb15.setInformativeText("저장된 학생 데이터가 없습니다. 자료를 먼저 입력하세요.")
            self.qmb15.exec_()


class MyApp_1(MyApp):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.top(), 0, 0)
        self.grid.addWidget(self.middle(), 1, 0)
        self.grid.addWidget(self.bottom(), 2, 0, 10, 1)

        self.setLayout(self.grid)

        self.setWindowTitle('통계보기')
        self.move(473, 100)
        self.setFixedSize(900, 240)
        self.show()

    def top(self):

        self.group1 = QGroupBox(self)

        self.labelPeople = QLabel(self)
        self.tempo = '총원  :  ' + str(ex.total_rank[-1][-1]) + '    명'
        self.labelPeople.setText(self.tempo)

        self.hbox1 = QHBoxLayout(self)
        self.hbox1.addStretch(20)
        self.hbox1.addWidget(self.labelPeople)
        self.hbox1.addStretch(1)

        self.group1.setLayout(self.hbox1)

        return self.group1

    def middle(self):

        self.group2 = QGroupBox(self)

        self.label7 = QLabel('이름', self)

        self.label8 = QLabel('언어영역\n(석차)', self)

        self.label9 = QLabel('수리영역\n(석차)', self)

        self.label10 = QLabel('사회탐구영역\n(석차)', self)

        self.label11 = QLabel('외국어영역\n(석차)', self)

        self.label12 = QLabel('평균', self)

        self.label13 = QLabel('전체 석차', self)

        self.hbox2 = QHBoxLayout(self)
        self.hbox2.addWidget(self.label7)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label8)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label9)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label10)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label11)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label12)
        # self.hbox2.addStretch(0)
        self.hbox2.addWidget(self.label13)
        # self.hbox2.addStretch(0)

        self.group2.setLayout(self.hbox2)

        return self.group2

    def bottom(self):

        self.group3 = QGroupBox(self)

        # # 라벨 변수 리스트 길이 만큼 자동 생성
        #
        # # 이름 - Done
        self.temp_name_t = ''
        self.temp_name = QLabel(self)
        for i in range(len(ex.total_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab1 = a
            # self.lab1 = QLabel(self)
            # self.lab1.move(20, (80 + (i * 20)))
            # self.lab1.setText(ex.total_rank[i][0])
            self.temp_name_t += ex.total_rank[i][0] + '\n'
            self.temp_name.setText(self.temp_name_t)

        # 국어
        self.temp_sub1_t = ''
        self.temp_sub1 = QLabel(self)
        for i in range(len(ex.sub1_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab2 = a
            # self.lab2 = QLabel(self)
            # self.lab2.move(80, (80 + (i * 20)))
            # self.lab2.setText(str(ex.sub1_rank[i][1]) + '(' + str(ex.sub1_rank[i][2]) + ')')
            self.temp_sub1_t += str(ex.sub1_rank[i][1]) + '(' + str(ex.sub1_rank[i][2]) + ')\n'
            self.temp_sub1.setText(self.temp_sub1_t)

        # 수학
        self.temp_sub2_t = ''
        self.temp_sub2 = QLabel(self)
        for i in range(len(ex.sub2_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab3 = a
            # self.lab3 = QLabel(self)
            # self.lab3.move(240, (80 + (i * 20)))
            # self.lab3.setText(str(ex.sub2_rank[i][1]) + '(' + str(ex.sub2_rank[i][2]) + ')')
            self.temp_sub2_t += str(ex.sub2_rank[i][1]) + '(' + str(ex.sub2_rank[i][2]) + ')\n'
            self.temp_sub2.setText(self.temp_sub2_t)

        # 사회
        self.temp_sub3_t = ''
        self.temp_sub3 = QLabel(self)
        for i in range(len(ex.sub3_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab4 = a
            # self.lab4 = QLabel(self)
            # self.lab4.move(400, (80 + (i * 20)))
            # self.lab4.setText(str(ex.sub2_rank[i][1]) + '(' + str(ex.sub2_rank[i][2]) + ')')
            self.temp_sub3_t += str(ex.sub3_rank[i][1]) + '(' + str(ex.sub3_rank[i][2]) + ')\n'
            self.temp_sub3.setText(self.temp_sub3_t)

        # 영어
        self.temp_sub4_t = ''
        self.temp_sub4 = QLabel(self)
        for i in range(len(ex.sub4_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab5 = a
            # self.lab5 = QLabel(self)
            # self.lab5.move(580, (80 + (i * 20)))
            # self.lab5.setText(str(ex.sub2_rank[i][1]) + '(' + str(ex.sub2_rank[i][2]) + ')')
            self.temp_sub4_t += str(ex.sub4_rank[i][1]) + '(' + str(ex.sub4_rank[i][2]) + ')\n'
            self.temp_sub4.setText(self.temp_sub4_t)

        # 평균
        self.temp_avg_t = ''
        self.temp_avg = QLabel(self)
        for i in range(len(ex.total_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab6 = a
            # self.lab6 = QLabel(self)
            # self.lab6.move(730, (80 + (i * 20)))
            # self.lab6.setText(str(ex.total_rank[i][1]))
            self.temp_avg_t += str(ex.total_rank[i][1]) + '\n'
            self.temp_avg.setText(self.temp_avg_t)

        # 전과목 석차
        self.temp_grd_t = ''
        self.temp_grd = QLabel(self)
        for i in range(len(ex.total_rank)):
            # a = 'var'
            # a = a + str(i)
            # self.lab7 = a
            # self.lab7 = QLabel(self)
            # self.lab7.move(780, (80 + (i * 20)))
            # self.lab7.setText(str(ex.total_rank[i][2]))
            self.temp_grd_t += str(ex.total_rank[i][2]) + '\n'
            self.temp_grd.setText(self.temp_grd_t)

        self.hbox3 = QHBoxLayout(self)

        self.hbox3.addWidget(self.temp_name)
        self.hbox3.addWidget(self.temp_sub1)
        self.hbox3.addWidget(self.temp_sub2)
        self.hbox3.addWidget(self.temp_sub3)
        self.hbox3.addWidget(self.temp_sub4)
        self.hbox3.addWidget(self.temp_avg)
        self.hbox3.addWidget(self.temp_grd)

        self.vbox1 = QVBoxLayout(self)
        self.vbox1.addStretch(1)
        self.vbox1.addLayout(self.hbox3)
        self.vbox1.addStretch(30)

        self.group3.setLayout(self.vbox1)

        self.scr = QScrollArea(self)
        self.scr.setWidget(self.group3)
        self.scr.setWidgetResizable(True)
        self.scr.setFixedWidth(878)

        return self.scr


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


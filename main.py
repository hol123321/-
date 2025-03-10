'''Головний файл'''
from PyQt5.QtWidgets import QApplication
app = QApplication([])
from main_window import *
from menu_window import *
from random import shuffle, choice
from time import sleep

#оголошуємо клас
class Question:
    #створення конструктору
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        #створюємо властивості
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.actual = True
        self.count_ask = 0 
        self.count_correct = 0
    #методи класу
    def got_right(self):
        self.count_ask += 1
        # self.count_ask = self.count_ask + 1
        self.count_correct += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Як перекладається слово apple?','яблуко','груша','машина','дерево')
q2 = Question('Як перекладається слово car?','машина','перо','качка','камінь')
q3 = Question('Як перекладається слово sun?','сонце','син','небо','дорога')
q4 = Question('Як перекладається слово cat?','кіт','папуга','шапка','пісок')

radio_buttons = [rbtn1, rbtn2, rbtn3, rbtn4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    radio_group.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_correct.text():
                cur_q.got_right()
                lb_result.setText('Молодець! Відповів вірно!')
                answer.setChecked(False)
                break
            else:
                lb_result.setText('хаха неправильно!')
                cur_q.got_wrong()
                answer.setChecked(False)
        else:
            lb_result.setText('хаха неправильно!')


    radio_group.setExclusive(True)      

def click_ok():
    if btn_ok.text() == 'Відповісти':
        check()
        radio_gb.hide()
        ans_gb.show()

        btn_ok.setText('Наступне запитання')

    else:
        new_question()
        radio_gb.show()
        ans_gb.hide()

        btn_ok.setText('Відповісти')

btn_ok.clicked.connect(click_ok)

def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_correct/cur_q.count_ask)*100

    text = f'Разів відповіли: {cur_q.count_ask}\n'\
            f'Вірних відповідей: {cur_q.count_correct}\n'\
            f'Успішність: {round(c, 2)}%'
    lb_stat.setText(text)
    menu_win.show()
    window_card.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    window_card.show()
    menu_win.hide()

btn_back.clicked.connect(back_menu)

def rest():
    window_card.hide()
    n = box_min.value()
    sleep(n)
    window_card.show()

btn_sleep.clicked.connect(rest)

app.exec_()
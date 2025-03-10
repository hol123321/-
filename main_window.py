'''Файл інтерфейс для головного вікна'''
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,\
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel,\
    QSpinBox
from PyQt5.QtCore import Qt
from random import shuffle # для перемішування відповідей

# створюємо вікно
window_card = QWidget()
window_card.resize(600,500)
window_card.setWindowTitle('Memory Card')

# створюємо віджети
btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочити')
btn_ok = QPushButton('Відповісти')
box_min = QSpinBox() # к-сть хв для відпочинку
box_min.setValue(5)
lb_question = QLabel('') # текст для запитання

# панель із запитаннями
radio_gb = QGroupBox('Варіанти відповіді')
radio_group = QButtonGroup()

rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')
radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)

# панель із результатом
ans_gb = QGroupBox('Результат тесту')
lb_result = QLabel('') # надпис правильно чи неправ.
lb_correct = QLabel('') # правильний вар. з відповіддю

# розміщаємо об'єкти на направляючих лініях
# розм. варіанти відповідей
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
# до н. л. додаємо кнопки
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radio_gb.setLayout(layout_ans1)

# розташовуємо результат
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result,
                        alignment=(Qt.AlignTop | Qt.AlignLeft))
layout_result.addWidget(lb_correct,
                        alignment=(Qt.AlignCenter), stretch=2)
ans_gb.setLayout(layout_result)
ans_gb.hide()

# створюємо та добавляємо всі інші віджети
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_min)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_question, alignment=(Qt.AlignCenter))
layout_line3.addWidget(radio_gb)
layout_line3.addWidget(ans_gb)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_ok, stretch=2)
layout_line4.addStretch(1)

# головна н.л.
layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1, stretch= 1)
layout_main.addLayout(layout_line2, stretch= 2)
layout_main.addLayout(layout_line3, stretch= 8)
layout_main.addLayout(layout_line4)

window_card.setLayout(layout_main)



window_card.show()
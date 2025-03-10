from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,\
    QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel,\
    QSpinBox, QLineEdit
from PyQt5.QtCore import Qt

menu_win = QWidget()

lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:') 
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь:')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь:')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь:')

le_quest = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel('Статистика:')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
lb_stat = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_LineEdits = QVBoxLayout()
vl_LineEdits.addWidget(le_quest)
vl_LineEdits.addWidget(le_right_ans)
vl_LineEdits.addWidget(le_wrong_ans1)
vl_LineEdits.addWidget(le_wrong_ans2)
vl_LineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_LineEdits)

btn_back = QPushButton('Назад')
btn_add_quest = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_quest)
hl_buttons.addWidget(btn_clear)

vl_main = QVBoxLayout()
vl_main.addLayout(hl_question)
vl_main.addLayout(hl_buttons)
vl_main.addWidget(lb_header_stat)
vl_main.addWidget(lb_stat)
vl_main.addWidget(btn_back)

menu_win.setLayout(vl_main)
menu_win.resize(400,300)
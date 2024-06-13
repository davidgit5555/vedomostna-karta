from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QHBoxLayout, 
                             QVBoxLayout, 
                             QGroupBox, 
                             QButtonGroup, 
                             QRadioButton, 
                             QPushButton, 
                             QLabel)

# hlavne nastavenie aplikacie
app = QApplication([])
# tlacidlo pre odpoved
btn_OK = QPushButton('Odpoveď')
# menovka s otazkou
lb_Question = QLabel('Najťašia otázka na svete!')

# skupina pre tlacidka moznosti (sivy ramcek)
RadioGroupBox = QGroupBox("Možnosti odpovede")
# tlacidla moznosti
rbtn_1 = QRadioButton('Odpoved 1')
rbtn_2 = QRadioButton('Odpoved 2')
rbtn_3 = QRadioButton('Odpoved 3')
rbtn_4 = QRadioButton('Odpoved 4')

# kontajner pre skupinu tlacidiel
RadioGroup = QButtonGroup()
# pridanie tlacidiel do kontajneru
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

# horiyontalne rozlozenie pre panel s moznostami
layout_ans1 = QHBoxLayout()   
# vertikalne rozlozenie pre panel s moznostami(1 a 2 tlacidlo) 
layout_ans2 = QVBoxLayout() 
# vertikalne rozlozenie pre panel s moznostami(3 a 4 tlacidlo) 
layout_ans3 = QVBoxLayout()

# pripojenie tlacidiel moznosti do rozlozenia
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
# pripojenie tlacidiel moznosti do rozlozenia
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

# pripojenie rozlozenia tlacidel moznosti na rozlozenie panelu moznosti
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

# nastavenie rozlozenia panelu moznosti do kontajneru pre skupinu tlacidiel
RadioGroupBox.setLayout(layout_ans1) 

# skupina pre panel odpovede (sivy ramcek)
AnsGroupBox = QGroupBox("Test odpovede")
# menovka pre text ci je vysledok spravny alebo nespravny
lb_Result = QLabel('je tvoja odpoveď správna alebo nesprávna?')
#menovka pre tvoju odpoved co si vybral
lb_Correct = QLabel('tvoja odpoveď bude tu!')

# vertikalne rozlozenie pre panel vysledkom 
layout_res = QVBoxLayout()
# pripojenie menovky pre vysledok na rozlozenie a zarovnanie vlavo a zvrchu
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
# pripojenie menovky pre tvoju odpoved na rozlozenie a zarovnanie na horizontalne na stred, a roztiahnutie
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

# nastavenie rozlozenia panelu odpovede do kontajneru pre skupinu panelu odpovede
AnsGroupBox.setLayout(layout_res)

# rozlozenie pre menovku otazky
layout_line1 = QHBoxLayout()
# rozlozenie pre panely moznosti a odpovede
layout_line2 = QHBoxLayout()
# rozlozenie pre tlacidlo
layout_line3 = QHBoxLayout()

#pridanie menovky otazky do rozlozenia a zarovnanie na stred
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# pridanie kontajnerov panelu moznosti a odpovede do rozlozenia 
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
# skry panel s odpoved
AnsGroupBox.hide() 

# pridat medzeru medzi tlacidlom z lava 
layout_line3.addStretch(1)
# pridat tlacidlo do rozlozenia a roztiahnut ho na dvojnasobok
layout_line3.addWidget(btn_OK, stretch=2)
# pridat medzeru medzi tlacidlom z prava 
layout_line3.addStretch(1)

# hlavne vertikalne rozlozenie
layout_card = QVBoxLayout()

# pripojenie rozlozeni k hlavnemu rozlozeniu 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    ''' zobrazi panel odpovedi '''
    #skryje panel moznosti
    RadioGroupBox.hide()
    #ukaze panel odpovedi
    AnsGroupBox.show()
    #nastavy text na tlacidlo
    btn_OK.setText('Ďalšia otázka')


def show_question():
    ''' zobrazi panel otazky '''
    # ukaze panel moznosti
    RadioGroupBox.show()
    # skryje panel odpovedi
    AnsGroupBox.hide()
    #nastavy text na tlacidlo
    btn_OK.setText('Odpoveď')
    # vypne vlastnost, ze sa da zasktrnut len jedno tlacidlo
    RadioGroup.setExclusive(False) 
    # odsktne vsetky talcidla
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
     # zapne vlastnost, ze sa da zasktrnut len jedno tlacidlo
    RadioGroup.setExclusive(True) 


def show_correct(res):
    ''' ukáže odpoved - vloži a úkaže odpoveď v paneli odpovede'''
    # nastavey text v premenej res do menovky
    lb_Result.setText(res)
    # ukaze vysledok
    show_result()

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(question,right_answer,wrong1,wrong2,wrong3,) :
    '''funkcia vztvoru otazku s odpovedami'''
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer)
    show_question

def check_answer():
  ''' otestuje odpoved'''
  if answers[0].isChecked():
      show_correct("Správne")
  else:
      show_correct("Nesprávne")

#hlavne okno v aplikacii  
window = QWidget()
# nastavenie hlavneho rozlozenia do hlavneho okna aplikacie
window.setLayout(layout_card)
# nastavy nadpis hlavnemu oknu
window.setWindowTitle('Vedomostná karta')

ask("aky je narodni jazyk brazilie", "Portugalcina","brazilcina","slovencina","nigerscina")

# nastavenie udalosti kliknuta na tlacidlo a nastavenie funkcie pre reakciu 
btn_OK.clicked.connect(check_answer) 

# ukaz hlavne okno
window.show()
# spust aplikaciu
app.exec()
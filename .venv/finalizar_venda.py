import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSizePolicy
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

class Color(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("My App")
        self.setGeometry(500,30,648,380)

# usar addWidget em layouts

# a ordem em que você adiciona os layout faz diferença
# Como tem um texto entre dois layout, primeiro precisa adicionar o layout do meio, adicionar o texto e depois o layout de baixo



# usar um setContentsMargins(l,t,r,b) pra dividir os itens. Esse espaçamento é fixo
# e entre itens tem como usar setSpacing(), só não sei se é só para listas
# seria bom usar um maximumSize pra limitar cada layout

# Declarar todos os Layouts em sequência
        titulo = QLabel('Finalizar Venda')
        titulo.setStyleSheet('font-size: 18px')
        main = QVBoxLayout()
        middle = QHBoxLayout()
        middle_left = QVBoxLayout()
        ml1 = QHBoxLayout()
        ml2 = QHBoxLayout()
        ml3 = QHBoxLayout()
        ml4 = QHBoxLayout()
        ml5 = QHBoxLayout()
        ml_v1 = QLineEdit('R$ 100,00')
        ml_v2 = QLineEdit('R$ 0,00')
        ml_v3 = QLineEdit('R$ 0,00')
        ml_v4 = QLineEdit('R$ 100,00')
        ml_v5 = QLineEdit('R$ 0,00')
        middle_right = QVBoxLayout()
        mr1 = QHBoxLayout()
        # mrb1 = 
        mr2 = QHBoxLayout()
        mr3 = QHBoxLayout()
        combo = QComboBox()
        mr3_valor = QLineEdit('R$ 0,00')
        big_input = QLineEdit('1-DINHEIRO         100,00')
        # big_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bottom_text = QLabel('Selecione o Documento para emissão:')
        bottom_text.setAlignment(Qt.AlignCenter)
        bottom = QHBoxLayout()
        bottom_center = QVBoxLayout()
        bottom_right = QVBoxLayout()

# main
        main.addWidget(titulo)
        main.addLayout(middle)
        main.addWidget(bottom_text)
        main.addLayout(bottom)

# middle
        middle.addLayout(middle_left)
        middle.addLayout(middle_right)

# middle_left
        middle_left.addLayout(ml1)
        middle_left.addLayout(ml2)
        middle_left.addLayout(ml3)
        middle_left.addLayout(ml4)
        middle_left.addLayout(ml5)

# Os mls
        ml1.addWidget(QLabel('Total da Venda: '))
        ml1.addWidget(ml_v1)

        ml2.addWidget(QLabel('Desconto: '))
        ml2.addWidget(ml_v2)

        ml3.addWidget(QLabel('Acréscimo: '))
        ml3.addWidget(ml_v3)

        ml4.addWidget(QLabel('Total Líquido: '))
        ml4.addWidget(ml_v4)

        ml5.addWidget(QLabel('Troco: '))
        ml5.addWidget(ml_v5)

#ml_v
        ml_v1.setAlignment(Qt.AlignRight)
        ml_v2.setAlignment(Qt.AlignRight)
        ml_v3.setAlignment(Qt.AlignRight)
        ml_v4.setAlignment(Qt.AlignRight)
        ml_v5.setAlignment(Qt.AlignRight)

# middle_right
        middle_right.addLayout(mr1)
        middle_right.addLayout(mr2)
        middle_right.addLayout(mr3)
        middle_right.addWidget(big_input)


# mrs
        mr1.addWidget(QLabel('Cliente: '))
        mr1.addWidget(QLineEdit('1 - CONSUMIDOR FINAL'))

        mr2.addWidget(QLabel('Vendedor: '))
        mr2.addWidget(QLineEdit('999 - SYNDATA'))

        mr3.addWidget(QLabel('Forma de Pagto: '))
        mr3.addWidget(combo)
        mr3.addWidget(mr3_valor)

# combo
        combo.addItem('1 - DINHEIRO')
        combo.addItem('2 - CARTÃO')
        combo.addItem('3 - PIX')

# mr3_valor
        mr3_valor.setAlignment(Qt.AlignRight)

# big_input
        big_input.setFixedWidth(285)
        big_input.setFixedHeight(100)
        big_input.setAlignment(Qt.AlignTop)

# bottom
        bottom.addWidget(QPushButton('(Esc) Sair'))
        bottom.addLayout(bottom_center)
        bottom.addLayout(bottom_right)

# bottom_center
        bottom_center.addWidget(QPushButton('(F6) Cupom Fiscal'))
        bottom_center.addWidget(QPushButton('(F8) NFC-e Online'))

# bottom_right
        bottom_right.addWidget(QPushButton('(F7) Pedido de Venda'))
        bottom_right.addWidget(QPushButton('(F9) NFC-e Offline'))











        # layout1.setContentsMargins(0,0,0,0)
        # layout1.setSpacing(5)

        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))

        # layout1.addLayout( layout2 )

        # layout1.addWidget(Color('green'))

        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(main)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
from calc import Ui_MainWindow



class Control:
    def __init__(self, window):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        self.ui.pushButton_one.clicked.connect(self.press_button('1'))
        self.ui.pushButton_two.clicked.connect(self.press_button('2'))
        self.ui.pushButton_three.clicked.connect(self.press_button('3'))
        self.ui.pushButton_four.clicked.connect(self.press_button('4'))
        self.ui.pushButton_five.clicked.connect(self.press_button('5'))
        self.ui.pushButton_six.clicked.connect(self.press_button('6'))
        self.ui.pushButton_seven.clicked.connect(self.press_button('7'))
        self.ui.pushButton_eight.clicked.connect(self.press_button('8'))
        self.ui.pushButton_nine.clicked.connect(self.press_button('9'))
        self.ui.pushButton_zero.clicked.connect(self.press_button('0'))
        self.ui.pushButton_point.clicked.connect(self.point)
        self.ui.pushButton_add.clicked.connect(self.press_button('+'))
        self.ui.pushButton_sub.clicked.connect(self.press_button('-'))
        self.ui.pushButton_mul.clicked.connect(self.press_button('*'))
        self.ui.pushButton_div.clicked.connect(self.press_button('/'))
        self.ui.pushButton_plus_minuce.clicked.connect(self.plus_minus)
        self.ui.pushButton_result.clicked.connect(self.equal)
        self.ui.pushButton_percent.clicked.connect(self.percent)
        self.ui.pushButton.clicked.connect(self.press_button('AC'))

        window.show()


    def press_button(self, symbol):
        def click(*args, **kwargs):
            if symbol == 'AC':
                self.ui.output_label.setText('0')
            else:
                if self.ui.output_label.text() == '0':
                    self.ui.output_label.setText(symbol)
                else:
                    txt = self.ui.output_label.text() + symbol
                    self.ui.output_label.setText(txt)
        return click

    def equal(self):
        txt = self.ui.output_label.text()
        try:
            result = str(eval(txt))
        except SyntaxError:
            result = 'ERROR'
        self.ui.output_label.setText(result)

    def plus_minus(self):
        txt = self.ui.output_label.text()
        if '-' in txt:
            self.ui.output_label.setText(txt.replace('-', ''))
        else:
            self.ui.output_label.setText(f'-{txt}')

    def percent(self):
        txt = self.ui.output_label.text()
        if int(txt) >= 10:
            self.ui.output_label.setText(f'0.{txt}')
        else:
            self.ui.output_label.setText(f'0.0{txt}')

    def point(self):
        txt = self.ui.output_label.text()
        if txt[-1] == '.':
            pass
        else:
            self.ui.output_label.setText(f'{txt}.')

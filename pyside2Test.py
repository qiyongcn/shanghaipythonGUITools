import os

envpath = r'D:\Anaconda3\Lib\site-packages\PySide2\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath

from PySide2 import QtXml
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox, QHBoxLayout
from PySide2.QtUiTools import QUiLoader

class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handleCalc)

        self.ui = QUiLoader().load(r'.\ui\first.ui')


        self.button2 = QPushButton('统计2', self.window)

        # 可以隐藏，但还不能动态添加组件
        self.button2.move(380, 180)
        self.button2.setHidden(True)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.button2)



    def handleCalc(self):
        info = self.textEdit.toPlainText()

        self.button2.setHidden(False)

        self.button3 = QPushButton('统计3', self.window)
        self.hbox.addWidget(self.button3)
        # error self.layout1.addItem(self.button3)
        self.button3.move(380, 280)
        self.button3.show()

        # 用text传值过来，if < n 就显示当前的一组text，前名是编号label，中间是行数，后面是文字。

        """
        n = 4;
        self.("button"+n) = QPushButton('统计'+n, self.window)
        self.hbox.addWidget(self.button3)
        # error self.layout1.addItem(self.button3)
        self.button3.move(380, 280)
        self.button3.show()
        """
        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            # 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
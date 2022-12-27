#!/usr/bin/env python3
# coding=utf-8

import math
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Сложные табличные вычисления в Python')

        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.label_img.setPixmap(QPixmap('images/task.png'))
        self.label_img.setScaledContents(True)

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)

    def solve(self):
        class TableWid():
            def __init__(self, array):
                self.array = array
                self.answer = []
                proz = 1
                for index, item in enumerate(self.array):
                    proz *= item
                    first = math.sqrt(math.pow(math.pow(item,2),3) / (proz + 5))
                    second = math.tan(math.pow(math.cos(math.pow(math.cos(item),2)),2))
                    elem = math.pow((first/ second), (1/3))
                    self.answer.append(elem)


        if validation_of_data(self.tableWidget):
            i = 0

            table_value = []
            while i < self.tableWidget.rowCount():
                item = self.tableWidget.item(i, 0).text()
                table_value.append(int(item))
                i += 1
            my_table = TableWid(table_value)
            i = 0
            while i < self.tableWidget.rowCount():
                answer = format(my_table.answer[i],".5f")
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(answer)))
                i += 1

            self.label_error.setText('')
        else:
            self.label_error.setText('Введены некорректные данные!')

    def clear(self):
        self.tableWidget.clearContents()

    def exit(self):
        self.close()

    def fill_random_numbers(self):
        i = 0
        while i < self.tableWidget.rowCount():
            random_num = randint(0, 101)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1


def validation_of_data(table_widget):
    """
    проверяем данные на валидность
    :param table_widget: таблица с числами
    :return: True - данные корректны, False - есть некорректные данные
    """
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False

    return True


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
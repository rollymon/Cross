#!/usr/bin/env python3
# coding=utf-8
import random
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):

        row = 0
        col = 0

        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = random.randrange(-20, 21, 1)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0

        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            self.label_max.setText(
                'Минимум: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + '][' + str(list_information_max_num[2] + 1) + '],\n' +
                'Сумма: ' + str(list_information_max_num[3]))

    def solve(self):
        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
            return
        else:
            self.label_max.setText(
                'Минимум: ' + str(list_information_max_num[0]) + ' [' +
                str(list_information_max_num[1] + 1) + '][' + str(list_information_max_num[2] + 1) + '],\n' +
                'Сумма: ' + str(list_information_max_num[3]))

        min_num = list_information_max_num[0]
        row_min_number = list_information_max_num[1]
        col_min_number = list_information_max_num[2]
        sum1 = list_information_max_num[3]

        if sum1 < min_num:
            self.label_answer.setText(
                'Сумма элементов первой строки (' + str(sum1) + ') не больше минимума (' + str(min_num) + ')\n'
                'Задание не будет выполнено.'
            )
        else:
            self.label_answer.setText(
                'Сумма элементов первой строки (' + str(sum1) + ') больше минимума (' + str(min_num) + ')\n'
            )
            self.tableWidget.setItem(row_min_number, col_min_number, QTableWidgetItem(str(sum1)))

        self.label_error.setText('')


def finder(table_widget):

    row_min_number = 0
    col_min_number = 0
    min_num = int(table_widget.item(row_min_number, col_min_number).text())

    row = 0
    col = 0
    sum1 = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number < min_num:
                    min_num = number
                    row_min_number = row
                    col_min_number = col
                if row == 0:
                    sum1 += number
                col += 1
            row += 1
            col = 0
        return [min_num, row_min_number, col_min_number, sum1]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

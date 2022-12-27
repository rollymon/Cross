#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.label_img.setPixmap(QPixmap('main.png'))
        self.label_img.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)



    # Процедура решения примера
    def solve(self):
        try:
            self.colorLineEdits()
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x >= 5:
                y = 5 * (pow(a, 2) + pow(b, 2)) / (x - 4);
            else:
                y = (6*a*b)-(5*x);
            self.label_answer.setText('Ответ: ' + str(format(y, '.2f')))
            self.label_answer.setStyleSheet("border: 1px solid green;")

        except:
            self.label_answer.setText('Ошибка!')
            self.label_answer.setStyleSheet("border: 1px solid red;")

    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')
        self.label_answer.setStyleSheet("")
        self.lineEdit_a.setStyleSheet("")
        self.lineEdit_b.setStyleSheet("")
        self.lineEdit_x.setStyleSheet("")

    def colorLineEdits(self):
        self.colorChange(self.lineEdit_a)
        self.colorChange(self.lineEdit_b)
        self.colorChange(self.lineEdit_x)

    # Установка окраски рамки у компонента в зависимости от значения в нем
    def colorChange(self, obj):
        try:
            int(obj.text())
            obj.setStyleSheet("border: 1px solid green;")
        except:
            obj.setStyleSheet("border: 1px solid red;")


# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения

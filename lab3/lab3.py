from random import  randint

#pip install numpy
import numpy
#создаю массив с помощью randint
print ("практическая раббота номер 3")
print ("введите число строк: ")
n= int(input())
print ("введите число столбцов: ")
m= int(input())
print ("Введите диапозон чилес массива ")
print ("от")
min_array_value= int(input())
print ("до")
max_array_value= int(input())

array=[[0 for i in range(m)]for j in range(n)]
#задаются значения массива
for i in range(n):
    for j in range(m):
        array[i][j]=randint(min_array_value,max_array_value)
#массив выведен в строку для удобного поиска положения элемента в массиве
for i in range(n):
    for j in range(m):
        print(array[i][j],end=' ')



#используя библиотеку numpy ищу значения минимума и максимума в массиве
min = numpy.min(array)
minind = numpy.argmin(array, axis = None, out = None)
max = numpy.max(array)
maxind = numpy.argmax(array, axis = None, out = None)

#вывод данных для удобной проверки
print('    ')
print("минимальное значение в массиве:" , min)
print("положение в массиве :" , minind)

print('    ')
print("максимальное значение в массиве:" ,max)
print("положение в массиве :" , maxind)

print(array)
#Если максимальный элемент в таблице расположен после минимального, то поменять значения элементов первой и второй строки между собой
for j in range(m):
    if maxind > minind:
        change = array[0][j]
        array[0][j] = array[1][j]
        array[1][j] = change
else:
    print("максимальный элемент рассположен до минимального")
print(array)


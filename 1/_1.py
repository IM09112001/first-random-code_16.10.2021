#Написать функцию, которая заполняет массив случайными числами в диапазоне, указанном пользователем. 
#Функция должна принимать один аргумент - количество чисел, а вернуть должна заполненный список. 
#Для решения этой задачи вам нужно использовать встроенную функцию random. 
#Её нужно сначала импортировать в начале кода перед использованием.

import random
k=int(input("Введите левый диапазон рандома: "))
n=int(input("Введите правый диапазон рандома: "))
def ran(m=n-k): 
    array=[random.randint(k, n) for i in range(m)]
    return array
print(ran())


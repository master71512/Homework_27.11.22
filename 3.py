# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

newList = list(map(float, input('введите числа через пробел: ').split()))
# newList = input('введите числа через пробел: ').split()
subList = []

for i in newList:
    subList.append(i - int(i))
m1 = round(max(subList) - min(subList), 5)   
print(f'произведения пар чисел данного списка равны: {m1}')

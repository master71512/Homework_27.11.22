# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

newList = list(map(int, input('введите числа через пробел: ').split()))
compList = []
for i in range((len(newList)+1)//2):
    compList.append(newList[i]*newList[len(newList)-1 - i])
print(f'произведения пар чисел данного списка равны: {compList}')

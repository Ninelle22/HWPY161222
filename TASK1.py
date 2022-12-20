#1.Пользователь вводит число, 
#нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)

#import math
#print(round(math.pi))

s = int(input('Введите точность: '))
pi = 0
for n in range(s):
	pi += (1 / 16 ** n) * (4 / (8 * n + 1) - 2 / (8 * n + 4) - 1 / (8 * n + 5) - 1 / (8 * n + 6))
print('Число ПИ: ', round(pi, s))


k = 1
x = 0
for k in range(1, 10000):
    x = x + 4 * ((-1)**(k + 1)) / (2 * k - 1)
    print(round(x, int(input("Insert number after , : "))))



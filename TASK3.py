#TASK3
#3. Задайте последовательность чисел. Напишите программу, 
#которая выведет список неповторяющихся элементов исходной последовательности.

import numpy
from random import randint as r
list_input = [r(-10, 30) for i in range(20)] 
res = numpy.array(list_input)
unique_res = numpy.unique(res)
print("Generate array:\n", res)
print()
print("Generate array:\n", unique_res)

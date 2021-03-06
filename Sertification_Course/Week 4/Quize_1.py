# # # -*- coding: utf-8 -*-
# 1.Выберите ваше любимое непрерывное распределение (чем меньше оно будет похоже на нормальное, тем интереснее;
# попробуйте выбрать какое-нибудь распределение из тех, что мы не обсуждали в курсе).
# Сгенерируйте из него выборку объёма 1000, постройте гистограмму выборки и
# нарисуйте поверх неё теоретическую плотность распределения вашей случайной величины.
#
# 2.Для нескольких значений n (например, 5, 10, 50) сгенерируйте 1000 выборок объёма n и
#  постройте гистограммы распределений их выборочных средних. Используя информацию о
# среднем и дисперсии исходного распределения (её можно без труда найти в википедии),
# посчитайте значения параметров нормальных распределений, которыми, согласно
# центральной предельной теореме, приближается распределение выборочных средних.
# Обратите внимание: для подсчёта значений этих параметров нужно
# использовать именно теоретические среднее и дисперсию вашей случайной величины, а не их выборочные оценки.
# Поверх каждой гистограммы нарисуйте плотность соответствующего нормального распределения.
#
# Опишите разницу между полученными распределениями при различных значениях n.
# Как меняется точность аппроксимации распределения выборочных средних нормальным с ростом n?
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto
import scipy.stats as sts


# Выбор параметров для распределения
k = 10


# #Сгенерируйте из него выборку объёма 1000
# sampleRange = pareto.rvs(k, size=1000)
# #Постройте гистограмму выборки и нарисуйте поверх неё теоретическую плотность распределения вашей случайной величины.
# plt.hist(sampleRange, normed=True, bins=20, alpha=0.5, label='hist samples')
# plt.ylabel('number of samples')
# plt.xlabel('$x$')
#
# #теоретическая плотность распределения случайной величины
# left = pareto.ppf(0.01, k)
# right =  pareto.ppf(0.99, k)
# x = np.linspace(left,  right, 100)
# plt.plot(x, pareto.pdf(x, k), 'r-', lw=5, alpha=0.7, label='pareto pdf')
# plt.legend(loc='best')

# plt.show()



# m = []
# for _ in xrange(20):
#     m.append(np.mean(pareto.rvs(k, size=1000)))
# # plt.hist(m, normed=True, alpha=0.5, label='hist samples')

EX = pareto.mean(k)
print EX
std = pareto.std(k)
print std
DX = std**2
print DX
print
# Для нескольких значений n (например, 5, 10, 50) сгенерируйте 1000 выборок объёма n и
# постройте гистограммы распределений их выборочных средних.
n = 100
values = np.array([ pareto.rvs(k, size=n) for x in range(1000)])
meanVal = values.mean(axis = 1)
plt.hist(meanVal, normed=True, alpha=0.5, label='hist mean n ' + str(n))

mu = EX
sigma = math.sqrt(DX/n)

# зададим нормально распределенную случайную величину
norm_rv = sts.norm(loc=mu, scale=sigma)
x = np.linspace(0.5,2,100)
# print x
pdf = norm_rv.pdf(x)
plt.plot(x, pdf, 'r-', lw=3, alpha=0.7, label='pareto pdf')


plt.show()


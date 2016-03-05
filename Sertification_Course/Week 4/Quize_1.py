# # -*- coding: utf-8 -*-

# Распределе́ние Паре́то в теории вероятностей — двухпараметрическое семейство абсолютно непрерывных распределений
# , являющихся степенными. Называется по имени Вилфредо Парето.
# Встречается при исследовании различных явлений, в частности, социальных,
# экономических, физических и других.
# Вилфредо Парето изначально использовал это распределение для описания распределения благосостояния,
# а также распределения дохода. Его правило 20 к 80 (которое гласит: 20 %
# популяции владеет 80 % богатства) однако зависит от конкретной величины k, и утверждается,
# что фактически встречаются существенные количественные отклонения, например, данные
# самого Парето по Британии в Cours d'économie politique говорят, что там примерно 30 % населения
# владеет 70 % общего дохода.
# https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%9F%D0%B0%D1%80%D0%B5%D1%82%D0%BE
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html#scipy.stats.pareto



# b = 1
#
# # pareto_rv = pareto.stats(b, moments='mvsk')
# # print type(pareto_rv)
#
# ax = plt.subplots(1, 1)
#
# sample = pareto.rvs(b, size=1000)
#
# plt.hist(sample, normed=True, bins=40, alpha=0.8)
# plt.ylabel('F(X)')
# plt.xlabel('$x$')
#
# print type(sample)
# print sample
#
# x = np.linspace(pareto.ppf(0.01, b),  pareto.ppf(0.99, b), 100)
#
# plt.plot(x, pareto.pdf(x, b), 'r-', lw=5, alpha=0.7, label='pareto pdf')
#
# mean, var, skew, kurt = pareto.stats(b, moments='mvsk')
# print pareto.std(b)
# print mean, var, skew, kurt
#
# # для построения ECDF используем библиотеку statsmodels
# # from statsmodels.distributions.empirical_distribution import ECDF
# # ecdf = ECDF(sample)
# # print ecdf.x
# # plt.step(ecdf.x, ecdf.y, label='ECDF')
#
#
# sample = pareto.rvs(b, size=1000)
#
# plt.hist(sample, normed=True, bins=10, alpha=0.8)
# plt.ylabel('F(X)')
# plt.xlabel('$x$')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

# Выбор параметров для распределения
k = 10
x_m = 1

#Сгенерируйте из него выборку объёма 1000
sampleRange = pareto.rvs(k, size=1000)
#Постройте гистограмму выборки и нарисуйте поверх неё теоретическую плотность распределения вашей случайной величины.
plt.hist(sampleRange, normed=True, bins=100, alpha=0.5)
print type(sampleRange)
print sampleRange
plt.ylabel('number of samples')
plt.xlabel('$x$')

# b = 10
# r = pareto.rvs(b, size=1000)
# fig, ax = plt.subplots(1, 1)
# ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
plt.show()




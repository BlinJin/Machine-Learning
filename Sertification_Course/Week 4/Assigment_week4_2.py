# # -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2


df = 5
rv = chi2(df)


#Сгенерируйте из него выборку объёма 1000
sampleRange = chi2.rvs(df, size=1000)
#Постройте гистограмму выборки и нарисуйте поверх неё теоретическую плотность распределения вашей случайной величины.
# plt.hist(sampleRange, normed=True, bins=20, alpha=0.5, label='hist samples')
# plt.ylabel('number of samples')
# plt.xlabel('$x$')
#теоретическая плотность распределения случайной величины
left = chi2.ppf(0.01, df)
right =  chi2.ppf(0.99, df)
x = np.linspace(left,  20, 100)
# plt.plot(x, rv.pdf(x), 'r-', lw=5, alpha=0.7, label='chi2 pdf')
plt.legend(loc='best')

# plt.show()


# values = np.array([pareto.rvs(k, size=10) for x in range(10)])
# print values
# plt.hist(values.mean(axis=1), normed=True)

m = []
# for _ in xrange(20):
#     m.append(np.mean(chi2.rvs(df, size=1000)))
# plt.hist(m, normed=True, alpha=0.5, label='hist samples')

mean = chi2.mean(df)
print mean

EX = mean
print 'EX ', mean
std = chi2.std(df)
print 'Standard deviation of the distribution. ', std
DX = std**2
print 'DX - ', DX
#
n = 50
values = np.array([ chi2.rvs(df, size=n) for x in range(10000)])
# print 'values ', values
# print 'mean ', values.mean(axis = 1)
meanAr = values.mean(axis = 1)
plt.hist(meanAr, normed=True, alpha=0.5, bins=100)
#
import scipy.stats as sts
#
mu = EX
sigma = DX/n
#
# # зададим нормально распределенную случайную величину
norm_rv = sts.norm(loc=mu, scale=std)
x = np.linspace(3,7,100)
print x
pdf = norm_rv.pdf(x)
plt.plot(x, pdf)

# # для построения используем библиотеку Pandas:
import pandas as pd
df = pd.DataFrame(meanAr)
# # print df
norm_rv = sts.norm(loc=mu, scale=std/n)
x = np.linspace(0,2,100)
# # print x
pdf = norm_rv.pdf(x)
plt.plot(x, pdf, 'r-',)

plt.show()

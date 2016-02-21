# -*- coding: utf-8 -*-
# 1.Сформируйте систему линейных уравнений (то есть задайте матрицу коэффициентов A и свободный вектор b)
# для многочлена первой степени, который должен совпадать с функцией f в точках 1 и 15.
# Решите данную систему с помощью функции scipy.linalg.solve. Нарисуйте функцию f и полученный многочлен.
# Хорошо ли он приближает исходную функцию?

# Повторите те же шаги для многочлена второй степени, который совпадает с функцией f в точках 1, 8 и 15. Улучшилось ли качество аппроксимации?
# Повторите те же шаги для многочлена третьей степени, который совпадает с функцией f в точках 1, 4, 10 и 15. Хорошо ли он аппроксимирует функцию? Коэффициенты данного многочлена (четыре числа в следующем порядке: w_0, w_1, w_2, w_3) являются ответом на задачу. Округлять коэффициенты не обязательно, но при желании можете произвести округление до второго знака (т.е. до числа вида 0.42)
# Запишите полученные числа в файл, разделив пробелами.
# Обратите внимание, что файл должен состоять из одной строки, в конце
# которой не должно быть переноса. Пример файла с решением вы можете найти в конце задания (submission-2.txt).




import numpy as np
import matplotlib.pylab as plt
import scipy.linalg as lilg
import random as rnd
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
def functQuiz(x):
    f = np.sin(x / 5.) * np.exp(x /10.) + 5 * np.exp(-x /2.)
    return f

def polinom(degree, arrayCoef, x):
    result = 0.0
    degree += 1
    for iter in range(degree):
        if (iter == 0):
            result += arrayCoef[iter]
        else:
            result += arrayCoef[iter] * (x ** iter)
    return result

def approximationPolinomVector(aPointsX, functionInit):
    aPointsY =[]
    for xP in aPointsX:
        aPointsY.append(round(functionInit(xP),2))
    return aPointsY

def approximationPolinomMatrix(degree, aPointsX, functionInit):
    polinomMatrix = []
    for d in range(len(aPointsX)):
        rowVector = []
        for w in range(degree + 1):
            if (w == 0):
                rowVector.append(1)
            else:
                rowVector.append(aPointsX[d] ** w)
        polinomMatrix.append(rowVector)
    return polinomMatrix


def runPolinom1():
    xPoints = np.arange(1, 15, 0.1)
    print type(xPoints), xPoints
    yPoints = []
    for x in xPoints:
        yPoints.append(functQuiz(x));
    plt.plot(xPoints, yPoints)

    # Аппроксимация функции многочленом 1 степени
    approximationMatrix = approximationPolinomMatrix(1, [1,15], functQuiz)
    approximationVector = approximationPolinomVector([1,15], functQuiz)
    a = np.array(approximationMatrix)
    b = np.array(approximationVector)
    xW = np.linalg.solve(a, b)
    xW2 = lilg.solve(a, b)
    print "--------Аппроксимация функции многочленом 1 степени--------------------"
    print "Матрица A:\n", a
    print "Вектор b:\n", b
    print "Решение системы:\n", xW
    print "Решение системы:\n", xW2
    print "Проверка:\n"
    print "Аппроксимирующий полином 1 степени ", polinom(degree=1, arrayCoef=xW, x=1), " - ", functQuiz(1)
    print "Аппроксимирующий полином 1 степени ", polinom(degree=1, arrayCoef=xW, x=15), " - ", functQuiz(15)
    yAPoints = []
    for xPoint in xPoints:
        yAPoints.append(polinom(degree=1, arrayCoef=xW, x=xPoint));
    plt.plot(xPoints, yAPoints)
    plt.show()

def runPolinom2():
    xPoints = np.arange(1, 15, 0.1)
    print type(xPoints), xPoints
    yPoints = []
    for x in xPoints:
        yPoints.append(functQuiz(x));
    plt.plot(xPoints, yPoints)
        # Аппроксимация функции многочленом 2 степени
    approximationMatrix = approximationPolinomMatrix(2, [1,8,15], functQuiz)
    approximationVector = approximationPolinomVector([1,8,15], functQuiz)
    a = np.array(approximationMatrix)
    b = np.array(approximationVector)
    xW = np.linalg.solve(a, b)
    xW2 = lilg.solve(a, b)
    print "--------Аппроксимация функции многочленом 2 степени--------------------"
    print "Матрица A:\n", a
    print "Вектор b:\n", b
    print "Решение системы:\n", xW
    print "Решение системы:\n", xW2
    print "Проверка:\n"
    print "Аппроксимирующий полином 2 степени ", polinom(degree=2, arrayCoef=xW, x=1), " - ", functQuiz(1)
    print "Аппроксимирующий полином 2 степени ", polinom(degree=2, arrayCoef=xW, x=8), " - ", functQuiz(8)
    print "Аппроксимирующий полином 2 степени ", polinom(degree=2, arrayCoef=xW, x=15), " - ", functQuiz(15)
    yAPoints = []
    for xPoint in xPoints:
        yAPoints.append(polinom(degree=2, arrayCoef=xW, x=xPoint));
    plt.plot(xPoints, yAPoints)
    plt.show()


def runPolinom3():
    xPoints = np.arange(1, 15, 0.1)
    print type(xPoints), xPoints
    yPoints = []
    for x in xPoints:
        yPoints.append(functQuiz(x));
    plt.plot(xPoints, yPoints)
        # Аппроксимация функции многочленом 2 степени
    approximationMatrix = approximationPolinomMatrix(3, [1,4,10,15], functQuiz)
    approximationVector = approximationPolinomVector([1,4,10,15], functQuiz)
    a = np.array(approximationMatrix)
    b = np.array(approximationVector)
    xW = np.linalg.solve(a, b)
    xW2 = lilg.solve(a, b)
    print "--------Аппроксимация функции многочленом 3 степени--------------------"
    print "Матрица A:\n", a
    print "Вектор b:\n", b
    print "Решение системы:\n", xW
    print "Решение системы:\n", xW2
    print "Проверка:\n"
    print "Аппроксимирующий полином 3 степени ", polinom(degree=3, arrayCoef=xW, x=1), " - ", functQuiz(1)
    print "Аппроксимирующий полином 3 степени ", polinom(degree=3, arrayCoef=xW, x=4), " - ", functQuiz(4)
    print "Аппроксимирующий полином 3 степени ", polinom(degree=3, arrayCoef=xW, x=10), " - ", functQuiz(10)
    print "Аппроксимирующий полином 3 степени ", polinom(degree=3, arrayCoef=xW, x=15), " - ", functQuiz(15)
    yAPoints = []
    for xPoint in xPoints:
        yAPoints.append(polinom(degree=3, arrayCoef=xW, x=xPoint));
    plt.plot(xPoints, yAPoints)
    plt.show()




def runPolinomN(degPolinom, funInit, poinx1, pointxn):
    xPoints = np.arange(poinx1, pointxn, 0.1)
    print type(xPoints), xPoints
    yPoints = []
    for x in xPoints:
        yPoints.append(funInit(x));
    plt.plot(xPoints, yPoints)
        # Аппроксимация функции многочленом 2 степени
    # pointXToApporximate = [1,4,10,15]
    pointXToApporximate=[]
    pointXToApporximate.append(poinx1)
    for rNumb in range(degPolinom-1):
         pointXToApporximate.append(rnd.randint(poinx1 + 1, pointxn - 1))
    pointXToApporximate.append(pointxn)
    # pointXToApporximate = np.arange(1, 15, 15/degPolinom)

    approximationMatrix = approximationPolinomMatrix(degPolinom, pointXToApporximate, funInit)
    approximationVector = approximationPolinomVector(pointXToApporximate, funInit)
    a = np.array(approximationMatrix)
    b = np.array(approximationVector)
    xW = np.linalg.solve(a, b)
    xW2 = lilg.solve(a, b)
    print "--------Аппроксимация функции многочленом 3 степени--------------------"
    print "Матрица A:\n", a
    print "Вектор b:\n", b
    print "Решение системы:\n", xW
    print "Решение системы:\n", xW2
    print "Проверка:\n"
    for pl in range(degPolinom + 1):
        print "Аппроксимирующий полином", degPolinom,  " степени ", polinom(degree=degPolinom, arrayCoef=xW, x=pointXToApporximate[pl]), " - ", funInit(pointXToApporximate[pl])
    yAPoints = []
    for xPoint in xPoints:
        yAPoints.append(polinom(degree=degPolinom, arrayCoef=xW, x=xPoint));
    plt.plot(xPoints, yAPoints)
    plt.show()


# Запуск
# runPolinomN(3,functQuiz, 1,15)
runPolinom3()
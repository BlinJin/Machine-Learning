import pandas
import numpy as np

def main():
    data = readCSV('titanic.csv', indexColumn = 'PassengerId')
    # print (data.head())
    quize1(data)
    quize2(data)
    quize3(data)
    quize4(data)
    quize5(data)
    quize6(data)


def readCSV(name, indexColumn):
    data = pandas.read_csv(name, index_col=indexColumn)
    return data

def quize1(data):
# Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
    print ('--------------------------------------')
    print ('1.Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.')
    print (data['Sex'].value_counts())
    print (data['Sex'].value_counts().get_value(label='male'))
    print (data['Sex'].value_counts().get_value(label='female'))

def quize2(data):
# Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
    print ('--------------------------------------')
    print ('2.Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров. '
           'Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).')
    print (data['Survived'].value_counts())
    print (data['Survived'].value_counts().get_value(label=1)/data['Survived'].count())


def quize3(data):
# Какую долю пассажиры первого класса составляли среди всех пассажиров? Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
    print ('--------------------------------------')
    print ('3.Какую долю пассажиры первого класса составляли среди всех пассажиров? '
           'Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен)')
    print (data['Pclass'].value_counts().get_value(label=1)/data['Pclass'].count())

def quize4(data):
# Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.
    print ('--------------------------------------')
    print ('4.Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров. В качестве ответа приведите два числа через пробел.')
    print (data['Age'].mean())
    print (data['Age'].median())


def quize5(data):
# Коррелируют ли число братьев/сестер с числом родителей/детей? Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
    print ('--------------------------------------')
    print ('5.Коррелируют ли число братьев/сестер с числом родителей/детей? Посчитайте корреляцию Пирсона между признаками SibSp и Parch.')
    print (data['SibSp'].corr(data['Parch'], 'pearson'))


def quize6(data):
# Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).
# Это задание — типичный пример того, с чем сталкивается специалист по анализу данных. Данные очень разнородные и шумные,
# но из них требуется извлечь необходимую информацию. Попробуйте вручную разобрать несколько значений столбца
# Name и выработать правило для извлечения имен, а также разделения их на женские и мужские.
    print ('--------------------------------------')
    print ('6.Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name) его личное имя (First Name).')
    X = data.loc[data['Sex'] == 'female']
    X1 = X['Name']
    X2 = X1.apply(parse)
    # print(X2)
    X3 = X2.groupby(X2).count()
    print(X3)


def parse(name):
    parsedName = name.split(".")[1].strip()
    if parsedName.find("(") >= 0 and parsedName.find(")") >= 0:  # .replace("(", "").replace(")", "").split(" ")[0]
        parsedName = parsedName.split("(")[1].split(")")[0].split(" ")[0].strip()
        print(parsedName)
    else :
        parsedName = parsedName.split(" ")[0]
        print(parsedName)
    return parsedName


main()

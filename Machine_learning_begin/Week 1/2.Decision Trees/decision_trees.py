import pandas
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def main():
    data = readCSV('titanic.csv', indexColumn = 'PassengerId')
    quize1(data)


def readCSV(name, indexColumn):
    data = pandas.read_csv(name, index_col=indexColumn)
    return data

def quize1(data):
# 1. Select count of neighbors.Загрузите выборку из файла titanic.csv с помощью пакета Pandas.
# 2.Оставьте в выборке четыре признака: класс пассажира (Pclass), цену билета (Fare), возраст пассажира (Age) и его пол (Sex).
# 3.Обратите внимание, что признак Sex имеет строковые значения.
# 4.Выделите целевую переменную — она записана в столбце Survived.
# 5.В данных есть пропущенные значения — например, для некоторых пассажиров неизвестен их возраст.
# 6.Такие записи при чтении их в pandas принимают значение nan.
# Найдите все объекты, у которых есть пропущенные признаки, и удалите их из выборки.
# Обучите решающее дерево с параметром random_state=241 и остальными параметрами по умолчанию.
# Вычислите важности признаков и найдите два признака с
# наибольшей важностью. Их названия будут ответами для данной задачи
# (в качестве ответа укажите названия признаков через запятую или пробел, порядок не важен).
    dataF = data[['Pclass', 'Fare', 'Age', 'Sex','Survived']]
    dataF = dataF.dropna()
    Y = dataF['Survived']
    dataF = dataF[['Pclass', 'Fare', 'Age', 'Sex']]
    clf = DecisionTreeClassifier(random_state=241)
    dataF.loc[dataF['Sex'] != 'male', 'Sex'] = 0
    dataF.loc[dataF['Sex'] == 'male', 'Sex'] = 1
    print (dataF)
    clf.fit(dataF, Y)
    importances = clf.feature_importances_
    print(importances)
    # d = zip(dataF.columns, clf.feature_importanc_)
    # print(d)
    return

main()
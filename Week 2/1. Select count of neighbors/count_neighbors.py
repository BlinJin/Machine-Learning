import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn import cross_validation
# 1.Загрузите выборку Wine по адресу https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
# 2.Извлеките из данных признаки и классы. Класс записан в первом столбце (три варианта), признаки — в столбцах со второго по последний.
# Более подробно о сути признаков можно прочитать по адресу https://archive.ics.uci.edu/ml/datasets/Wine
# 3.Оценку качества необходимо провести методом кросс-валидации по 5 блокам (5-fold). Создайте генератор разбиений, который перемешивает выборку перед формированием блоков (shuffle=True).
# Для воспроизводимости результата, создавайте генератор KFold с
# фиксированным параметром random_state=42. В качестве меры качества используйте долю верных ответов (accuracy).


def main():
    data = readCSV('wine.data.txt')
    print (data)
    a = data[data[0] == 1]
    print (a[0].count())
    countElements = a[0].count()
    kf = KFold(n=countElements, n_folds=5, shuffle=True, random_state=42)
    print(len(kf))
    for train_index, test_index in kf:
        print("TRAIN:", train_index, "\nTEST:", test_index, "\n")
    # neigh = KNeighborsClassifier(n_neighbors=3)
        scores = cross_validation.cross_val_score(estimator=kf, X=test_index, scoring=None)
        print(scores)


def readCSV(name):
    data = pandas.read_csv(name, index_col=False, header=None)
    return data

main()
import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn import cross_validation
from sklearn import preprocessing
import numpy as np
# 1.Загрузите выборку Wine по адресу https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
# 2.Извлеките из данных признаки и классы. Класс записан в первом столбце (три варианта), признаки — в столбцах со второго по последний.
# Более подробно о сути признаков можно прочитать по адресу https://archive.ics.uci.edu/ml/datasets/Wine
# 3.Оценку качества необходимо провести методом кросс-валидации по 5 блокам (5-fold). Создайте генератор разбиений, который перемешивает выборку перед формированием блоков (shuffle=True).
# Для воспроизводимости результата, создавайте генератор KFold с
# фиксированным параметром random_state=42. В качестве меры качества используйте долю верных ответов (accuracy).

# 1.import pandas
#
# import numpy as np
#
# dat = np.array(pandas.read_csv(’train.csv’, header = None))
#
# X_train = dat[:,1:]
#
# y_train = dat[:,0]

# 2.X = df.iloc[:,1:]
#
# y = df.iloc[:,0]

# 3.
# X_np = df.iloc[:,1:].values
#
# y = df.iloc[:,0].values

def main():
    data = readCSV('wine.data.txt')
    # print (data)
    a = data[data[0] == 1]
    # print (data[0].count())
    countElements = data[0].count()
    kf = KFold(n=countElements, n_folds=5, shuffle=True, random_state=42)
    # neigh = KNeighborsClassifier(n_neighbors=3)
    # print(len(kf))
    # for train_index, test_index in kf:
    #     print("TRAIN:", train_index, "\nTEST:", test_index, "\n")
    dataX = data[[1,2,3,4,5,6,7,8,9,10,11,12,13]]
    dataY = data[0]
    maxResult = 0
    maxIndex = 0
    for i in range(1,51):
        clf = KNeighborsClassifier(n_neighbors=i)
        scores = cross_validation.cross_val_score(clf, dataX, dataY, cv=kf)
        mean = np.mean(scores)
        if (mean > maxResult):
            maxResult = mean
            maxIndex = i
    print(maxIndex," ", maxResult)

    X_scaled = preprocessing.scale(dataX)
    # Y_scaled = preprocessing.scale(dataY)
    print (X_scaled)
    for i in range(1,51):
        clf = KNeighborsClassifier(n_neighbors=i)
        scores = cross_validation.cross_val_score(clf, X_scaled, dataY, cv=kf)
        mean = np.mean(scores)
        if (mean > maxResult):
            maxResult = mean
            maxIndex = i
        print (i," ", mean)
    print(maxIndex," ", maxResult)


def readCSV(name):
    data = pandas.read_csv(name, index_col=False, header=None)
    return data

main()
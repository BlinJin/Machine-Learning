import pandas
import numpy as np
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
data.head()
print (data.head())
sort = data.sort_values(['Sex'], ascending=False)
sort.head(1)
print (data['Sex'].value_counts())
print (data['Survived'].value_counts())
print (data['Survived'].value_counts()[1]/data['Survived'].count())

X = np.random.normal(loc=1, scale=10, size=(1000, 50))
# print (X)

print (data['Pclass'].value_counts()[1]/data['Pclass'].count())
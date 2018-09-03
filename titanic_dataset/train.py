import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

import pickle

params = {
    'axes.labelsize': "large",
    'xtick.labelsize': 'x-large',
    'legend.fontsize': 20,
    'figure.dpi': 150,
    'figure.figsize': [25, 7]
}
plt.rcParams.update(params)
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score

lr = LogisticRegression()

data = pd.read_csv("train.csv")

"""
#Exploring the Data

data['Died'] = 1 - data['Survived']
data.groupby('Sex').agg('sum')[['Survived', 'Died']].plot(kind='bar', figsize=(25, 7),
                                                          stacked=True, color=['g', 'r']);

figure = plt.figure(figsize=(25, 7))
plt.hist([data[data['Survived'] == 1]['Fare'], data[data['Survived'] == 0]['Fare']],
         stacked=True, color = ['g','r'],
         bins = 100, label = ['Survived','Dead'])

#When binned, find percentage survived vs dead
#Use an ROC graph

plt.xlabel('Fare')
plt.ylabel('Number of passengers')
plt.legend();
plt.show()
print(data.describe())
"""
#Convert male/female to binary representation where male is 1
Sex1 = []
num = 0
for gen in data['Sex']:
    if gen == 'male':
        Sex1.append(1)
    else:
        Sex1.append(0)
    num += 1

#convert Embarked to int
embarked1 = []
embarked2 = []
embarked3 = []

num = 0
for place in data['Embarked']:
    if place == 'S':
        embarked1.append(1)
        embarked2.append(0)
        embarked3.append(0)
    elif place == 'C':
        embarked1.append(0)
        embarked2.append(1)
        embarked3.append(0)

    elif place == 'Q':
        embarked1.append(0)
        embarked2.append(0)
        embarked3.append(1)
    else:
        embarked1.append(0)
        embarked2.append(0)
        embarked3.append(0)
    num += 1

dataFeatures = data[[ 'Pclass', 'SibSp', 'Parch', 'Fare']]
#dataFeatures['Age'] = dataFeatures['Age'].fillna(30)
#print(dataFeatures.shape)
dataFeatures.insert(loc=0, column = 'Sex', value = Sex1)
#dataFeatures.insert(loc=0, column = 'Embarked', value = embarked1)
"""
dataFeatures.insert(loc=0, column = 'Embarked C', value = embarked2)
dataFeatures.insert(loc=0, column = 'Embarked S', value = embarked1)
dataFeatures.insert(loc=0, column = 'Embarked Q', value = embarked3)
"""

#print(dataFeatures.shape)
"""
#Making use of the Name column
title = []
Nme = []
words = []
for str in data['Name']:
    Nme = re.split('[.,]',str)
    words.append(Nme[1])

data['Titles'] = words
title_dict = dict(zip(data['Titles'].unique(), list(range(0,17))))

titles = []
for val in data['Titles']:
    a = title_dict[val]
    titles.append(a)
dataFeatures['Titles'] = titles
"""
print(dataFeatures.columns)
yvalues = data['Survived']

X_train, X_test, Y_train, Y_test = train_test_split(
    dataFeatures, yvalues, test_size = 0.2, random_state = 10)

lr.fit(X_train, Y_train)


#pred_train = lr.predict(X_train)
pred_test = lr.predict(X_test)

scores = cross_val_score(lr, dataFeatures, yvalues, cv = 15)
scores.sort()
accuracy = scores.mean()

print(f"The test score with logistic regression is {accuracy} %")

filename = 'model.sav'
pickle.dump(lr, open(filename, 'wb'))

"""
#  Using a decision tree
tr = tree.DecisionTreeClassifier()
tr.fit(X_train, Y_train)
pred_tree_test = tr.predict(X_test)

scores_tree = cross_val_score(tr, dataFeatures, yvalues, cv = 3)
scores_tree.sort()
accuracy_tree = scores_tree.means()

print(f"The test score with decision tree is {accuracy_tree} %")
"""
"""
Submission Stuff

testData = pd.read_csv("test.csv")

#Convert male/female to binary representation where male is 1
Sex2 = []
num = 0
for gen in testData['Sex']:
    if gen == 'male':
        Sex2.append(1)
    else:
        Sex2.append(0)
    num += 1

#Need to do this for embarked
embarked2 = []
num = 0
for place in testData['Embarked']:
    if place == 'S':
        embarked2.append(10)
    elif place == 'C':
        embarked2.append(0)
    else:
        embarked2.append(-10)
    num += 1
dataSubmission = testData[[ 'Pclass', 'SibSp', 'Parch', 'Fare']]
dataSubmission.insert(loc=0, column = 'Sex', value = Sex2)
dataSubmission.insert(loc=0, column = 'Embarked', value = embarked2)
dataSubmission.at[152, 'Fare'] = 0

matrixSubmission = testData[['PassengerId']]
pred_submission = lr.predict(dataSubmission)
matrixSubmission.insert(loc=1, column = 'Survived', value = pred_submission)
matrixSubmission.to_csv('titanicSubmit.csv',index = False)
"""

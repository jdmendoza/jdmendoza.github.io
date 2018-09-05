import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/Users/jdmendoza/.kaggle/datasets/mlg-ulb/creditcardfraud/creditcard.csv",header = 0)
#print(data.shape)
#print(data.head(10))
#data['normAmount'] = StandardScaler().fit_transform(data['Amount'].reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)

frauds = data[data['Class'] == 1]
not_frauds = data[data['Class'] == 0].sample(frauds.shape[0]*2)

event = round(frauds.shape[0]*100/(frauds.shape[0]+not_frauds.shape[0]),1)
print("The test set event occurence is:", event, "%")

#Shuffle the rows
data_eq = pd.concat([frauds, not_frauds]).reset_index(drop=True)
#print(data_eq[0:10])
#print([data_eq[500:510]])
data_eq = data_eq.sample(frac=1).reset_index(drop=True)
print("After sample", data_eq.shape)
target = data_eq['Class']
#print(data_eq)

data_eq = data_eq.drop(['Class'],axis=1)

model = LogisticRegression(C = 0.6, penalty='l2')

X_train, X_test, Y_train, Y_test = train_test_split(
    data_eq, target, test_size = 0.3, random_state = 0)

model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

#In order of importance recall > precision > tnr
tn, fp, fn, tp = confusion_matrix(Y_test, Y_pred).ravel()
recall = tp/(tp + fn)
precision = tp/(tp + fp)
print("Small -> recall:", round(recall,4), "precision: ", round(precision,4))

full_target = data['Class']
full_data = data.drop('Class', axis=1)

Y_full_pred = model.predict(full_data)

tn_full, fp_full, fn_full, tp_full = confusion_matrix(full_target, Y_full_pred).ravel()
recall_full = tp_full/(tp_full + fn_full)
precision_full = tp_full/(tp_full + fp_full)
print("All  -> recall: ", round(recall_full,4), "precision: ", round(precision_full,4))
#Add further optimization: dimension reduction, optimize C, average recall and such

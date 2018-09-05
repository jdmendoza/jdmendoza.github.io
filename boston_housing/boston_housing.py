from sklearn.datasets import load_boston
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", color_codes=True)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

dataset = load_boston()
boston = pd.DataFrame(dataset.data, columns=dataset.feature_names)
target = pd.DataFrame(dataset.target, columns={"Target"})

lr = LinearRegression(normalize=True)

X_train, X_test, Y_train, Y_test = train_test_split(
    boston, target, test_size = 0.2)

model = lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)
mse = mean_squared_error(Y_test, Y_predict)

print("Mean Squared Error is: ",mse)

plt.scatter(Y_test, Y_predict)
plt.show()

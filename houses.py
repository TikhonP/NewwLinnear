from sklearn.datasets import load_boston

boston_dataset = load_boston()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(boston_dataset.data, boston_dataset.target, random_state=1)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

def pred (X):
    y = lin_model.predict(X)
    return y[0]

import numpy as np

def getXandPredict (CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
    X = np.array([CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT])
    X = X.reshape(1, -1)
    return pred(X)

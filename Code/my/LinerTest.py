import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data_age_salary.csv')
X = dataset.iloc[:,:1].values
print(X)
Y = dataset.iloc[:,1].values
print(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=1/4, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train,Y_train)

Y_predict = regressor.predict(X_test)

plt.scatter(X_test, Y_test, color="red")
plt.plot(X_test, Y_predict, color="blue")

plt.scatter(X_train, Y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")

plt.title('Linear Regression')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.show()
# Importing the libraries
import pandas as pd
import numpy as np

# Importing the dataset
dataset = pd.read_csv('../datasets/50_Startups.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : ,  4 ].values

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[: , 3] = labelencoder.fit_transform(X[ : , 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()
print("onehot:")
print(X[:10])

# Avoiding Dummy Variable Trap
X = X[: , 1:]
print("Avoiding Dummy Variable Trap")
print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# regression evaluation
from sklearn.metrics import r2_score
print("y_pred")
print(y_pred)
print("Y_test")
print(Y_test)
print(r2_score(Y_test, y_pred))     # 越接近1，模型越好

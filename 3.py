import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

print("Enter no of data points:")
n = int(input())

x = []
y = []

for i in range(n):
    a1 = float(input("enter x value: "))
    b1 = float(input("enter y value: "))
    x.append(a1)
    y.append(b1)

df = pd.DataFrame({
    "x": x,
    "y": y
})

print(df)

plt.scatter(df["x"], df["y"])
plt.show()

X = df["x"].values
Y = np.log(df["y"].values)

a00 = np.sum(X**2)
a01 = np.sum(X)
a10 = np.sum(X)
a11 = n

b0 = np.sum(X * Y)
b1 = np.sum(Y)

coef_matrix = np.array([
    [a00, a01],
    [a10, a11]
])

const_matrix = np.array([b0, b1])

result = np.dot(np.linalg.inv(coef_matrix), const_matrix)

b = result[0]
a = np.exp(result[1])

print("a =", a)
print("b =", b)

y_pred = a * np.exp(b * df["x"])

plt.scatter(df["x"], df["y"], label="Data")
plt.plot(df["x"], y_pred, label="Exponential Fit")
plt.legend()
plt.show()

mse = mean_squared_error(df["y"], y_pred)
r2 = r2_score(df["y"], y_pred)

print("MSE =", mse)
print("R2 =", r2)

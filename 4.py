import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))
degree = int(input("Enter the degree of polynomial regression: "))

x = []
y = []

for i in range(n):
    xi = float(input(f"Enter x[{i+1}]: "))
    yi = float(input(f"Enter y[{i+1}]: "))
    x.append(xi)
    y.append(yi)

x = np.array(x, dtype=float)
y = np.array(y, dtype=float)

df = pd.DataFrame({"x": x, "y": y})
print(df)


X = np.column_stack([x**j for j in range(degree + 1)])

XT = X.T
XTX = XT @ X
XTy = XT @ y.reshape(-1, 1)
coefficients = np.linalg.inv(XTX) @ XTy

print("\nCoefficients:")
for i, c in enumerate(coefficients.flatten()):
    print(f"a{i} = {c}")

y_pred = (X @ coefficients).flatten()

sort_idx = np.argsort(x)
x_sorted = x[sort_idx]
y_pred_sorted = y_pred[sort_idx]

plt.scatter(x, y, color="red", label="Data points")
plt.plot(x_sorted, y_pred_sorted, color="blue", label="Fitted polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Polynomial Curve Fitting (degree={degree})")
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
 
print("Enter number of data points: ", end="")
n = int(input())
 
x = []
y = []
for i in range(n):
    a = int(input(f"  Enter x[{i+1}]: "))
    b = int(input(f"  Enter y[{i+1}]: "))
    x.append(a)
    y.append(b)
 
df = pd.DataFrame({"x": x, "y": y})
print("\nData Points:")
print(df.to_string(index=False))
 

a00 = np.sum(df["x"] ** 2)   
a01 = np.sum(df["x"])         
a10 = np.sum(df["x"])         
a11 = n                       
 
b0 = np.sum(df["x"] * df["y"])  
b1 = np.sum(df["y"])             
 
co_ef_matrix = np.array([[a00, a01],
                          [a10, a11]])
const_matrix  = np.array([b0, b1])
 
co_ef_matrix_inv = np.linalg.inv(co_ef_matrix)
result = np.dot(co_ef_matrix_inv, const_matrix)
 
m = result[0]   # slope
b = result[1]   # intercept
 
print(f"\n{'='*40}")
print(f"  Fitted Line: y = {m:.4f}x + {b:.4f}")
print(f"  Slope (m)  : {m:.4f}")
print(f"  Intercept  : {b:.4f}")
 
y_pred = m * df["x"] + b
mse    = mean_squared_error(df["y"], y_pred)
r2     = r2_score(df["y"], y_pred)
 
print(f"  MSE        : {mse:.4f}")
print(f"  R² Score   : {r2:.4f}")
print(f"{'='*40}")
 
plt.figure(figsize=(7, 5))
plt.scatter(df["x"], df["y"], color="blue", zorder=5, label="Data points")
plt.plot(df["x"], y_pred,    color="red",  linewidth=2, label=f"Fitted line: y = {m:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Linear Curve Fitting  |  R² = {r2:.4f}")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("stline_plot.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved to stline_plot.png")

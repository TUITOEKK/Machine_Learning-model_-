import numpy as np

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)  

m = 0.0  
b = 0.0  

lr = 0.01

epochs = 1000

n = len(X)

for i in range(epochs):

    y_pred = m * X + b
    
    error = y - y_pred
    
    mse = (1/n) * np.sum(error ** 2)
    
    dm = -(2/n) * np.sum(X * error) 
    db = -(2/n) * np.sum(error)     
  
    m = m - lr * dm
    b = b - lr * db

    if i % 100 == 0:
        print(f"Epoch {i}: MSE={mse:.4f}, m={m:.4f}, b={b:.4f}")

print("Final model: ŷ = {:.4f}X + {:.4f}".format(m, b))
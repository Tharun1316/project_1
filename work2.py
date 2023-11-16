import numpy as np

# Create a 2x3 array
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Create a 1x3 array
B = np.array([10, 20, 30,2])

# When we add A and B, NumPy automatically broadcasts B to match the shape of A
result = A + B

print(result)

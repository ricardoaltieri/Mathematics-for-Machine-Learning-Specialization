# Eigenvalues
import numpy as np

M = np.array([[4, -5, 6],
              [7, -8, 6],
              [3/2, -1/2, -2]])
vals, vecs = np.linalg.eig(M)
print(vals)
print(vecs)


import numpy as np
import math

N=10**8

h = 1.0 / N; s = 0.0
for i in range(N):
    x = h * (i + 0.5)
    s += 4.0 / (1.0 + x**2)
    estimated_pi = s * h

print(estimated_pi)

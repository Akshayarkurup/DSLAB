import numpy as np
x=np.arange(21)
print("Vector")
print(x)
print("After changing the sign")
x[(x>=9)&(x<=15)]*=-1
print(x)
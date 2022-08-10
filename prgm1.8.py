import numpy as np
x=np.array([2,4,1,5,3])
y=np.array([1,3,1,5,2])
print("orginal array",x,"\n",y)
print("checking whether two numbers are equal")
print(x==y)
print(np.equal(x,y))
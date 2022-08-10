import numpy as p
x=p.array([[3,2],[2,1]])
print("matrix")
print(x)
print("sum of elements")
print(p.sum(x))
print("sum of column",p.sum(x,axis=0))
print("sum of rows",p.sum(x,axis=1))
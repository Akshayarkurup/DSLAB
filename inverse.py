import numpy as np
def create_matrix(mc):
    print("enter the array"+str(mc)+"elements:")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    #print(arr)
    print("enter the array"+str(mc)+",Row column:")
    row,column = map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("Row and column size donot match with total elements!!retry")
        return create_matrix(mc)
    array_1 = array_1.reshape(row,column)
    print("array"+str(mc))
    print(array_1)
    print("Inverse:")
    return array_1
print(np.linalg.inv(create_matrix(1)))



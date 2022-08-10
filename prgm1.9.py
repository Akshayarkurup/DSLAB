import numpy as np
nums=np.arange(16,dtype='int').reshape(-1,4)
print("orginal array")
print(nums)
print("after swapping first and last rows:")
nums=nums[[-1,1,2,0]]
print(nums)
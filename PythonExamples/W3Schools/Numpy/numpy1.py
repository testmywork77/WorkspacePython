# Array object in Numpy is called 'ndarray'
# Convert Python list to ndarray
import numpy as np

thislist = [1,2,3,4,5]
numpyArray = np.array(thislist)

print(f"Numpy version: {np.__version__}")
print(f"thislist results: {thislist}")
print(f"numpyArray result: {numpyArray}")
print(f"thislist's dataType: {type(thislist)}")
print(f"numpyArray's dataType: {type(numpyArray)}")
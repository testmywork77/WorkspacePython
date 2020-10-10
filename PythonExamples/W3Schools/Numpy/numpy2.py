import numpy as np

thistuple = (1,2,3,4,5)
numpyArray = np.array(thistuple)

print(f"Numpy version: {np.__version__}")
print(f"thistuple results: {thistuple}")
print(f"numpyArray result: {numpyArray}")
print(f"thistuple's dataType: {type(thistuple)}")
print(f"numpyArray's dataType: {type(numpyArray)}")
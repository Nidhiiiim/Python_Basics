# Creation and execution of Basic Array
from array import *

# Declared an empty array
arr = array("i", [])
x = int(input("Please provide the size of 2 D Array: "))
print("Size of your 2D array is %d" %x)

for i in range(x):
    ele = int(input())
    arr.append(ele) # Pushing element to array
print(arr)

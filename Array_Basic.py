# Creation and execution of Basic Array
from array import *

# Declared an empty array
arr = array("i", [])
x = int(input("Please provide the size of 2 D Array: "))
print("Size of your 2D array is %d" % x)

for i in range(x):
    ele = int(input())
    arr.append(ele)  # Pushing element to array
print(arr)

# Removing Duplicates in input array
i = 0
while i < x - 1:
    j = i + 1
    while j < x:
        if arr[i] == arr[j]:
            del arr[j]
            x = x - 1
        j += 1
    i += 1
print(arr)
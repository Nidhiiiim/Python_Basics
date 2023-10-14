from array import array


def first_func():
    print("Hello here is my first function of this Demo!")


first_func()


def Cube(n):
    return n * n * n


try:
    n = int(input("Provide number you want cube of: "))
    print(Cube(n))
# will catch any kind of exception
except:
    print("Invalid Input")


def Min_fx(arr):
    return min(arr)


arr = []
s = int(input("Provide size of List: "))
print("Provide list of elements: ")
for i in range(0, s):
    a = int(input())
    arr.append(a)

print("Min is: " + str(Min_fx(arr)))

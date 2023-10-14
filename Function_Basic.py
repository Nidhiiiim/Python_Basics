from array import array


def first_func():
    print("Hello here is my first function of this Demo!")


first_func()


def Cube(n):
    return n * n * n


try:
    n = int(input("Provide number you want cube of: "))
    print(Cube(n))
    #x = 100/0
# will catch any kind of exception
except ZeroDivisionError:
    print("Divided by 0")
except ValueError:
    print("Invalid Input")



def Min_fx(arr):
    return min(arr)


arr = []
try:
    s = int(input("Provide size of List: "))
    print("Provide list of elements: ")
    for i in range(0, s):
        a = int(input())
        arr.append(a)
except ValueError:
    print("Invalid input")


print("Min is: " + str(Min_fx(arr)))

print("-----Reversing the String------")
s = input("Enter the string you want to reverse: ")
s = s + " "
temp = ""
rev_s = ""

for i in s:
    if i != " ":
        temp = i + temp
    else:
        rev_s = rev_s + " " + temp
        temp = " "
print(rev_s)


print("-----Making sure number enters is multiple of 7-----")

num = int(input("Provide the multiple of 7: "))
while num % 7 != 0:
    num = int(input("Re - provide the multiple of 7: "))
else:
    print("Here you goo!")

print("-----Acessing Values of Matrics.-----")

X = [[1,2,3,4],["a","s","d","f","g"],["Hello","Nidhi"]]
print(X)
## Will take individual lists
for i in X :
    for j in i :
        print(j, end="")
    print()
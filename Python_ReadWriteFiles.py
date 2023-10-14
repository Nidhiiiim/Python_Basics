## Declaring a var pointing to a file

emp_file = open("IBM.csv", "a")

# Reads Individual Lines, put each line inside array as elements.
# a - Append mode
# w - write mode (overwrites entire file from blank)
# r - Read mode

# To give all elements of file
for i in emp_file.readlines():
    print(i)

emp_file.write("\n 23324 234 23423 234234234 234234234")

# Will read the file
# print(emp_file.read())

emp_file.close()

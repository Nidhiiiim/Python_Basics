# Can Have multiple Data Types
# Used for creating Matrix

l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c"]
l3 = ["Nidhi" , "Mishra"]
l4 = [2.3, 4.5, 6.7]

# Retriving item with index

print(l1[0])

# Concatenation
l_concat = l1 + l2 + l3 + l4
print(l_concat)

l1.extend(l2)
print(l1)

# Appending Lists
l_append = [l2]
print(l_append)

# Length of List
print(len(l1))

#Minimum of List
print(min(l4))

#Maximum of List
print(max(l4))

#Sum of List
print(sum(l4))

#Avg of List
print(sum(l4)/ len(l4))


# Seperating even and odd from list of first 10 numbers

basic_list = list(range(1,11))
print(basic_list)
odd = []
even = []
for i in basic_list:
    if i % 2 == 0:
        odd.append(i)

        continue
    else:
        even.append(i)

print(odd)
print(even)

odd_list = basic_list[::2]

print("------")
print(odd_list)
even_list = basic_list[1::2]
print("------")
print(even_list)

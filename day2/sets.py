# set = {1,5,4,7,3,2,6,8,9,10}
# print(set)
# print(type(set))

# # a = set() # creates an empty set
# a= {3}
# a.add(1) # adds an element to the set
# a.add(2)
# a.add('Mazhar')
# a.add(3.14)
# print(a)
# print(len(a)) # prints the length of the set

# b = {1,2,3,4,5,6,7,8,9,10}
# result = a.union(b) # combines two sets
# print(result)

# result = a.intersection(b) # finds common elements in two sets
# print(result)

s = set()
n = int(input("Enter the number of elements in the set: "))
s.add(n)
n = int(input("Enter the number of elements in the set: "))
s.add(n)
n = int(input("Enter the number of elements in the set: "))
s.add(n)
n = int(input("Enter the number of elements in the set: "))
s.add(n)
n = int(input("Enter the number of elements in the set: "))
s.add(n)
n = int(input("Enter the number of elements in the set: "))
s.add(n)
print("Set elements:", s)
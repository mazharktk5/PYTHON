
my_dic = {
    "name": "Mazhar",
    "age": 30,
    "city": "Karachi",
    "country": "Pakistan"
}

my_dic2 = {
    "name": "Ali",

    "age": 25,
    "city": "Lahore",
    "country": "Pakistan"
}

dictionary_list = [my_dic, my_dic2]
print("Dictionary List:", dictionary_list)

# Accessing elements in a dictionary
print("Name:", my_dic["name"])
print("Age:", my_dic["age"])
print("City:", my_dic["city"])

# Adding a new key-value pair
my_dic["profession"] = "Engineer"
print("Updated Dictionary:", my_dic)

# Modifying an existing key-value pair
my_dic["age"] = 31
print("Modified Age:", my_dic["age"])

# Removing a key-value pair
del my_dic["city"]
print("Dictionary after removing city:", my_dic)

# Checking if a key exists in the dictionary
if "country" in my_dic:
    print("Country exists in the dictionary.")

# Iterating through the dictionary
for key, value in my_dic.items():
    print(f"{key}: {value}")

# Getting the keys and values of the dictionary
keys = my_dic.keys()
values = my_dic.values()
print("Keys:", keys)
print("Values:", values)

# Merging two dictionaries
my_dic3 = {
    "hobby": "Reading",
    "language": "Python"
}
my_dic.update(my_dic3)
print("Merged Dictionary:", my_dic)
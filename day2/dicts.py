# marks = {
#     "Ali": 85,
#     "Ahmed": 90,
#     "Fatima": 78,
#     "Sara": 92,
#     "John": 88
# }

# print("Marks of students:", marks.items())
# print("Marks of students:", marks.keys())
# print("Marks of students:", marks.values())
# marks.update({"Ahmed": 95})
# print(marks)
# print("Marks of Ahmed:", marks["Ahmed"])

dicts = {
    "apple": "seb",
    "banana": "kela",
    "orange": "narangi",
    "grape": "angoor",
}

fruits = input("Enter a fruit name in English: ").strip().lower()
if fruits in dicts:
    print(f"The translation of '{fruits}' in Urdu is: {dicts[fruits]}")
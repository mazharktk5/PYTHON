marks = {
    "Ali": 85,
    "Ahmed": 90,
    "Fatima": 78,
    "Sara": 92,
    "John": 88
}

print("Marks of students:", marks.items())
print("Marks of students:", marks.keys())
print("Marks of students:", marks.values())
marks.update({"Ahmed": 95})
print(marks)
print("Marks of Ahmed:", marks["Ahmed"])
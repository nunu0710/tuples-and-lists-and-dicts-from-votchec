student_record = ("John Doe", 20, "Computer Science")

# creating multiple variable from tuple
name, age, department = student_record

# same as line number 4
# name = student_record[0]
# age = student_record[1]
# department = student_record[2]

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Department: {department}")

second_record = department, age, name
print(second_record)
print(student_record)
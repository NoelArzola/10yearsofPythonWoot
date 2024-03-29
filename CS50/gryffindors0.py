students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students] list comprehension

#dictionary comprehension
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

for i, student in enumerate(students, start=1):
    print(i, student)
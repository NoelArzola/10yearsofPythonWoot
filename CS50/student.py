import csv

students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         # student["name"] = name
#         # student["house"] = house
#         students.append(student)

# def get_name(student):
#     return student["name"]        

# for student in sorted(students, key=get_name): # key=lambda student: student["name"]
#     print(f"{student['name']} is in {student['house']}")

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name}, is in {house}")
#         """
#         Hermione, is in Gryffindor
#         Harry, is in Gryffindor
#         Ron, is in Gryffindor
#         Draco, is in Slytherin
#         """
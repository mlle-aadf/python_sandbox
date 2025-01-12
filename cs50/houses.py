### dict

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    name, house, patronus = student.values()
    print(f"{name} is in {house} and their patronus is a {patronus}.")


# name = input("Who's house? ")

# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student])

# print(students["Hermione"])
# print(students[name])
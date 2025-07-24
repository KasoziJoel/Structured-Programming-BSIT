

#lists and dictionaries

students = [
    {'username': "b2647.ucu.ac.ug",'password': "12345"},
    {'username': "b2647.ucu.ac.ug",'password': "12345"},
    {'username': "b2647.ucu.ac.ug",'password': "12345"}

]

print(students[1]["username"])

student = {'username': "b2647.ucu.ac.ug",'password': "12345"}

students.append(student)
students.insert(1, student)

print(students)

from classes import student

student1 = student(1, "jose", "derecho")
student2 = student(2, "Mose", "derecho")
student3 = student(3, "Marco", "derecho")

students=[]
students.append(student1)
students.append(student2)
students.append(student3)

#mostrar lista
for stu in students:
    print(stu)

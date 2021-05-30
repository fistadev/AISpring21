from classes_objects_Student import Student

student1 = Student("Jim", "Business", 3.1, True)
student2 = Student("Pam", "Art", 4.2, False)

print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)
print("Honor roll? ", student1.on_honor_roll())
print("---")
print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.is_on_probation)
print("Honor roll? ", student2.on_honor_roll())
print("---")


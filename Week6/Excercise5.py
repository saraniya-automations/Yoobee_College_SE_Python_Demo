id = [1,2,3]
names = ["Alice","Bob","Cathy"]
grade = ['A','B','A+']
students = list(zip(id,names,grade))
print(students)


student_dict = dict(zip(id,zip(names,grade)))
print(student_dict)

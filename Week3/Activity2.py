class student:
    def __init__(self,name):
        self.studentName = name
        self.studentGrades = []

    def setStudentGrade(self,studentGrade):
        self.studentGrades.append(float(studentGrade))
    
    def calculateAverage(self):
        total = 0
        for grade in self.studentGrades:
            total = total + grade
        return total/len(self.studentGrades)


student1 = student('StudentA')
student2 = student('StudentB')

student1.setStudentGrade('60')
student1.setStudentGrade('70')
student1.setStudentGrade('80')

student2.setStudentGrade('64')
student2.setStudentGrade('75')
student2.setStudentGrade('86')

print('Average of first student is : ',student1.calculateAverage())
print('Average of second student is : ',student2.calculateAverage())
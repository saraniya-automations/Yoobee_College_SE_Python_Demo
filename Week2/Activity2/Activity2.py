import numpy as np

student1 = np.array([78, 85, 90])
student2 = np.array([88, 79, 92])
student3 = np.array([84, 76, 88])
student4 = np.array([90, 93, 94])
student5 = np.array([75, 80, 70])


scores = np.array([student1,student2,student3,student4,student5])

# Average score for each student
print('Average score of first student ',np.mean(student1)) 
print('Average score of second student ',np.mean(student2)) 
print('Average score of third student ',np.mean(student3)) 
print('Average score of fourth student ',np.mean(student4)) 
print('Average score of fifth student ',np.mean(student5)) 

# Total score for each student
print('Total score of first student ',np.sum(student1)) 
print('Total score of second student ',np.sum(student2)) 
print('Total score of third student ',np.sum(student3)) 
print('Total score of fourth student ',np.sum(student4)) 
print('Total score of fifth student ',np.sum(student5)) 

# Average score for each subject
print('Average score of subject 1:', np.mean(scores[:, 0])) 
print('Average score of subject 2:', np.mean(scores[:, 1])) 
print('Average score of subject 3:', np.mean(scores[:, 2])) 

total = [np.sum(student1),np.sum(student2),np.sum(student3),np.sum(student4),np.sum(student5)]
highest = max(total)

print('Student with highest total score is at row:', total.index)

# Add 5 bonus points to third subject
scores[:, 2] = scores[:, 2] + 5
print(scores)

# print('**************************')

# x,_,y = (1,"ignored",3)
# print(x,y,_)



# print('**************************')
# names = ["sara1","sara2","sara3","sara4"]
# for i in range(len(names)):
#     print(i,names[i])



# print('**************************')
# names1 = ["sara1","sara2","sara3","sara4"]
# for i ,names1 in enumerate(names1):
#     print(i,names1)



# print('**************************')
# names2 = ["A","B","C","D"]
# for i ,names2 in enumerate(names2, start = 1):
#     print(i,names2)



print('**************************')

names3 = ["A","B","C"]
ages = [25,30,35]

paired = zip(names3,ages)
print(paired)

print('**************************')

paired = list(zip(names3,ages))
print(paired)
print(type(paired))

dic1 = dict(paired)
print(dict)
import numpy as np

temperatures = np.array([18, 19, 20, 25, 30, 20, 22])
days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

average_tmp = np.mean(temperatures)
max_tmp = np.max(temperatures)
min_tmp = np.min(temperatures)

print('Maximum temperature is :', max_tmp)
print('Minimum temperature is :', min_tmp)
print('Average temperature is :', average_tmp)


for temperature,day in zip(temperatures,days):
    temInF = temperature * 9/5 +32
    print('Temperature in ',day,' is',temInF,'F')


for temperature,day in zip(temperatures,days):
    if temperature > 20 :
        print(day,' temperature is above 20C ',temperature,'C') 
   





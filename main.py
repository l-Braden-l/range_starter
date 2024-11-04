#Braden Leach
# Nov 4 2024
# Range Starter



#4-3
#for i in range(1,21):      #done
    #print(i)
#4-4
#for i in range(1,1000001):     #done
    #print(i)
#4-5
#numbers = []
#for number in range(1,1000001):
    #numbers.append(number) 
 
    #nums_sum = sum(numbers)
    #print(f'{nums_sum}')
#4-6
#for i in range(1,21,2):        #done
    #print(i)
#4-7
#for i in range(3,30):
    #print(i)
#4-8
cubes = []
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for cube in cubes: 
 for num in numbers:
  print(f'The cube of {num} is {cube}') 
for num in numbers:
    # Do the math each time the loop loops (runs)
    result = num ** 3
    cubes.append(result)
print('The original list of numbers:')
print(numbers)
print('The list of cubes:')
print(cubes)

for num in range(11):
    # Do the math each time the loop loops (runs)
    result = num ** 3
    cubes.append(result)
print('The original list of numbers:')
print(numbers)
print('The list of cubes:')
print(cubes)

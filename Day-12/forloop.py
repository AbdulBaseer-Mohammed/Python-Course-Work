'''
#str list tuple set dict range()

#for i in seq:
     #stmt

s = 'codegnan'
for i in s:
    print(i)

a = input("Enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)
       
s = (10,20,23,45,67,68,90,53,34,)
for i in s:
    print(i) 
    '''
'''
sumoftuple = 0
a = list(map(int,input("Enter the numbers: ").split()))
for i in a:
    sumoftuple+=i

print("Sum of the numbers is: ",sumoftuple)    
'''

'''
max = 0
a = set(map(int,input("Enter the number :").split()))
for i in a:
    if i > max:
        max = i
print("Maximum number is: ",max)
'''
'''
marks = {'python':90,'mysql':80,'fastapi':70}
for i in marks:
    print(i,marks[i])

    sum = 0
    marks = {'python':90,'mysql':80,'fastapi':70}
    for i in marks:
        sum+=marks[i]


        print("Total marks is: ",sum)
        '''
'''
#range(start,end+1,step)
#range(0,,1)


for i in range(1,11):
    print(i,end=' ')


for i in range(20,0,-1):
    print(i,end=' ')


for i in range(2,101,2):
    print(i,end=' ')
'''

'''
n =int(input("Enter the table number: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}") 
    '''

'''
#codegnan
#c0vmvmvin8hv98ray9wry9yr

c = 'codegnan'
for i in range(len(c)):
    print(c[i],end=' ')
    '''

#range(start,end+1,step)
#range(0,,1)



#[12,34,45,67,89,90]
#0+3+6+9+12+15 = 33

'''
sum = 0
c = [12,34,45,67,89,90]
for i in range( len(c),):
   if c[i]%2==0:
       sum+=c[i]

print(sum)
'''



'''
#[12,34,45,67,89,90]
#2*5 = 10


sum = 0
c = [12,34,45,67,89,90]
for i in range(len(c)):
    if c[i]%2==0:
        sum-=i
        
print(sum)        
'''


for i in range(1,11):
    if i%2==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)    
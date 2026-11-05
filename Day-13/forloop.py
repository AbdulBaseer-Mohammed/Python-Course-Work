

'''
pin =12345


for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin==pin:
        print("Access granted")
        break
    else:
            print("Access denied")

else:
     print("Maximum attempts reached ! try again after 20 seconds")
     '''
'''
l =[2,3,7,23,45,67,89,90]
search = int(input("Enter the number to search: "))


for i in range(len(l)):
    if l[i] == search:
        print(f"{search} is found at  {i}")
        break
else:
    print(f"{search} is not found ")
'''
'''
c = (1,2,3,4,5,6,7,8,9,10)
for i in enumerate(c):
    print(f"{i[0]} : {i[1]}")   
'''

'''
c = {1,2,3,4,5,6,7,8,9,10}
for i in enumerate(c):
    print(f"{i[0]} : {i[1]}") 
    '''
'''
c = [1,2,3,4,5,6,7,8,9,10]
for i in enumerate(c):
    print(f"{i[0]} : {i[1]}") 
    '''


c = {"k1":"v1","k2":"v2","k3":"v3"}
for i in enumerate(c):
    print(i[0],i[1],c[i[1]])
    
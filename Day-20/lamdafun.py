''' # var = lambda arg: #sts


sot = lambda a,b,c: a+b+c

print(sot(10,20,30))


gst = lambda price: price+ price*0.18

print(gst(1000))

avg = lambda l: sum(l)/len(l)
l=[99,80,60,50,86]
print(avg(l))

iseven = lambda n: "Even" if n%2==0 else "Odd"
print(iseven(10))
print(iseven(17))


isvowel = lambda ch: "Vowel" if ch in 'aeiouAEIOU' else "Consonant"
print(isvowel('a'))
print(isvowel('z'))
'''
'''
check = lambda data,pro: (f"Product Price: {data[pro]['price']}" if data[pro]["stock"]>0 else "Out of stock") if pro in data else "Product is unavailable"

data = {
    'apple':{'stock':10,'price':50},
    'mango':{'stock':20,'price':40},
    'banana':{'stock':60,'price':150},
    'sapota':{'stock':100,'price':250},
    'coconut':{'stock':30,'price':350},
}

print(check(data,'mango'))
'''

#def addten(l):
   # for i in range(len(l)):
  #      l[i]+=10
 #   return l

#l=[9,2,4,34,5,45,54,2]
#print(addten(l))



#def domain(d):
   # for i in range(len(d)):
  #      d[i] = (d[i].split('@')[1]).split('.')[0]
 #   return d 

#d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']    
#print(domain(d))
'''

l=[9,2,4,34,5,45,54,2]
addten = list(map(lambda i:i+10 , l))
print(addten)


d=['xyy@codegyan.com','abc@gmail.com','pqr@yahho.com']
domain = list(map(lambda i:(i.split('@')[1]).split('.')[0],d))
print(domain)

c = ['sadfdgh','dsgfh','fds','gfds']
cu = list(map(lambda i:i.upper(),c))
print(cu)

d = {'a':20,'b':30,'c':10000,'d':5000,'e':2000}

gst =  dict(map(lambda i:(i[0],i[1]+i[1 ]*0.18),d.items()))
print(gst)
'''
'''
l=[1,2,3,34,56,45,64,54,56,7,89]
even = list(filter(lambda i:i%2==0,l))
print(even)

a=['a','d','i','e','(((o','k','j','l']
vowels = list(filter(lambda i: i in'aeiouAEIOU',a))
print(vowels)
'''
'''
from functools import reduce

l=[2,45,6,5,7,3,2,9]
sumofl = reduce(lambda sum,i:sum+i,l)

print(sumofl)
'''
from functools import reduce

l=[2,3,45,6,78,9,23]
maxofl = reduce(lambda max,i:max if max>i else i,l)

print(maxofl)

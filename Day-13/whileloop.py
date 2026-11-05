'''
l = [1,2,0,0,0,0,0,4,0,9,0,7,0,6,9,0]
while 0 in l:
    l.remove(0)

print(l)
'''
'''
i=5
while i<101:
    print(i)
    i+=5
'''
'''
i=2
while i<101:
    print(i)
    i+=2
'''
'''
a = [1,2,3,4,5,6,7,8,9,]
i=0
while i<len(a):
    print(i,a[i])
    i+=1
'''
'''
a = 'python programming'
i=0
while i<len(a):
    print(i,a[i])
    i+=1
    '''
'''
a = [1,2,3,4,5,6,7,8,9,]
i=0
while i<len(a)-1:
     i+=1
     if a[i] == 5:
          continue
     print(i,a[i])
'''

c='pythonprogramming'
i=0
j=len(c)-1
while i<=j:
    if i==j:
        print(c[i])
    else:
        print(c[i],c[j])
    i+=1
    j-=1
        
     



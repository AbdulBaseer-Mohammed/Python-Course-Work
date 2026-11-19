
'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(0)
'''
'''
def display(n) :
    if n == len(s):
        print()
        return
    print(s[n],end='')
    display(n+1)
    print(s[n],end='')


s= 'python programming'    
display(0)
'''
'''
def display(n):
    if n == len(s):
        return
    print(s[:n+1])
    display(n+1)


s= 'Mohammed Abdul Baseer'
display(0)
'''
'''
def display(n,w):
    if n > len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)

s= 'codegnan'
display(0,6)
'''
'''
def display(n):
    if n < 1:
        return 0
    return n + display(n-1)

print(display(10))
'''
'''
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)

print(factorial(6))
'''
l = [23,45,67,89,45,32,22]
def sumoflst(n):
    if n == len(l):
        return 0
    return [n]+sumoflst(n+l)

print(sumoflst(0))


'''
def display():
    global n
    n=10
    print("inside:",n)


display()
print("Outside:",n)
'''
'''
def display():
    course ="JFS"
    print("Starting:",course)
    def update():
        nonlocal course
        course = "PFS"
        print("updated:",course)
    update()
    print("final:",course)    


    display()'''

s = "codegnan"

len = 10


print(max(s))

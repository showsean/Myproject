x = 50
def func():
    global x
    print 'x is ',x
    x = a = 2
    print 'changed gobal x to ',x
func()
print 'Value of x is ',x
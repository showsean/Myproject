def total(initial=5,*numbers,**keywords):
    count = initial
    for number in numbers:
        count += number
    print 'count is count+numbers',count
    for key in keywords:
        count += keywords[key]
    print 'count is count + numbers + keywords',count
    return count
print total(10,1,2,3,vagetables=50,fruits=100)
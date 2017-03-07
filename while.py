number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer:'))
    if guess == number:
        print 'Congratulations,you gussed it.'
        #This cause the while loop to stop
        running =False
    elif guess < number:
        print 'No,it is a little higher than that.'
    else:
        print 'No,it is a little lower than that.'
else:
    print 'while,the loop is over.'
    #Do anything you want do here
print 'Done.'


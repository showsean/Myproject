try:
    text = raw_input('Entersomething-->:')
except EOFError:
    print 'Why did you do an EOF on me?'
except KeyboardInterrupt:
    print 'You canceled the operation.'
else:
    print 'You enter: "{}"'.format(text)
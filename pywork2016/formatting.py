import logging
logging.info('info')
logging.debug('debug')
x='hello'
y='SEONIL'
y=y.replace('SEONIL', 'ssoniri')
z='hi%10s'%y
d=2000000
#if space is not enough, strings are conserved, not lost
print('hi%6s'%x+'%10s'%y +'%4d'%d)
print(z)
y='    '+y+'    '
print(y.rstrip()+'space')
#similarly, .lstrip() is also notable
k=y.rstrip()+'space'
k=k.replace('space', ' is killing himself?')
print(k)
#print(type(x.count('l')))
print(k.split('i'))
#.split('x') split strings into list of splited string with specified identifier 'x'. default identifier is ' '
adv_format2='sth {a} wrong. I {b} my ticket way to home'.format(a='went', b='lost')
print(adv_format2)
#numberofsth = input("type number of dementers: ")
#verb = input('what\'s dementer(s) doing to you?(gerund) ' )
#adv_format='sth strange. {0} dementers are {1} me!'.format(numberofsth,verb)
#print(adv_format)
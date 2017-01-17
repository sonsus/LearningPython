#1008function

#passing parameter with default value
def say_myself(name,major,state='good'):
#	global name 
	return (name,major,state)


'''
global name

if the line above have been added in the def block, name variable is declared as global one
but this makes the function subjective to external env, which would not be a good choice for
designing
'''

res=say_myself('seonil','chem')
print(res)

#recursive function
def recurPower(base, exp):
    if exp <=0:
        return 1
    return base * recurPower(base, exp - 1)

print(recurPower(3,2)==3**2)

#below do not work: parameter w/o default cannot follow one with default
'''
def say_myself2(name,state='good',major):
	return (name,state,major)

print(say_myself2('seonil','chem'))

'''
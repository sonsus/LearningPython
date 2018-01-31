#class overiding

class Bird:
	def fly(self):
		raise NotImplementedError

class Eagle(Bird):#Eagle class inherited class Bird.
	pass

if __name__=='__main__':
	eagle = Eagle()
try:	
	eagle.fly() #NotImplementedError(built-in error) occurs here
except:
	pass

#customizing error class

class Custom_error(Exception):
	
	def __init__(self,msg):
		self.msg=msg
	
	def __str__(self):
		return self.msg


def say_simon(simon):
	if simon=='dumb':
		raise Custom_error("not even close.")
	elif simon=='good man':
		print('correct he is a %s'%(simon))
	elif simon=='willful':
		print('yes, sometimes he is\nbut not always')
		raise Custom_error("he's better than good.")

if __name__=='__main__':
	try:
		say_simon('dumb')
	except Custom_error as E:
		print(E)
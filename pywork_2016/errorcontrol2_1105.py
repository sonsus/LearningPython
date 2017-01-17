#errorcontrol_bypassing

try:
	f=open('dont_exist.txt', 'w')
except:
	pass

# then error is just passed (no error warning appears)
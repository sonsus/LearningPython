##How to bash-command on python interpreter (or in code)

####os.system    
returns only execution result (success or failure)  

````python
import os

os.system("ls -al | grep user ") #pipe is available

````

####os.subprocess

````python
import subprocess as sb

sb.run(["ls", "-al"]) #same as os.system("ls -al")

sb.run(["chrome", "https://www.facebook.com"])   #open facebook page!
sb.check_call(["python","example.py"])   #similar with run
sb.check_output(["python","example.py"])   #return output of the execution
````

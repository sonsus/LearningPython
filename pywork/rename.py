#rename.py

import os
import subprocess as sb

cwd=os.getcwd()

for (i,song) in enumerate(os.listdir(cwd)):
    if song=="rename.py": continue
    else:
        commandstr="rename {songname} {num}.wav\n".format(songname=song, num=str(i) ) 
        sb.run(commandstr.split())

print("name converted well!")

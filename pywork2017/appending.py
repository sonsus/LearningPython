#appending to the file
#reading and, after it, writing (r+)

with open("file.txt","r+") as file:
    content=file.read()
    file.seek(0,2)
    file.write("\nccccc")


#Here we use fileObject.seek(offset[, whence]) with offset 0 & whence 2 that is seek to 0 characters #from the end. And then write to the file.

#OR (Alternate using SEEK_END):

import os
with open("file.txt", 'rb+') as file:
    file.seek(-1, os.SEEK_END)
    file.write("\nccccc\n")


#Here we seek to SEEK_END of the file(with the os package) and then write to it.
import os
import glob

print(os.environ)
print(os.getcwd())
os.chdir("C:/Users/xozmf/documents/2016-2/")
print(os.getcwd())

os.mkdir("directory C:/Users/xozmf/documents/2016-......")
os.rmdir("C:/Users/xozmf/documents/2016-......")
os.unlink("filename") #removing the file
os.rename(src, dst) #change the name of the file src to dst

glob.glob(pathname) #files in the dir into list
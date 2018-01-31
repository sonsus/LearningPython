import sys
args=sys.argv[1:]


#file write: Beware-opened file will be cleared to be empty
f=open("C:/Users/xozmf/Documents/2016-2/pywork/newfile.txt", 'w')
for i in range(0,11):
    f.write("%s: is here\n"%i)
f.close()

#file append: When you want to add sth.
k=open("C:/Users/xozmf/Documents/2016-2/pywork/newfile.txt", 'a')
#'a' option only works when the file already exists
list_food=['burrito', 'chicken']
list_want=['good job','being a helpful son','enjoying the life']
for n,item in enumerate(list_food):
    k.write("Eat list %d: %s \n" %(n,item))
k.close()

#with makes a block so that all the objects could be used locally.
with open("C:/Users/xozmf/Documents/2016-2/pywork/newfile.txt", 'a') as k:
    for items in list_want:
        k.write(items+"\n")
    for things in args:
    	k.write(things.upper()+" ")
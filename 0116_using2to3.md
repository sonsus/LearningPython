#Using 2to3

````bash
$2to3 test.py
  --- test.py     (original)
  +++ test.py     (refactored)
  @@ -1,2 +1,2 @@
   #2to3test
  -print "superman"
  +print("superman")
````
####shows difference in code of ver2 and 3

    
    
    
````bash
$2to3 -w test.py
````
####result in ...
  test.py (ver3)
  test.py.bak (original, ver2)
    
    
    
####flag options
-w  write in file with backup file, *.bak
-n  no backup
-l  list available fixes: not sure how or when to use
-f  fix: same as above

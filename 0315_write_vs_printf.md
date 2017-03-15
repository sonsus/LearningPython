##EC4205 OS mini HW: printf() vs write()     
    
printf calls write() which requires syscall
write is direct syscall function

what looks faster?

###method    
python to run similar C codes of printing "p" write() and printf() and check the time needed

####get_laps_c.py
''''
import os
import subprocess as sb
from time import clock

sb.run(['gcc','printftest.c','-o','print'])
sb.run(['gcc','writetest.c','-o','write'])

startprint=clock()
sb.run(['print'])
print_lap=clock()-startprint
startwrite=clock()
sb.run(['write'])
write_lap=clock()-startwrite

print("\n\n\n write(): {0}s\n print(): {1}s".format(write_lap, print_lap))
````    
     
####printftest.c    
````C
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

void main(){

for(int i = 0; i < 300; i++ ) {
    printf( "p" );
}
return;
}

````    


####writetest.c    
````C
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

void main(){
size_t len = strlen("p");
for(int i = 0; i < 300; i++ ) {
    write( STDOUT_FILENO, "p", len );
}
return;
}
````


###RESULT:    
#####write() lost. it increasingly time expensive accoding to number of loops while printf shows negligible runningtime    
#####This is because printf() not alsways call write that needs context switching but write in buffer to faster I/O

300000 loops    
 write(): 38.02788286335628s       
 print(): 0.03321697109619989s       

30000 loops    
 write(): 5.228296188784547s    
 print(): 0.03282091284182665s    
    
3000 loops     
 write(): 0.5773472790918673s    
 print(): 0.03195393166304619s   
    
300 loops     
 write(): 0.0680761349544352s   
 print(): 0.033000829548843764s    
   
30 loops    
 write(): 0.034026596277776905s   
 print(): 0.03055263408926525s   
    
3 loops   
 write(): 0.02557775601604036s    
 print(): 0.030334077552553185s    
    
0 loop    
 write(): 0.03292837986816573s   
 print(): 0.029377138020264173s    

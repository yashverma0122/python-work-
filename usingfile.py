'''
read() it will read complete file and will give the string
read(n) will read the n no of characters
readlines() will read all thel lines and will give list
properties of file
readable will give true if file is open in read mode
writeable will give true if file can be use for writig
opened will give true if file is opened
closed will give true if the file is closed
mode will give the mode of file
'''
import os
if os.path.isfile('myfile.txt'):
    print('file exist')
    f1=open("myfile.txt","r")
    k=f1.read()
    print('file is still opned')
    f1.readable()

    print(k)
    print('file is still opned',f1.readable)
    f1.close()
    
    
else:
    print('file not exist')

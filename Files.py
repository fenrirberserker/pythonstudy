import os
import shutil

source = "D:\\IT\\DEV\\STUDY\\PYTHON\\resources\\filetest.txt"
dest = "D:\\IT\\DEV\\STUDY\\PYTHON\\resources\\filetest2.txt"

if os.path.exists(source):
    print("exists")
    if os.path.isfile(source):
        print("Is a file")
else:
    print("doesn't exists")

#read
try:
    with open(source, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")

#write
try:
    with open(source, 'a') as file:#w for write
        file.write("\nWhat's up! Hello there")
except FileNotFoundError:
    print("File not found")

#copy a file
shutil.copyfile(source, dest)

#move a file
newfile = "D:\\IT\\DEV\\STUDY\\PYTHON\\resources\\filetest3.txt"
try:
    if os.path.exists(newfile):
        print("There's a file there")
    else:
        os.replace(dest,newfile)
        print(dest+" was moved")
except FileNotFoundError:
    print("File not found")

#delete a file
os.remove(newfile)
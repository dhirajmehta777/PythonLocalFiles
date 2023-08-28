# manual steps to write to a file
"""
open notepad and create file
write in the file
close the file
"""
#########################################
"""
Mode
Read mode:r
Write mode:w
Append mode:a
Read/Write:r+
"""
#open(filename, mode)
#how to create file
# f=open("/home/excellarate/fileIO/writedemo.txt","w")
# f.write("this is first line")
# f.close()
##############################################################
# f=open("/home/excellarate/fileIO/writedemo1.txt","w")
# l=[60,30,40,50,80]
# for items in l:
#     f.write(str(items)+"\n")
# f.close()
#############################################################
#append mode:this mode will not override the existing content wereas write mode overrides the existing content
f=open("/home/excellarate/fileIO/writedemo1.txt","a")
l=[60,30,40,50,80]
for items in l:
    f.write(str(items)+"\n")
f.close()

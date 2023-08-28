# fw=open("demofile.txt","w")
# fw.write("1st line")
# fw.close()#if we wont close the file then the content will not be displayed
# # in the console.
#
# fr=open("demofile.txt", "r")
# print(fr.read())
# fr.close()
#######################################################
with open("demofile.txt", "w") as fw:
    fw.write("this line is from with operation")
with open("demofile.txt", "r") as fr:
    print(fr.read())
#here with as keyword will handle the closing of file.
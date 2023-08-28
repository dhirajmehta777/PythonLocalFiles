#read content
# f=open("/home/excellarate/fileIO/writedemo1.txt","r")
# # print(f.read())
# # f.close()
#
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

##########################################
#Read And Write content
f1=open("writedemo.txt", "r+")
f1.write("this is line2")
# f1.close()
# f1=open("writedemo.txt","r+")
print(f1.read())
f1.close()

import glob
import subprocess
input_dir="/home/excellarate/example/"
filepath=list(glob.glob("{0}/**/*.py".format(input_dir),recursive=True))
#print(filepath)
for file in filepath:
    p1=subprocess.run(['2to3',file],stdout=subprocess.PIPE,text=True)
    #print(p1.stdout)
    if len(p1.stdout)==0:
        print("This file doesn't required any modifications:",file)
    else:
        print("This file needs modification:",file)














    # print(p1.stdout)
    # p2=subprocess.run(['grep','-n','refactored'],capture_output=True,text=True,input=p1.stdout)






















    #for output in p2.stdout:
        # if p2.stdout.find('refactored'):
        #     print(p2.stdout)
    #         list1.append(output)
    #     elif(p2.stdout.find('No changes')):
    #         list2.append(output)
    # print(''.join(list1))
    # print(list2)
    # #print(p1.stdout)
    #print(p1.returncode)
#     if p1.returncode==0:
#         list1.append(file)
#     else:
#         list2.append(file)
# print(list1)
# print(list2)







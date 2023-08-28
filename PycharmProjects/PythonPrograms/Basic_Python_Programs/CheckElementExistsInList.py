#Approach1:Using loop
# mylist=[1,6,5,2,3,4]
# ele=4
# flag=0
#
# for i in mylist:
#     if(i==ele):
#         print("element found...")
#         flag = 1
#         break
# if(flag == 0):
#     print("element not found...")

#Approach2:using IN operator
mylist=[1,6,5,2,3,4]
ele=200
if ele in mylist:
    print("element found...")
else:
    print("element not found...")

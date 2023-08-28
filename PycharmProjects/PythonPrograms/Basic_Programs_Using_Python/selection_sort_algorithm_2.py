#list1=[56,0,2,2,6,0]
num=int(input("how many numbers you want to enter?:"))
list1=[int(input("enter number:")) for x in range(num)]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)#here we need to change the statement
    if list1[i]!=list1[min_index]:
        list1[i], list1[min_index]=list1[min_index], list1[i]
print(list1)

"""
the adove program is to sort all the values including duplicate value in a list into an ascending order
"""
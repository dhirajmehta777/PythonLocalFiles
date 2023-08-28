list1=[56,0,2,2,6,0]
print(list1)
for i in range(len(list1)-1):
    min_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j]<min_val:
            min_val=list1[j]

    min_index=list1.index(min_val,i)#here we need to change the statement
    if list1[i]!=list1[min_index]:
        list1[i], list1[min_index]=list1[min_index], list1[i]
print(list1)

list1=[56,0,2,2,6,0]
print(list1)
for i in range(len(list1)-1):
    max_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j]>max_val:
            max_val=list1[j]

    max_index=list1.index(max_val,i)#here we need to change the statement
    if list1[i]!=list1[max_index]:
        list1[i], list1[max_index]=list1[max_index], list1[i]
print(list1)


"""
the above sorting methods are without using build in functions min and max(list1)
"""
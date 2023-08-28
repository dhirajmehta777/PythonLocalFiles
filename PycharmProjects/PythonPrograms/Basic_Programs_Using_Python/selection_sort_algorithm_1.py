# list1=[56,3,2,78,6,0]
# min_val=min(list1)
# min_index=list1.index(min_val)
# list1[0], list1[min_index]=list1[min_index], list1[0]
# print(list1)

list1=[56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    list1[i], list1[min_index]=list1[min_index], list1[i]
print(list1)

"""
decending order
"""
list1=[56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    max_val=max(list1[i:])
    min_index=list1.index(max_val)
    list1[i], list1[min_index]=list1[min_index], list1[i]
print(list1)

"""
these above sorting method is only applicable for non duplicate numbers in a list
"""
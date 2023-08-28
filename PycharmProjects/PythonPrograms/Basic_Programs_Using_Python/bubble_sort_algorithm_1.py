"""
Bubble Sort:
Sometimes reffrered as sinking sort, is a simple sorting algorithm which sorts n number of
elements in a list by comparing the each pair of adjecent items and swaps them if they are in wrong
order
"""
"""
Asscending Order-Algorithm:
1. starting with first element(index=0) compare the current element with the next element of the list
2. if the current element is greater then next element of the list swap them.
3. if the current element is less then the next element, move to the next element, repeat step 1
"""
list1=[10,15,4,23,0]
print("unsorted list",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print("sorted list", list1)

"""
Descending Order
"""
#list1=[10,15,4,23,0]
# num=int(input("how many numbers you want to enter:"))
# print("enter values:")
# for k in range(num):
#     list1.append(int(input()))
# print("unsorted list",list1)
# for j in range(len(list1)-1):
#     # for i in range(len(list1)-1):
#     for i in range(len(list1) - 1-j):
#         if list1[i]<list1[i+1]:
#             list1[i],list1[i+1]=list1[i+1],list1[i]
#             print(list1)
#         else:
#             print(list1)
#     print()
# print("sorted list", list1)
list1=[]
num=int(input("how many numbers you want to enter:"))
print("enter values:")
for k in range(num):
    list1.append(int(input()))
print("unsorted list",list1)
for j in range(len(list1)-1,0,-1):
    # for i in range(len(list1)-1):
    for i in range(j):
        if list1[i]<list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]

print("sorted list", list1)





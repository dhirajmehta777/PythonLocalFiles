# # #list under another lists
# # a=[10,20,30,[50,60]]
# # n=len(a)
# # for i in range(n):
# #     if type(a[i]) is list:
# #         if len(a[i])>1:
# #             m=len(a[i])
# #             for j in range(m):
# #                 print(i,j, a[i][j])
# #     else:
# #         print(i,a[i])
# #
# # #nested list Ex2:
# b=[[10,20,30],[40,50,60]]
# # #Without index
# # for r in b:
# #     for c in r:
# #         print(c)
# #     print()
# #with index:
# n=len(b)
# for i in range(n):
#     for j in range(len(b[i])):
#         print(i,j,b[i][j])
#     print()
"""
HackerRank Problem on nested list
"""
n=int(input("Enter Size of the nested list:"))
student=[]
grade=[]
for i in range(n):
    name=input("Enter Name of Student:")
    marks=float(input("Enter marks of Student:"))
    student.append([name,marks])
    grade.append(marks)
grade=sorted(set(grade))
m=grade[1]
name=[]
for val in student:
    if m==val[1]:
        name.append(val[0])
name.sort()
for nm in name:
    print(nm)



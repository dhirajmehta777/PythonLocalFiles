#Approach1:
# n=5
# print("* "*n)#* * * * *
#
# #Approach2:
# k=5
# for i in range(k):
#     print('*',end=' ')#* * * * *

#Square Pattern
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


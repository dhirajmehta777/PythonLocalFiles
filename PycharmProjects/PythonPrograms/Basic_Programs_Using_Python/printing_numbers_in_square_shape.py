num=int(input("Enter number of rows:"))
n_list=[[0 for x in range(num)] for y in range(num)]
#print(n_list)
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()
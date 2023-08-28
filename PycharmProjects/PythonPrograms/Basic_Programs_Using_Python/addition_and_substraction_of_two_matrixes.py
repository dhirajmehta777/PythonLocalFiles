#we can perform addition and substraction only when the no of cols and no of rows are same
row=int(input("enter the row number:"))
col=int(input("enter the col number:"))

print("enter the elements for matrix1:")
matrix1=[[int(input()) for i in range(col)] for j in range(row)]
print("matrix1:")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end="")
    print()

print("enter the elements for matrix2:")
matrix2=[[int(input()) for i in range(col)] for j in range(row)]
print("matrix2:")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end="")
    print()

result=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j]=matrix1[i][j]+matrix2[i][j]

print("result is:")
for i in range(row):
    for j in range(col):
        print(format(result[i][j],"<3"),end="")
    print()
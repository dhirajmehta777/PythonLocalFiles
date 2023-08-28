num=int(input("Enter the number of rows:"))
n=1
for i in range(num):
    for j in range(i+1):
        #print(n,end="")
        #print(n, end=" ")
        print(format(n,"<4"), end="")
        n=n+1
    print()

num=int(input("Enter the number of rows:"))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(format(" ","<5"),end="")
    for j in range(i,0,-1):
        print(format(j,"<5"),end="")
    for j in range(2,i+1):
        print(format(j,"<5"),end="")
    print()

num=int(input("Enter the number of rows:"))
n=1
for i in range(num):
    for j in range(num-i-1):
        print(format(" ","<3"),end="")
    for j in range(i+1):
        print(format(n,"<6"),end="")
        n=n+1
    print()
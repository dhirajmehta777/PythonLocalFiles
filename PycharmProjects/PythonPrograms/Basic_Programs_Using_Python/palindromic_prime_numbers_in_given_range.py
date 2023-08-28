lower=int(input("enter the lower limit:"))
upper=int(input("enter the upper limit:"))
for num in range(lower, upper+1):
    reverse_str = int(str(num)[::-1])
    if num == reverse_str:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


num=int(input("Enter the number:"))
reverse_str=int(str(num)[::-1])
if num==reverse_str:
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not prime number but it is palindrome")
                break
        else:
            print(num,"is a palindromic prime number")
else:
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                print(num,"is not prime number as well as it uis not palindrome")
                break
        else:
            print(num,"is prime number but not a palindrome")
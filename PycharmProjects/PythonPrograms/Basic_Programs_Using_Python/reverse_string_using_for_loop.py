def reverse(string):
    reversed_str=""
    for i in string:
        reversed_str=i+reversed_str
    print("reversed string is:",reversed_str)

string=input("enter a string:")
print("entered string:",string)
reverse(string)
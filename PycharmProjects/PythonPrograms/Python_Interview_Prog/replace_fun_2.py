str=input('enter string:')
x=input('enter char to replace:')
n=int(input('enter index at which char to be replaced by x:'))
output=""
for index, letter in enumerate(str):
    if index%n==0 and index!=0:
        output=output + x
    else:
        output=output+letter
print(output)

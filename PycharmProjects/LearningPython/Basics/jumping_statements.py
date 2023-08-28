#jumping statements (break & continue)
#break:
for i in range(1,10):
    if i==5:
        break#if we want to jump out from the loop using certain conditions
    print(i)
print("###########################")

#continue:
for i in range(1,10):
    if i==5:
        continue#if we want to skip any specific number from the range then we go for continue
    print(i)
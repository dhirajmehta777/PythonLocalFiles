str=input('enter string:')
words=str.split()
final_lst=[]
for word in words:
    final_lst.append((len(word),word))
print(final_lst)
final_lst.sort()
print(final_lst[-1][1])

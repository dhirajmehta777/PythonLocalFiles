s=input('enter string:')
alphabates=[]
digits=[]
for ch in s:
    if ch.isalpha():
        alphabates.append(ch)
    else:
        digits.append(ch)
print(''.join(sorted(alphabates)+sorted(digits)))
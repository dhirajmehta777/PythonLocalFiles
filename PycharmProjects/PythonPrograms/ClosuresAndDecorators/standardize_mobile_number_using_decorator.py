input_1=int(input())
l=[]
#l=[input() for x in range(input_1)] using list comprehension we can write in one line
for x in range(input_1):
    l.append(input())

def decor(fn):
    def inner(l):
        fn("+91" +" "+ c[-10:-5] +" "+c[-5:] for c in l)
    return inner

@decor
def sort_phone_no(l):
    print(*sorted(l), sep="\n")
sort_phone_no(l)

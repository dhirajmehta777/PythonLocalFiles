def swap_case(s):
    x=""
    for c in s:
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper()
        x+="".join(c)
    return x

if __name__ == '__main__':
    s=input()
    result=swap_case(s)
    print(result)
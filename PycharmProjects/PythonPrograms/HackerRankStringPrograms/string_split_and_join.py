def split_and_join(s):
    a=s.split()
    x="-".join(a)
    return x

if __name__ == '__main__':
    s=input()
    result=split_and_join(s)
    print(result)

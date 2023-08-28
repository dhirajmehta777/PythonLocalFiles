if __name__ == '__main__':
    s = input()
    # print(any([i.isalnum() for i in s]))
    # print(any([i.isalpha() for i in s]))
    # print(any([i.isdigit() for i in s]))
    # print(any([i.islower() for i in s]))
    # print(any([i.isupper() for i in s]))
#######################################OR##################################
    for i in range(len(s)):
        if s[i].isalnum():
            print("True")
            break
        if s[i]==len(s)-1:
            print("False")

    for i in range(len(s)):
        if s[i].isalpha():
            print("True")
            break
        if s[i]==len(s)-1:
            print("False")

    for i in range(len(s)):
        if s[i].isdigit():
            print("True")
            break
        if s[i]==len(s)-1:
            print("False")

    for i in range(len(s)):
        if s[i].islower():
            print("True")
            break
        if s[i]==len(s)-1:
            print("False")

    for i in range(len(s)):
        if s[i].isupper():
            print("True")
            break
        if s[i]==len(s)-1:
            print("False")

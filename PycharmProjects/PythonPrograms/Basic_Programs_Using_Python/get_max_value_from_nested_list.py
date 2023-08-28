list2=[]
def get_max(list1):
    for i in list1:
        if type(i)==list:
            get_max(i)
        else:
            list2.append(i)
    return max(list2)

list1=[7,9,[12,5,[30,15],17],7]
print(get_max(list1))
"""
The above program is to convert the nested list into flat list as we cant apply max function on nested list
"""

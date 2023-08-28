str=input()
check_lst=[item for item in input().split()]
res=dict()
for ele in check_lst:
    if ele in str:
        startindex=str.index(ele)
        res[ele]=[startindex,startindex+len(ele)-1]
print(res)
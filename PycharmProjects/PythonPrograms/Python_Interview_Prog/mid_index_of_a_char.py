str=input('enter string:')
x=input('enter char whose index to be known:')
indices=[]
for index, ele in enumerate(str):
    if(ele==x):
        indices.append(index)
res=indices[len(indices)//2]
print(res)

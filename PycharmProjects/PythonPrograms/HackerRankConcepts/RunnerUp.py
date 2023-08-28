list1=[1,2,6,6,5]
list1.sort()
print(list1)
print(max(list1))
print(list1.index(max(list1)))
RunnerUp=list1[list1.index(max(list1)-1)]
print(RunnerUp)
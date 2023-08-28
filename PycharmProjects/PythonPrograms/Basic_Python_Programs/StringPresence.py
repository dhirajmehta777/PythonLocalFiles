#the find() method finds the first occurance of the specified value
#the find() method returns -1 if the value is not found

str="welcome to python programming"
sub_str="python"
print(str.find(sub_str))

if str.find(sub_str)==-1:
    print("not found...")
else:
    print("found...")
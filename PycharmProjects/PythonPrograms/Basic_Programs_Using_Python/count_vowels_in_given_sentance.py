sentence=input("enter the sentence:")
string=sentence.lower()
count=0
list1=["a","e","i","o","u"]
for char in string:
    if char in list1:
        count=count + 1
print("Total number of vowels in given sentence is:",count)
#Using for loop
# any_list=[1,2,3,4,5]
# new_list = []
# for x in any_list:
#     if x>3:
#         new_list.append(x)
# print(new_list)

#using list comprehensions
any_list=[1,2,3,4,5]
new_list = [x for x in any_list if x>3]
print(new_list)

#Ex2 for list comprehensions:we want to print different combinations
list1=[1,2]
list2=[3,4]
list3=[5,6]
newlist=[(x,y,z) for x in list1 for y in list2 for z in list3]
print(newlist)

#Ex3 for list comprehensions:
student=["Raman","Kisan","Prince","Rakesh","Vinod","Rohit"]
newlist1=[x for x in student if x.startswith("R")]
print(newlist1)

#Ex4 for list comprehensions:
student1=[("Raman",17),("Kisan",20),("Prince",22),("Himanshu",15),("Vinod",16)]
newlist2=[x for (x,y) in student1 if y>18]
print(newlist2)



#Approach1:using for loop
# str="welcome"
# counter = 0
# for i in str:
#     counter=counter + 1
# print(counter)

#Approach2:using while loop and slicing
# str="welcome"
# counter = 0
# while str[counter:]:
#     counter=counter + 1
# print(counter)

#Approach3:using build in function
# str="welcome"
# print(len(str))

#Approach4:using join and count
str="welcome"
randon_str="X"
print((randon_str).join(str))
print((randon_str).join(str).count(randon_str))
print((randon_str).join(str).count(randon_str)+1)
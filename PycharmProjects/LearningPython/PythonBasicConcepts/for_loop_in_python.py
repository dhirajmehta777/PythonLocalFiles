#used to iterate over sequence like list, string, dictionary, string, set or tuple

city="Mumbai"
for x in city:
    print(x)

cities=["pune","mumbai","goa","aayodya"] #for list iterated with for loop
for y in cities:
    print(y)

names=('raj', 'ram', 'prem')#for tuple iterated with for loop
for s in names:
    print(s)

list1=[['India','Delhi'],['Australia','Melbourne'],['USA','NewYork']]##iterated for loop for list within the list
for l in list1:
    print(l)#returns sub lists

list3=[['India','Delhi'],['Australia','Melbourne'],['USA','NewYork']]##iterated for loop for list within the list
for country, city in list3:
    print("country is "+country+" and city is "+city)

list2={'Delhi','Melbourne'}#lists within the set
for c in list2:
    print(c)

my_dictionary=dict(list3)#converts lists into dictionary
print(my_dictionary)
for country,city in my_dictionary.items():#here while iterating dictionary we must use items() funtion else
    #will through error
    print(country,city)
    for f in country:#nested for loop
        print(f)


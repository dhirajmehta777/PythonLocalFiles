n=int(input("Enter total number of students:"))
Student_Mark={}

for i in range(n):
    name=input("Enter name of the student:")
    score1=float(input("Enter Score1 of a student:"))
    score2 = float(input("Enter Score2 of a student"))
    score3 = float(input("Enter Score3 of a student"))
    scores=[]
    scores.append(score1)
    scores.append(score2)
    scores.append(score3)
    Student_Mark[name]=scores
Query_name=input("Enter the name of the student whose percentage need to know:")
sum=0
for i in Student_Mark[Query_name]:
    sum=sum+i
print("{0:.2f}".format(sum/3))
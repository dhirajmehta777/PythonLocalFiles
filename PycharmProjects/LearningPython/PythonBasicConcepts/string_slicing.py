#s[i:j]-slice of s from i to j
#s[i:j:k]-slice of s from i to j with step k
#s[startindex:endindex:step]

s="welcom to python world"
print(s[0])#returns first char
print(s[-1])#returns last char

print(s[0:8]) #excludes last index returns 7 chars
print(s[4:8])
print(s[4:8:1])
print(s[4:15:2])
print(s[0:]) #prints whole string
print(s[0:-1])#prints whole string except last char
print(s[:])#prints whole string
print(s[8:])#it prints from that position till end
print(s[-7:])#it prints from reverse
print(s[-7:-2])
print(s[::-1])#reverse the entire string
x="name, age, city"
print(x.index(','))
print(x[0:x.index(',')])
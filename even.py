#even number checking (example for if condition)
a=20
if a%2==0:
    print("even number")
else:
    print("odd number")


#string concatenation
    
name="kavitha"
name1="rani"
print(name+name1)
print(name+'bs')

#print many times

print(name*2)

#fetching character at specific location

print(name[0])

#built in functions in python..
#1.capitalize():capitalize only the first character of the data

print(name.capitalize())

#2.len(): gives total no. of char present in the string
#3.count: cnt the occurence of substring in the actual string

name2="hii am kavitha from mysore"
print(len(name2))
print(name2.count('i'))

#4.find: returns the 1st occurance of the specified char..

print(name2.find('a'))


#ternary operation:

print("hii") if a<30 else print("hello")

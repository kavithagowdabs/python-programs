data="hello world"
print(data[0:5:2])

#makes a copy
print(data[::])

#reverse
print(data[::-1])

print(data[-1::])

#sets
a={10,20,30,40}
b={10,40,30,50,60}
print(a)
print(b)
print(a-b)
print(a&b)
print(a|b)
print(a^b)

#tuples
data=(20,40)
data1=(10,50)
print(data+data1)

#lists
c=[10,30,50,90,[20,40,[100,200,300]],70,80,50]
print(c)
print(c[0:5])
print(c[4][2][1])

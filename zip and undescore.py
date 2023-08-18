
#zip and underscore
a = "mumbai"
b = "hyd"
c = zip(a,b)
print(list(c))


a="mumbai"
b=1,2,3,4
c=zip(a,b)
print(list(c))


a="mahesh"
b="tushar"
c=1,2,3,4,5,6
d=zip(a,b,c)
print(list(d))

m=1,2,3,4,5,6
s=90,23,56,89
d=zip(m,s)
print(list(d))


e=1,2,3,45,67,77
h="mahesh"
g=zip(e,h)
print(list(g))

mahesh="amar"
vishnu="tushar"
tushar=zip(mahesh,vishnu)
print(list(tushar))

#-underscore

_ = 40*5
print(_)

_a =42-78
print(_a)

_a =45+50-36
print(_a)


a,_,c =[4,8,8]
print(a)
print(_)
print(c)


a = 100_20
print(a)

_ =52,56,85
a=_
print(_)

_ =[5.20,63,85]
a=_
print(_)

# shallow copy

a=[1,2,3,4]
b=a
print(a)
a.append(6)
print(a)


m=[1.1,2.2,3.3,4.4,5.5]
v=m
print(m)
m.append(6.6)
print(m)

t=['mahesh','vishnu','akilesh','tushar']
n=t
print(t)
t.append('saurabh')
print(t)

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tuple=list
list .append([10,11,12])
print(list)

mahi =[[12,78],[14,72],[16,89]]
new=mahi
mahi.append(['mahesh','vishnu'])
print(mahi)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = b
b[0][1] = 'XYZ'
b.append('XYZ')
print(b)

l= [['mahesh','vishnu','tushar'],['avi','manoj','vishal']]
i=l
l[1][0]=[1,12]
l.append([1,2,3])
print(l)

#############


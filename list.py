
str1="mahesh"
str2="mahesh"
if str1 == str2:
    print('string are equal')
else:
   	print('string are not equal')


s1="apple"
s2="mahesh"
if s1==s2:
	print('string are equal')
else:
	print('string are not equal')


a=[1,2,4]
b=[1,2,4]
if a==b:
	print('equal')
else:
	print('not equal')

a=[2,3,4,6]
b=['a','b','c']
if a==b:
	print('are equal')
else:
	print('are not equal')


s1='mahesh'
s2='vishnu'
if s1==s2:
	print('equal')
else:
	print('are not equal')

s1='sona'
s2='sona'
if s1==s2:
	print("string are equal")
else:
	print('string are not equal')

num1=10;
num2=5;
c=num1+num2;
print(c)
if num1 > num2:
	print(num1)
else:
	print(num2)
	

num1=10;
num2=6;
c=num1-num2;
print(c)	

m= {"address": "pune","mobile": 7887494265,"state": "maharashtra"}
for i in m:
	print('keys',[i],'val',m[i])

m.update({'key': 101,'values': 'student of the year'})
print(m.keys())
print(list(m.values()))

a = 30
b = 40
def myfun(x,y=60):
	print("x: ",x)
	print("y: ",y)
myfun(a,b)

a= 2
b= 8
def myfun(b=10,a=52):
	print("b:",b)
	print("a:",a)
myfun(a,b)

a=2+8
b=2-2
def myfun(a,b):
	print("a:",a)
	print("b:",b)

myfun(a,b)
   

a=3
def myfun(a,b=1):
    print("a:",a)
    print("b:",b)
myfun(a,b) 

a=30
b=20
c=40

def test(*args):
	for i in args:
		print(i)
test(a,b,c)

a=2
b=12
c="mahi"
d="sona"
e="satish"
def myfun(*args):
	for i in args:
		print(i)
myfun(a,b,c,d,e)		


a=5-6
b=9
c=3
d=2+8
def myfun(*args):
	for i in args:
		print(i)
myfun(a,b,c,d)		

a=10
b=80
c=90
d={"name":"mahesh"}
def function(*args):
	for i in args:
		print(i)
function(a,b,c,d)

def test(a,v=30):
	print(a+v)
test(5)
test(6,30)

def test(b,m=6):
    print(b+m)
test(8)
test(1,90)

def mahi(c,m=9-4):
	print(c-m)
mahi(8)
mahi(9,65)	

  




b=8
def function():
	for i in range(b,0,-1):
		print('*'*i)
function()

for i in range(5):
	print('*' *i)


n=7
def function():
	for i in range(3,n):
		for j in range(i):
			print(j, end = ' ')
		print()
function()

n=6
def function():
	for i in range(0,n+4):
		for j in range(i):
			print('M  ', end = ' ')
		print()
function()

for i in range(1,8):
	for j in range(i):
		print(i,end='')
	print()

for i in range(0,9):
	for j in range(0,i):
		print(i, end='')
	print()


for i in range(1,6):
	for j in range(0,i):
		print(j, end='') 
	print()


	

for i in range(1,27):
	x=65
	for j in range(0,i):
		print(chr( x ), end='')
		x += 1
	print()

for i in range(1,5+2):
	x=65
	for j in range(i):
		print(chr(x),end='')
		x += 1
	print()


a=4
x=10
for i in range(1,a+1):
	for j in range(i):
		print(chr(x), end='')
		x += 1
	print()

a=7
x=97
for i in range(1,a+1):
	for j in range(i):
		print(chr(x), end='')
	x += 1
	print()

a=7
x=97
for i in range(7,0,2):
	for j in range(i):
		print(chr(x), end='')
	x += 1
	print()


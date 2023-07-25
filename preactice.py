s = "Mahesh"
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
print(reverse(s))

 
n = 1234
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)


s = "mahesh" 
s1 = ""
for i in s:
    s1 = i + s1
if (s == s1):
    print("String is palindrome")
else:
    print("String is not palindrome")


a=[1,2,3,4,5,6,7,8,9,10]
a.sort(reverse=True)
print(a)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(1, 20):
    if is_prime(n):
        print(n)

m = {"address": "pune", "mobile": 7887494265,"adhar":389810987580,"state": "Maharashtra"}
for i in m:
	print('keys',[i],'val',m[i])
m.update({'key': 101,'values':'student of the year'})
print(m.keys())
print(list(m.values()))	



mahesh_dict = {'Mahesh': 1, 'vishnu': 2, 'tushar': 3, 'akhilesh': 4,'manoj':5}

for key in mahesh_dict.keys():
    print(key)


mahesh_dict ={'Mahesh': 1, 'vishnu': 2, 'tushar': 3, 'akhilesh': 4,'manoj':5}
for value in mahesh_dict.values():
    print(value)

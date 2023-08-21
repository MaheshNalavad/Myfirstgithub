class Company():
    company_name = 'Expert IT Data Informatics LLP'     
    def my_company_name(self):
        print(self.company_name)

class CompanyAddress():
    companyaddress = 'Pune'     
    def my_companyaddress(self):
    	print(self.companyaddress)

class AnnuelSalary():
    my_annuelsalary = 400000
    def annuelsalary(self):
        print(self.my_annuelsalary)
       
class Role():
    role_name='Devolper'
    def Role(self):   
        print(self.role_name)

class JoinDate():
    my_joindate = 2022
    def my_joindate(self):
        print(self.my_joindate)

class EmployeeName():
    my_employeename = 'Mahesh Nalavade'
    def employeename_is(self):
        print(self.my_employeename)      

class Employee(Company,CompanyAddress,JoinDate,AnnuelSalary, Role, EmployeeName,):
    def employee_Details(self):
        print(self.my_employeename)

Obj = Employee()
Obj.employee_Details()
Obj.my_company_name()
Obj.my_companyaddress()
Obj.Role()
Obj.annuelsalary()

#Reverse the list program

list = [1,2,3,4,5]
list1= list[::-1]
print(list1)

s="madam"
s1=""
for i in s:
    s1=i+s1
if(s==s1):
    print("string is palindrome")
else:
    print("string is not a palindrome") 

num=10
if (num%2==0):
    print("even")
else:
    print("odd")     
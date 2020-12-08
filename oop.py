import datetime

class Employee:
    
    num_of_employee=0
    raise_amount=1.04 
    
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.email=fname+'.'+lname+'@gmail.com'
        Employee.num_of_employee +=1


    def fullname(self):
        return ('{} {}'.format(self.fname,self.lname))
    def apply_raise(self):
        self.salary=int(self.salary* self.raise_amount) 


    #class method
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount  
    @classmethod
    def from_string(cls,emp_str):
        fname, lname, salary=emp_str.split('-') 
        return cls(fname,lname,salary)  

    #staticmethod 
    @staticmethod
    def is_workday(day):
        if day.weekday==5 or day.weekday==6:
            return False
        return True
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.fname,self.lname,self.salary) 
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email) 
    def __add__(self,other):
        return self.salary+other.salary    
    def __len__(self):
        return len(self.fullname())                        

emp_1=Employee('likhitha','pichika',50000)
emp_2=Employee('sravani','puchala',55000)


#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))

#the above stmt is similar to print(emp_1.__repr__())
#                             print(emp_1.__str__()) bcoz the both print same output

#print(emp_1.email)
#print(emp_2.salary)

#print('{} {}'.format(emp_1.fname,emp_1.lname))
#print(emp_1.fullname())
#emp_1.fullname()
#print(Employee.fullname(emp_1))


#emp_1.raise_amount=1.05


#Employee.set_raise_amount(1.05)

#emp_1.set_raise_amount(1.05)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)


#print(Employee.num_of_employee)


emp_str_1='shivani-munipally-60000'
emp_str_2='keerthana-srm-65000'
emp_str_3='pravanya-penumudi-70000'

#fname,lname,salary= emp_str_1.split('-')
#new_emp_1=Employee(fname,lname,salary)

#new_emp_1=Employee.from_string(emp_str_1)

#print(new_emp_1.email)
#print(new_emp_1.salary)


#my_date=datetime.date(2020,12,5)
#print(Employee.is_workday(my_date))

#inheritance
class Developer(Employee):
    raise_amount=1.10

    def __init__(self,fname,lname,salary,prog_lang):
        super().__init__(fname,lname,salary)
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self,fname,lname,salary,employees=None):
        super().__init__(fname,lname,salary)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())                                   


dev_1=Developer('saran','vajjiparthi',60000,'python')
dev_2=Developer('gopi','ravuri',65000,'java')

#print(dev_1.email)
#print(dev_2.email)

#print(help(Developer))

#print(dev_1.salary)
#dev_1.apply_raise()
#print(dev_1.salary)

#print(dev_1.email)
#print(dev_1.prog_lang)


mgr_1=Manager('koushik','jkshdg','90000',[dev_1])

#mgr_1.add_emp(dev_2)
#mgr_1.rem_emp(dev_1)

#print(mgr_1.email)
#mgr_1.print_emp()

#print(isinstance(mgr_1,Manager))
#print(issubclass(Developer,Employee))


#print(2+3)
#print(int.__add__(2,3))
#print(str.__add__('a','b'))

#print(emp_1+emp_2)

#print(len('test'))
#print('test'.__len__())
print(len(emp_1))
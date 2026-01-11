"""str = "aBCDefg#.,"
a = 0
b = 0
l = []
for i in str:
    if i.isupper():
        a += 1   #the count of upper case letters
    elif i.islower():
        b += 1   #the count of lower case letters 
    else:
        l.append(i)  # the list of remaining chars
print(a)
print(b)
print(l)"""

"""d ={}
str = input("enter the word:")  # input the value to the user
for i in str:  #loops the input value from the user 
    if i in d :# checks whether if i is present in dict d
        d[i] += 1   #condition fails here cuz d is empty
    else:
        d[i] = 1 # the first letter of the word gets the value 1 
print(d)"""

"""Write a program to find the second largest element in a list.

Write a program to remove duplicates from a list.

Write a program to count occurrences of each element in a list using a dictionary.

Write a program to convert two lists into a dictionary (one as keys, one as values).

Given a dictionary, find the key with the maximum value.

Write a program to merge two dictionaries into one.

Write a program to sort a list of tuples based on the second element."""
        
 # Write a program to count occurrences of each element in a list using a dictionary
 
"""a = [2,4,5,6,2,3,2,5,6,7,7,7,2,5]
d ={}
for i in a:
    d[i]=d.get(i,0)+1
    
    
print(d)"""
     
   # a.index(i)
"""lvowels = ['a','e','i','o','u']
def vowels():
    str ="tree"
    for i in str:
        if i in lvowels:
            print(i)
vowels()"""

"""def calc(a,b):
    return a+b, a-b     


x,y =calc(5,3)  
print(x)
print(y)"""

#function returns product of all num 



 
"""def multiply_all(*num):
    result = 1
    for i in num:
        result *= i
    return result

res = multiply_all(1, 2, 3)
print(res)  """

  
#greet all

"""def greet_all(*num):
    for i in num:
        g= print(f'Hello! {i}')
    #g=print(f'Hello! {num[0]},{num[1]}')
    return g
greet =greet_all('alex','alexa')   
print(greet) """

#1. Function to print your name 5 times	

"""def printfive(a):
    for i in range(1,6):
        print(a)
    
printfive("Ashik")  """  

#2. Function that takes a number and prints whether it’s even or odd	
"""def Oddoreven(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")
Oddoreven(5) """       

#3. Function that returns the square of a number
"""def squNum(a):	
    if a != 0:
        a**=2
        print(a)
        return a
squNum(2)"""
#4. Function that returns factorial of a number 
"""def factorial(a):
    if a ==0 and a ==1:
        return 1
    else:
        num = n* factorial(n-1)"""
        

"""sq = lambda a : a**3
print(sq(5))  """  


"""sq = lambda a : "even" if a %2 ==0 else "odd"
print(sq(6))"""  

"""lrg = lambda a,b : f'{ a}is greatest' if a>b else f'{ b } is greatest'
print(lrg(7,8))  """
#map    
                                             
"""lst = [5,8,3,2]
m = list(map(lambda a :a ** 2,lst))
print(m)"""

#filter

"""lst = [2,3,6,9,5]   
f =tuple(filter(lambda a:a% 2==0,lst) )
print(f)"""

#reduce

"""from functools import reduce
lst = [2,4,6,8]
r = reduce(lambda a,b:a+b,lst)
print(r)"""

#cube using lambda
"""c = lambda a :a ** 3
print(c(5))"""
#sort
#pairs =[(1,2),(4,1)(9,0)]
"""a = 10
print(type(a))"""


"""class car:
    pass
car1= car()
print(id(car1))     
car2= car()
print(id(car2))  
car2 = car1
print(type(car2)) """

#class
"""class car:
    def __init__(self,colour,brand):
         self.colour = colour
         self.brand = brand
    def brake (self):
        print(f'the {self.brand} car of colour {self.colour} is applied brake')
        
c1 =car("black","bmw")
c1.brake()"""

#amstrong 

"""num = int(input("enter the number:"))
for num in range(1,1001):
    temp = num
    powerS = len(int(num))
    if num >0:
        digit = num % 10"""
        
        
#Create a class Student with attributes: name, marks


#Add a method display() to print the details

#Create 2–3 student objects

#Call the display() method for each


"""class Student():
   
    
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
        
    
    
    def display(self):
        print(f"{self.name} scored {self.marks} marks")
            
s1= Student("Raju","80")   
s1.display() 
s1= Student("Bheem","90")   
s1.display() 
s1= Student("jaggu","100")   
s1.display() """



"""  
  
class bank():
    def __init__(self,balance):
        self.balance =balance
        
       
            
             
            
            
    
    
    def add(self,new_amount):
        self.balance +=new_amount 
        print(f"new amount:{self.balance}")
    
    def withdraw(self,new_amount):
        self.balance -= new_amount
        print(f"new amount:{self.balance}")
        
balance = int(input("amount: "))        
new_amount = int(input("amount: "))
option = input("withdraw/deposit") 

w = bank(balance)
if option == "withdraw" :
    w.add(new_amount)
elif option =="deposit" :
    w.withdraw(new_amount)"""
 
"""b = 38   
for i in range(27,39):
    if i <= b:
        c = i % 2
        if c == 0:
            print(i)"""

#car1.brand = "Audi"
"""class car:
    wheel = 4
    side_mirrors =2
    def __init__(self,colour,brand):
         self.colour = colour
         self.brand = brand
    def brake (self):
        print(f'the {self.brand} car of colour {self.colour} is applied brake')
        
c1 =car("black","bmw")
c1.brake()
c2 = car("yellow","volkswagen")
c2.brake()
w = car.wheel
print(w)
sm = car.side_mirrors
print(sm)
yc = c2.colour
print(yc)"""


#lets imagine youre programming for a factory that has multiple machines all machines run under a common voltage
# but each machine has  machine id and production count  220 v
        
"""class Machines:
    
    common_voltage = 230
    def __init__(self, id ):
        self.id = id
        self.product_count = 0
    def production(self ):
        self.product_count+=1
        print(f"new production count of m_id: {self.id}  is {self.product_count}")
        
m1= Machines(110)

m1.production()
m1.production()
m1.production()"""

#print from 10 to 1 
"""i = 11 
while i != 1:
    i -= 1
    print(i)"""
        
#factorial using while loop

#i = 6
"""while i != 0 or i != 1:
    
    n=i*(i-1)
    print(n)
    break"""
    
# f =1
# for i in range (1,7):
    
#     f *=i
    

# 6!=6*5*4*3*2*1
"""a = int(input("enter the num: "))   
f = 1
while a >0:
    f *= a 
    a=a-1     
print(f) """ 
      
# count digit of a number using while loop
"""num = 2345
while num > 1:
    nums = str(num)
    print(len(nums))
    break"""
#create a rectangle class to compute area and perimeter

"""class Rectangle:
    
    def __init__(self,a,b):
        self.a = a
        self.b= b
    def area(self):
        ar = self.a *self.b
        print(F'the area of the rectangle : {ar}')
    def perimeter(self):
        pr = 2*self.a+self.b
        print(f'the perimeter of the rectangle : {pr}')
R1=Rectangle(5,7)        
R1.area()
R1.perimeter()"""
#single
"""class Employee:
    def __init__(self,id ,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def Display(self):
        print(f'Name: {self.name} Salary:{self.salary} Id : {self.id}')
        
class Manager(Employee):
    def assigning():
        print("manager is assigning the work")        
    
e1 = Manager(101824,"Ashik",999999) 
e1.Display()"""

#1. Create a class Student with attributes: name, age, and grade.
#Add a method update_grade(new_grade) that updates the student’s grade.
#Create an object and test updating the grade?

"""class Student:
    def __init__(self,name,age,grade):
        self.name =name
        self.age = age
        self.grade =grade
        
    def update_grade(self,new_grade):
            self.grade = new_grade
            print(self.grade)
            
obj = Student("Ashik",24,"B")
obj.update_grade("A") """           
    

#2.Demonstrate inheritance using Teacher → MathTeacher.
"""class Employee:
    def __init__(self,id ,name,salary):
        self.id = id
        self.name = name
        self.salary = salary
    def Display(self):
        print(f'Name: {self.name} Salary:{self.salary} Id : {self.id}')
        
class Manager(Employee):
    def assigning():
        print("manager is assigning the work")        
    
e1 = Manager(101824,"Ashik",999999) 
e1.Display()"""
    
#3.Write a Python program to implement single inheritance with a base class Vehicle and a subclass Car.
"""class vehicle:
    def __init__(self, colour):
        self.colour = colour
    def display(self):
        print(f'the inherited colour is {self.colour}')
        
class Car(vehicle):
   pass
obj = Car("black")
obj.display()"""
                

#4.Create a multilevel inheritance example for a company hierarchy: Company → Department → Employee.
"""class Company():
    def __init__(self, Name,location):
        self.Name = Name
        self.location = location
    def display1(self):
       print(F'Company: {self.Name},{self.location}')
        
class Department(Company):
   
    def display2(self):
        print(F'Department: {self.Name},{self.location}')
class Employee(Department,Company):
    pass

obj = Employee("Ashik","Earth")

obj.display1()
obj.display2()"""

#5.Implement hierarchical inheritance for Account, SavingsAccount, and CurrentAccount.
"""class Account :
    def __init__(self,Account_name,main_balance,min_balance):
        self.acc =Account_name
        self.maxb = main_balance
        self.minb = min_balance
    def displayDetails(self):
        print(f'{self.acc} max :{self.maxb} min : {self.minb}')
class Savings(Account) :
    pass
class Current(Account):
    pass
obj = Savings("123344","10000","100")
obj.displayDetails()   
obj2 = Current("123384","10000","0")
obj2.displayDetails()  """


"""class Maths:
    def addd(self,*args):
        return sum(args)
    
math1 = Maths()
obj1 = math1.addd(1,2,3)
print(obj1)"""
    
    

from abc import ABC,abstractmethod
class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
        
class Car(Vehicle):
    def start_engine(selfie):
        print("the engine is starting")
    def stop_engine(selfie):
        print("the engine stops")
    
obj1=Car().start_engine()




   
        
        

    
    
    





          
        
"""Define a class named Car that has the following attributes: make, model, and year.
 Create a constructor that initializes these attributes when a new Car object is created.
 
 
 2. Create a class Car with attributes: brand, model, and year.Use a constructor to initialize
 these values. Create an object and print the details.
 
 
 3. Create a class Rectangle with attributes: length and width. Write a method area() to calculate
 the area. Write another method perimeter() to calculate the perimeter. Test with sample
 objects.
 
 
 4.Create a class Student with attributes: name, age, and grade. Add a method up
date_grade(new_grade) that updates the student’s grade. Create an object and test updating
 the grade.
 
 5.Create a class BankAccount with attributes: account_number, holder_name, and balance Con
structor should initialize balance as 0. Add methods: deposit(amount) → increases balance with
draw(amount) → decreases balance if sufficient display() → shows account details"""

#1

"""class Car:
    def __init__(self,make, model,year):
        self.make = make
        self.model = model
        self.year = year"""
#2

"""class Car:
    def __init__(self,brand, model,year):
        self.b = brand
        self.model = model
        self.year = year
obj=Car("ford","mustang","1988")
print(obj.b)
print(obj.model)
print(obj.year)"""

# 3.Create a class Rectangle with attributes: length and width.
# Write a method area() to calculatethe area. Write another method perimeter() to calculate the perimeter.
# Test with sampleobjects.

"""class Rectangle:
    def __init__(i,length,width):
        i.l = length
        i.w= width
    def area(i):
        area = i.l* i.w
        print(area)
    def perimeter(i):
        perimeter = 2* i.l+ i.w
        print(perimeter)
obj1 = Rectangle(5,7).perimeter()
obj2 = Rectangle(5,7).area()"""

#4.Create a class Student with attributes: name, age, and grade. Add a method up
#date_grade(new_grade) that updates the student’s grade. Create an object and test updating
#the grade.

"""class Student:
    
    def __init__(s,name,age,grade):
        s.name = name
        s.age = age
        s.grade = grade
    def update_grade(s,new_grade):
        s.grade = new_grade
        print(s.grade)
obj = Student("Ashik",24,"O")
obj1= obj.update_grade("B+") """

#5.Create a class BankAccount with attributes: account_number, holder_name, and balance Con
#structor should initialize balance as 0. Add methods: deposit(amount) → increases balance with
#draw(amount) → decreases balance if sufficient display() → shows account details"""

       
for i in range(1,11):
    print(i)      
    
        
        
        
        
        
    
            
        
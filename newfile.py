
#Arithmatic operators

"""a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000"""

#membership operators

"""fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # True
print("grape" not in fruits) # True"""

#comparison

"""x = 5
y = 3
print(x > y)  # True
print(x == y) # False
print(x != y) # True"""

#logical

"""a = 5
b = 10
print(a > 2 and b < 20) # True
print(a > 8 or b < 20)  # True
print(not(a > 2))       # False"""

#identity 

"""x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)     # True
print(x is z)     # False
print(x == z)     # True (values same, objects different)"""


"""score=99

if score >=50 and score <90 :
    print("Good marks")
    
elif score >= 90 and score <=100:
    print("Excellent")
    
elif score <50 :
    print("Try again")
    
else:
    print("Invalid marks")"""
    
    
    #questions
    
"""  1. Even or Odd
Write a program to check whether a given number is even or odd.


2. Positive, Negative, or Zero
Take an integer input and display whether it is positive, negative, or zero.


3. Greatest of Three Numbers
Write a program to find the largest among three numbers using conditional statements.


4. Leap Year Check
Ask the user to enter a year and check whether it is a leap year or not.
(Hint: A year is leap if divisible by 4 but not by 100, or divisible by 400.)


5. Grading System
Input a student’s marks and print the grade:

90–100 → A

80–89 → B

70–79 → C

60–69 → D

Below 60 → Fail



6. Vowel or Consonant
Take a character input and check whether it is a vowel or a consonant.


7. Eligibility to Vote
Ask the user for their age. If age ≥ 18 → "Eligible to vote", else → "Not eligible".


8. Password Check
Store a password in the program. Ask the user to enter a password.

If correct → "Access Granted"

Else → "Access Denied"



9. Day of the Week
Take a number (1–7) from the user and print the corresponding day of the week.
(1 = Monday, 7 = Sunday)


10. Discount Calculator
Ask the user to enter the purchase amount.



If amount > 5000 → 20% discount

If 2000–5000 → 10% discount

Else → No discount"""
    
   # Write a program to check whether a given number is even or odd.
   
"""a= int(input("Enter the number:"))

m = a%2

if a%2 == 0:
    print("the number is even")
else:
    print("the number is odd")"""
    
    #Positive, Negative, or Zero
    
"""a=int(input("Enter the number:"))

if a == 0:
    print("Zero")
elif a > 0 :
    print("positive")
elif a < 0 :
    print("Negative")"""
    
#Greatest of Three Numbers
#Write a program to find the largest among three numbers using conditional statements.

"""a= int(input("enter number a:"))
b= int(input("enter number b:"))  
c= int(input("enter number c:"))

if a >= b and  a >= c:   
    print("a is greatest")
    
elif b >= a and b >= c :
     print("b is greatest")

else :
    print("c is greatest")"""


    
#Ask the user to enter a year and check whether it is a leap year or not.
#(Hint: A year is leap if divisible by 4 but not by 100, or divisible by 400.)

"""a= int(input("Enter the year:"))
if a % 4 != 0 :
    print("the year is not leap")
if a % 4 == 0 :
    s = a % 100
    if s != 0 :
        print("the year is leap")
        
    elif s == 0 :
        sn = a % 400
        if sn == 0 :
            print("the year is leap")
        else:
            print("the year is not leap")"""


    
#    Input a student’s marks and print the grade:

#90–100 → A

#80–89 → B

#70–79 → C

#60–69 → D

#Below 60 → Fail
 
"""a= int(input("enter the number:"))
if a <60 :
    print("Fail")
elif a>=60 and a<70:
    print("D grade")   
elif a>=70 and a<80:
    print("C grade")
elif a>=80 and a<90:
    print("B grade")
elif a>=90 and a<=100:
    print("A grade")"""
    
# Take a character input and check whether it is a vowel or a consonant.

"""a = str(input("enter the text:"))
v = ["a","e","i","o","u"]
if a in v:
    print("vowel")
else:
    print("consonent")"""

#Store a password in the program. Ask the user to enter a password.

"""pwd = "password"
a= str(input("enter the password:"))
if a == pwd :
    print("Access Granted")
else:
    print("Access Denied")"""
    
#Take a number (1–7) from the user and print the corresponding day of the week.
#(1 = Monday, 7 = Sunday)
 
"""a= int(input("enter the number :"))
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
if a in days:
    d = days[a]
    print(d)"""

# Ask the user to enter the purchase amount.
#If amount > 5000 → 20% discount
#If 2000–5000 → 10% discount
 
"""a= int(input("enter the number:"))
if a > 5000 :
    print("20 percent discount")
elif a>=2000 and a<= 5000:
    print("10 percent discount")
else:
 print("invalid amount")"""
#output should be 14

"""m=0
a =[2,3,4,5]     
for i  in a:
     m += i
    
print(m)"""

#for loop

"""a= int(input("enter the number:"))
m = []
for i in range (1,a+1):
    if i % 2 == 0:
        m.append(i)
        print("even:",i)"""
        
"""a = str(input("text:"))
str =""
for i in a :
    str = i + str
print(str)
print(a)  """ 


"""n = 6
for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()"""
"""q"""
    
"""for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()"""
    
"""for i in range(1,5):
    for j in range(i):
        print(chr(64+i),end="")
    print()"""

"""for i in range(0,10,+2):
   # print(" ",end="")
    for j in range(1,i,+1):
        print("*",end="")
        
    print()"""
     
   
        
   
    
"""for i in range(1,5):
    for j in range(1,i+1):
        
        print(chr(64+j),end="")
    print()"""


  


   
        
    
        
  
  
  
        
   
   
    
   
    
    
    

    

    
 
    
    
    
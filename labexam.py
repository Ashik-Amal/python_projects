
#largest and smallest
a= int(input("enter number a,"))
b= int(input("enter number b,"))  
c= int(input("enter number c,"))
if a > b >= c :
    print("a is greatest")
if b > a >= c :
     print("b is greatest")
if c > a >= b :
    print("c is greatest")
if a < b <= c :
    print("a is smallest")
if b < a <= c :
     print("b is smallest")
if c < a <= b :
    print("c is smallest")
elif a==b==c :
    print("three values are same ")
    
 #vowels and consonents
 
a = str(input("enter the text:"))   
v = 0
vowels = ["a","e","i","o","u"]
for i in a :
    if i in vowels:
        v += 1

print("num of vowels:",v)
s = len(a)-v
print("num of consonents",s)

#Algorithm

"""s1: enter the input a 
s2: initialize a variable v and store vowels inside a list
s3: use for loop to iterate through the string .. if a = apple ,the loop iterates as i = a,i= p ...and the if condition 
 inside the loop is used to check whether the any letters in the string "a"  is present inside the list "vowels".if the
 if yes,the count of variable v start increasing by 1 
 s4:  the  vowel  count is printed 
 s5: the count of the consonent is calculated by subtracting the total length of the string "a" with the count of variable v
 """







    
    
    
     
    
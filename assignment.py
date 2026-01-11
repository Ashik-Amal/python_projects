# 1. Number is multiple of both 3 and 7
"""
a = int(input("Enter the number:"))
if a % 7 == 0 and a % 3 == 0:
    print("Multiple of 3 and 7")
else:
    print("No")
"""


# 2. Write a program to check whether a given character is a digit or not
"""
a = input("Enter the character:")
if a.isdigit():
    print("Digit")
else:
    print("Not a digit")
"""


# 3. Write a program to check if a number lies between 100 and 500
"""
a = int(input("Enter the number:"))
if a > 100 and a < 500:
    print("Number lies between 100 and 500")
else:
    print("No")
"""


# 4. Write a program to print 'Pass' if marks are greater than or equal to 40, otherwise print 'Fail'.
"""
a = int(input("Enter the marks:"))
if a >= 40 and a <= 100:
    print("Pass")
else:
    print("Fail")
"""


# 5. Write a program to compare two strings and print whether they are equal or not
"""
a = input("Enter the first string:")
b = input("Enter the second string:")
if a == b:
    print("Equal")
else:
    print("Not equal")
"""


# 6. Write a program to check whether a character is uppercase, lowercase, or a special symbol.
"""
a = input("Enter the character:")
if a.isupper():
    print("Upper case")
elif a.islower():
    print("Lower case")
else:
    print("Special character")
"""


# 7. Write a program to check if a given number is a perfect square.
"""
a = int(input("Enter number:"))
if a != 0:
    sq = a ** 0.5
    if sq * sq == a:
        print("Perfect Square")
    else:
        print("No")
"""


# 8. Write a program to find the smallest of four numbers using nested if-else.
"""
a = 12
b = 3
c = 4
d = 5
if a < b:
    if a < c:
        if a < d:
            print("a is smallest")
        else:
            print("d is smallest")
else:
    if b < a:
        if b < d:
            if b < c:
                print("b is smallest")
            else:
                print("c is smallest")
"""


# 9. Write a program to determine whether a person is a child, teenager, adult, or senior citizen based on age.
"""
a = int(input("Enter age:"))
if a >= 60:
    print("Senior Citizen")
elif a >= 20:
    print("Adult")
elif a >= 13:
    print("Teenager")
else:
    print("Child")
"""


# 10. Write a program to determine if three sides can form an equilateral, isosceles, or scalene triangle.
"""
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
"""


# 11. Write a program to print the first 20 multiples of 7.
"""
for i in range(1, 21):
    print(i * 7)
"""


# 12. Write a program to find the sum of even numbers between 1 and 100.
"""
sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers between 1 and 100:", sum_even)
"""


# 13. Write a program to print all numbers divisible by 9 between 1 and 200.
"""
for i in range(1, 201):
    if i % 9 == 0:
        print(i)
"""


# 14. Write a program to display all prime numbers between 50 and 150.
"""
for i in range(50, 151):
    if i <= 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
"""


# 15. Write a program to find the reverse of a given integer.
"""
num = 3456
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10
print("Reversed number:", rev)
"""


# 16. Write a program to print the sum of the digits of all numbers from 1 to 50.
"""
total_sum = 0
for num in range(1, 51):
    temp = num
    while temp > 0:
        digit = temp % 10
        total_sum += digit
        temp //= 10
print("Sum of digits from 1 to 50:", total_sum)
"""


# 17. Write a program to find and print all Armstrong numbers between 1 and 1000.
"""
print("Armstrong numbers between 1 and 1000 are:")
for num in range(1, 1001):
    temp = num
    digits = len(str(num))
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    if num == sum_of_powers:
        print(num, end=' ')
"""


# 18. Write a program to count and print the number of even and odd digits in an integer.
"""
num = int(input("Enter an integer: "))
even_count = 0
odd_count = 0
temp = num
while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    temp //= 10
print("Even digits:", even_count)
print("Odd digits:", odd_count)
"""


# 19. Write a program to print the pattern of stars in a right triangle using nested loops.
"""
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=' ')
    print()
"""


# 20. Write a program to print the multiplication tables from 1 to 10.
"""
for i in range(1, 11):
    print(f"\nMultiplication Table for {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
"""


# 21. Write a program to display all numbers whose cube is less than 1000.
"""
for i in range(1, 1000):
    if i ** 3 < 1000:
        print(i)
    else:
        break
"""


# 22. Write a program to print all numbers between 1 and 500 that are divisible by both 5 and 7.
"""
for i in range(1, 501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
"""


# 23. Write a program to find the sum of squares of the first n natural numbers.
"""
n = int(input("Enter n: "))
sum_squares = sum(i ** 2 for i in range(1, n + 1))
print("Sum of squares:", sum_squares)
"""


# 24. Write a program to calculate the product of all odd numbers between 1 and 15.
"""
product = 1
for i in range(1, 16, 2):
    product *= i
print("Product:", product)
"""


# 25. Write a program to print the Fibonacci series using a while loop.
"""
n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()
"""


# 26. Write a program to check if a string contains only alphabets.
"""
s = input("Enter a string: ")
print("Contains only alphabets:", s.isalpha())
"""


# 27. Write a program to remove all digits from a given string.
"""
s = input("Enter a string: ")
result = ''.join(ch for ch in s if not ch.isdigit())
print("String without digits:", result)
"""


# 28. Write a program to count uppercase, lowercase, digits, and special characters in a string.
"""
s = input("Enter a string: ")
upper = lower = digit = special = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print(f"Uppercase: {upper}, Lowercase: {lower}, Digits: {digit}, Special: {special}")
"""


# 29. Write a program to find the number of occurrences of each vowel in a string.
"""
s = input("Enter a string: ").lower()
vowels = "aeiou"
for v in vowels:
    print(f"{v}: {s.count(v)}")
"""


# 30. Write a program to remove all spaces and count the total number of characters.
"""
s = input("Enter a string: ")
no_space = s.replace(" ", "")
print("Without spaces:", no_space)
print("Character count:", len(no_space))
"""


# 31. Write a program to check if two strings are anagrams of each other.
"""
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagrams:", sorted(s1) == sorted(s2))
"""


# 32. Write a program to capitalize the first letter of every word in a string.
"""
s = input("Enter a string: ")
print(s.title())
"""


# 33. Write a program to remove duplicate characters from a string.
"""
s = input("Enter a string: ")
result = ''.join(sorted(set(s), key=s.index))
print("Without duplicates:", result)
"""


# 34. Write a program to count how many times a substring appears in a string.
"""
s = input("Enter a string: ")
sub = input("Enter substring: ")
print("Occurrences:", s.count(sub))
"""


# 35. Write a program to reverse each word in a sentence individually.
"""
s = input("Enter a sentence: ")
print(' '.join(word[::-1] for word in s.split()))
"""


# 36. Write a program to find the product of all elements in a list.
"""
lst = [2, 3, 4, 5]
product = 1
for i in lst:
    product *= i
print("Product:", product)
"""


# 37. Write a program to separate positive and negative numbers from a list.
"""
lst = [10, -5, 3, -2, 8, -9]
pos = [i for i in lst if i >= 0]
neg = [i for i in lst if i < 0]
print("Positive:", pos)
print("Negative:", neg)
"""


# 38. Write a program to count the number of even and odd numbers in a list.
"""
lst = [1, 2, 3, 4, 5, 6]
even = len([i for i in lst if i % 2 == 0])
odd = len(lst) - even
print("Even:", even, "Odd:", odd)
"""


# 39. Write a program to find common elements in two lists.
"""
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = list(set(a) & set(b))
print("Common elements:", common)
"""


# 40. Write a program to remove all zero elements from a list.
"""
lst = [0, 1, 2, 0, 3, 0, 4]
lst = [i for i in lst if i != 0]
print(lst)
"""


# 41. Write a program to find the second smallest element in a list.
"""
lst = [4, 1, 7, 3, 2]
lst.sort()
print("Second smallest:", lst[1])
"""


# 42. Write a program to print all elements of a list in reverse order using slicing.
"""
lst = [1, 2, 3, 4, 5]
print(lst[::-1])
"""


# 43. Write a program to square every element in a list.
"""
lst = [1, 2, 3, 4, 5]
squared = [i ** 2 for i in lst]
print(squared)
"""


# 44. Write a program to find the difference between the maximum and minimum element in a list.
"""
lst = [10, 3, 7, 1, 9]
print("Difference:", max(lst) - min(lst))
"""


# 45. Write a program to check if two lists are identical or not.
"""
a = [1, 2, 3]
b = [1, 2, 3]
print("Identical:", a == b)
"""


# 46. Write a program to count how many times a specific value appears in a tuple.
"""
t = (1, 2, 3, 2, 4, 2)
x = int(input("Enter value: "))
print("Count:", t.count(x))
"""


# 47. Write a program to find the largest and smallest elements in a tuple.
"""
t = (4, 7, 1, 9, 2)
print("Largest:", max(t))
print("Smallest:", min(t))
"""


# 48. Write a program to check if an element exists in a tuple.
"""
t = (1, 2, 3, 4, 5)
x = int(input("Enter element: "))
print("Exists:", x in t)
"""


# 49. Write a program to swap the keys and values in a dictionary.
"""
d = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in d.items()}
print(swapped)
"""


# 50. Write a program to create a dictionary from two lists: one of keys and one of values.
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)
"""


# 51. Write a program to find the total number of items in a dictionary.
"""
d = {'a': 1, 'b': 2, 'c': 3}
print("Total items:", len(d))
"""


# 52. Write a program to print all keys in a dictionary that have values greater than 50.
"""
d = {'x': 45, 'y': 60, 'z': 75}
for k, v in d.items():
    if v > 50:
        print(k)
"""


# 53. Write a program to sort a dictionary by its values.
"""
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)
"""


# 54. Write a program to update a dictionary element using a key if it exists, else add a new key.
"""
d = {'a': 1, 'b': 2}
key = input("Enter key: ")
value = int(input("Enter value: "))
d[key] = value
print(d)
"""


# 55. Write a program to find the symmetric difference between two sets.
"""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Symmetric difference:", a ^ b)
"""


# 56. Write a program to check if a set is a subset or superset of another set.
"""
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print("Subset:", a.issubset(b))
print("Superset:", b.issuperset(a))
"""


# 57. Write a program to remove an element from a set if it exists.
"""
s = {1, 2, 3, 4}
x = int(input("Enter element to remove: "))
s.discard(x)
print(s)
"""


# 58. Write a program to find the maximum and minimum element in a set.
"""
s = {10, 5, 8, 3, 2}
print("Max:", max(s))
print("Min:", min(s))
"""


# 59. Write a program to convert a list with duplicate elements into a set to remove duplicates.
"""
lst = [1, 2, 2, 3, 4, 4, 5]
s = set(lst)
print(s)
"""


# 60. Write a program to perform union of three different sets.
"""
a = {1, 2}
b = {2, 3}
c = {3, 4}
print("Union:", a | b | c)
"""

# Operator question 



# 1. Write a program to print your name, age, and course. All the details should be stored in separate variables and then print

name = input('Enter your name:')
age = int(input('Enter your Age: '))
course = input('Enter your Course:')

print("Hello",name,"Your age is",age,"You enrolled in",course, ".")

# 2. Write a program to print the name, age, and course details of three students. All the details should be stored in separate variables and then print


s1_name = input('Enter name of student one:')
s1_age = int(input('Enter age of student one:'))
s1_course = input('Enter course of student one:')
s2_name = input('Enter name of student two:')
s2_age = int(input('Enter age of second student:'))
s2_course = input('Enter course of student two:')
s3_name = input('Enter name of student three:')
s3_age = int(input('Enter age of student three:'))
s3_course = input('Enter course of student three:')

# Printing details 
print(s1_name,s1_age,s1_course)
print(s2_name,s2_age,s2_course)
print(s3_name,s3_age,s3_course)

# in a efficient way..the answer should be :
for i in range(1, 4):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    print(f"{name} is {age} years old and enrolled in {course}.\n")
    
# 3. Write a program to sum 2 integer variable values without using a third variable

a =2
b =4
print('Sum:',a+b)

# 4. Write a program to multiply 2 floating points

a =5.6
b =3.5
print('multiplication of this two numbers is:',a*b)

# 5. Write a program to print the ASCII Value of a character variable

char = 'A'
print(ord(char))

# 6. ⁠	Write a program to create 2 variables, ianitialize them with integer values, Print the sum of both variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print('Sum:',a+b)

# 7. ⁠Write a program to create 2 variables, initialize them with integer values, Print the difference of both variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print('difference:',a-b)

# 8. ⁠Write a program to create 2 variables, initialize them with integer values, Print the multiplication of both variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print('multiplication of this two numbers is:',a*b)

# 9. ⁠Write a program to create 2 variables, initialize them with integer values, Print the division of both variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print('Division:',a/b)

# 10. ⁠Write a program to create 2 variables, initialize them with integer values, Print the division  floored value of both variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print('floor Division:',a//b)

# 11. ⁠Write a program to create 2 variables, initialize them with integer values, Print the remainder after division of both the variables

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print(a%b)

# 12. ⁠Write a program to create 2 variables, initialize them with integer values, Print the value which is first variable to the power of second variable

a = int(input('Enter first value:'))
b = int(input('Enter second value:'))

print(a**b)




# PRINT THE PATTERNS :



# Print a Square Hollow Pattern

print('*'*6)
print('*'+' '*4+'*')
print('*'+' '*4+'*')
print('*'+' '*4+'*')
print('*'+' '*4+'*')
print('*'*6)

'''Output:
******
*    *
*    *
*    *
*    *
******
'''

# Write a program to print a filled square


for i in range(8):
    print('#'*8)
    
    
'''Output:
########
########
########
########
########
########
########
########
'''

# Square fill pattern

for i in range(7):
    print('*'*7)
    
    
'''Output:

*******
*******
*******
*******
*******
*******
*******

'''

# Number tringle pattern

for i in range(1, 7):
    print(str(i) * i)
    
'''Output:

1
22
333
4444
55555
666666

'''

# Write a program to print a hollow rectangle

print('#'*6)
print('#'+' '*4+'#')
print('#'+' '*4+'#')
print('#'+' '*4+'#')
print('#'*6)

'''Output:

######
#    #
#    #
#    #
######

'''

# Up pointing arrow

print(' '*4+'*')
print(' '*3+'*'+' '+'*')
print(' '*2+'*'+' '*3+'*')
print(' '+'*'+' '*5+'*')
print('*'*3+' '*3+'*'*3)
print(' '*2+'*'+' '*3+'*')
print(' '*2+'*'+' '*3+'*')
print(' '*2+'*'*5)

'''Output:

    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****
  
'''
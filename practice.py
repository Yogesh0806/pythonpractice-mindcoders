# print('Hello, World!')
# print('Welcome to Python programming.')
# print('testing ')


# list = [8,10,6,2,4]
# swapped = True
# count = 0
# while swapped:
#     swapped = False
#     for i in range(len(list)-1):
#         count+=1
#         if list[i] > list[i+1]:
#             swapped = True
#             list[i], list[i+1] = list[i+1], list[i]
# print('Sorted list:', list)
# print('Number of comparisons:', count)


# list = [8,10,6,3,6,7,2,4]
# list.sort()
# list.reverse()
# print('Sorted list:', list)
# print('reverse sorted list:', list)


# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print('list_1:', list_1)
# print('list_2:', list_2)


# my_list = [10,8,6,4,2]
# new_list = my_list[1:3]
# print(new_list)


# my_list = [10,8,6,4,2]
# new_list = my_list[-5:3]
# print(new_list)

# new_list = my_list[:3]
# print(new_list)


# new_list = my_list[2:]
# print(new_list)


# list = [10,8,6,4,2]
# del list[1 :3]
# print(list)

# del list[:]
# print(list)


# raw = []
# for i in range(8):
#     raw.append('WHITE_POWN')



# raw = ['WHITE_POWN' for i in range(8)]
# squares = [x ** 2 for x in range(1,11)]
# two = [2 ** index for index in range(1,11)]


# print(raw) 
# print(squares)
# print(two)



# squares = [index ** 2 for index in range(1,11) ]
# odds = [element for element in squares if element % 2 !=0]
# print(odds)


# board = []
# for i in range(8):
#     row = ['Empty' for i in range(8)]
#     board.append(row)
    
# for element in board:
#     print(element)
    
# # print(len(board))


# # print(board[0][0])
# print('---------------------')

# board[0][0] = 'ROOk'
# board[0][7] = 'ROOk'
# board[7][0] = 'ROOk'
# board[7][7] = 'ROOk'

# print(board)

# print('---------------------')

# for element in board:
#     print(element)
    
# board[0][1] = 'KRIGHT'
# board[0][6] = 'KRIGHT'
# board[7][1] = 'KRIGHT'
# # board[7][6] = 'KRIGHT'

# print(board)

# for element in board:
#     print(element)
    
# print('---------------------')

# temps = [[0.0 for i in range(24)] for d in range(31)]
# temp1 = 30
# temp2 = 19
# count = 0

# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2
#         count = 0
        
# for element in temps:
#     print(element)
    
    
# print('---------------------')



# total = 0.0
# for days in temps:
#     total += days[11]
# average = total / 31

# print('Average temperature:', average)



# heighest = -100.0
# for day in temps:
#     for temps in day:
#         if temps > heighest:
#             heighest = temps
        
# print('Heighest temperature:', heighest)


# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
        
# print('Number of hot days:', hot_days)


# rooms =[[[False for r in range(20)] for f in range(15)] for t in range (3)]

# print(rooms)

# rooms[1][9][13] = True

# rooms[1][9][1] = True


# vacancy = 0
# for room_number in range(20):
#     if not rooms[1][9][room_number]:
#         vacancy += 1
        
# print('Number of vacant rooms on floor 9:', vacancy)



# def message():
#     print('Enter a value :')
    
# message()
# a = int(input())

# message()
# b = int(input())

# message()
# c = int(input())


# def message():
#     print('Enter a value :')
#     temp = int(input())
#     return temp


# a = message()
# b = message()
# c = message()

# print('a =', a)
# print('b =', b)
# print('c =', c)

# def message():
#     print('Enter a value : ')


# print('We start here.')
# print(message)
# message()
# print('Wr end here.')


# def hello(n): #Defining a function named hello that takes one parameter n
#     print('Hello,', n)   #body of the function that prints a greeting message with the value of n
    
# name = input('Enter your name: ')
# hello(name)   #Calling the function hello with the argument name, which is obtained from user input

# def message(number):
#     print('Enter a number:',number)
    
# number = 1234
# message(1)
# print(number)


# def message(what,number):
#     print('Enter ', what, 'number', number)
    
# message('telephone', 11)
# message(11,'telephone')

# message('price', 5)
# message(5, 'price')
# message('number', 'number')


# def introduction(first_name, last_name):
#     print('Hello, My name is', first_name, last_name)
    
# introduction('John', 'Smith')
# introduction('Smith', 'John')
# introduction('Soyash', 'Patel')


# introduction(last_name = 'Thakur', first_name = 'Soyash')
# introduction(first_name = 'John', last_name = 'Smith')

# def adding(a,b,c):
#     print(a, '+', b, '+', c, '=', a+b+c)
    
    
# adding(1,2,3)
# adding(c=3, a=1, b=2)
# adding(c=1, a=2, b=3)
# adding(1, c=3, b=2)
# adding(1, a=2, c=3)


# def happy_new_year(wishes = True):
#     print('Three...')
#     print('Two...')
#     print('One...')
#     if not wishes:
#         return
#     print('Happy New Year!')
    
# happy_new_year(True)
# # happy_new_year(False)

# def boring_function():
#     print("'Bordom Mode'ON.")
#     return 123

# print('The lesson is intersting!')
# boring_function()
# print('The lesson is boring...')

# def chackMyVar(variable):
#     if (variable==10):
#         print('Variable is 10')
#         return 2
#     else:
#         print('Variable is not up to the mark')
#         return
    
# chackMyVar(5)
# print()



# def list_sum(list):
#     total = 0
#     for element in list:
#         total += element
#     return total

# print(list_sum([5,4,3]))


# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(n):
#         # strange_list.insert(0, i+1)
#         strange_list.append(i+1)
    
#     return strange_list

# print(strange_list_fun(5))



# def scope_test():
#     x = 123
# scope_test()
# print(x)

# def my_function():
#     print('Do i know that variale?', var)
    
# var =1
# my_function()
# print(var)


# def mult(x):
#     var =7
#     return x * var

# var =3
# print(mult(7))


# def my_function():
#     global var
#     var = 2
#     print('Do I know that variable?', var)
    
# var = 1
# my_function()
# print(var)



# var = 2
# print(var) #Output: 2

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var()) #Output: 5
# print(var) #Output: 5


# def my_function(n):
#     print('I got', n)
#     n+=1
#     print('I have', n)
    
# var = 1
# my_function(var)
# print(var)
    

# def my_function(my_list_1):
#     print('print #1:', my_list_1)
#     print('print #2:', my_list_2)
#     my_list_1 =[0,1]
#     print('print #3:', my_list_1)
#     print('print #4:', my_list_2)
    
# my_list_2 =[2,3]
# my_function(my_list_2)
# print('print #5:', my_list_2)


# def my_function(my_list_1):
#     print('print #1:', my_list_1)
#     print('print #2:', my_list_2)
#     del my_list_1[0]
#     print('print #3:', my_list_1)
#     print('print #4:', my_list_2)
    
# my_list_2 =[2,3]
# my_function(my_list_2)
# print('print #5:', my_list_2)


# def countdown(n):
#     print(n)
#     if n == 0:
#         return
#     else:
#         print('Going in rec :', n)
#         countdown(n-1)
#         print('out of rec :', n)
# print('Starting Recursion...')
# countdown(5)  
# print('Recursion finished!')


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))

# my_tuple = (1,10,100)

# t1 = my_tuple+ (1000,10000)
# t2 = my_tuple*3

# print(len(my_tuple))
# print(len(t1))
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(10 not in my_tuple)

# my_tuple = (1,10,100)
# print(len(my_tuple))
# my_tuple +=(1000,10000)
# print(my_tuple)
# print(len(my_tuple))

# tuple_1 = (1,2,3)
# for element in tuple_1:
#     print(element)

# tuple_2 = (1,2,3,4)
# print(tuple_2)
# print(5 in tuple_2)
# print(10 in tuple_2)
# print(7 not in tuple_2)
# print(2 in tuple_2)


# tuple_3 = (1,2,3,4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2
# print(tuple_4)
# print(tuple_5)


# my_tuple = tuple((1,2,'string'))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2,4,6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type(tup))


# my_tuple = (1,2,3)
# list =[]
# for element in my_tuple:
#     list.append(element*2)
    
# print(tuple(list))


# var =123

# t1 =(1, )
# t2 =(2, )
# t3 =(3, )

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)
# print(type(t1), type(t2), type(t3))

# dictinary = {
#     'Cat': 'chat',
#     'Dog': 'chien',
#     'Horse': 'cheval'
# }

# phone_numbers = { 'boss': 5551234567, 'Suzy': 5559876543, 'Jenny': 5556781234 }
# empty_dictinary = {}

# print(dictinary)
# print(phone_numbers)
# print(empty_dictinary)
# print(type(dictinary))
# print(type(phone_numbers))
# print(type(empty_dictinary))


# print(dictinary['Cat'])
# print(phone_numbers['Suzy'])

# print(phone_numbers['bos'])


# dictionary = {
#     'cat': 'chat',
#     'dog': 'chien',
#     'horse': 'cheval'
# }
# words = ['cat', 'loin','horse']


# for word in words:
#     if word in dictionary:
#         print(word, '->', dictionary[word])
#     else:
#         print(word, 'is not in the dictionary')


# print(dictionary.keys())

# for key in dictionary.keys():
#     print(key, '->', dictionary[key])
    
# print(dictionary.items())

# for key, value in dictionary.items():
#     print(key, '->', value)

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)

# pol_eng_dict ={ 
 
#                'zemek': 'castle',
#                'woda'   : 'water',
#                'gleba'   : 'soil'
               
#                }
# print('pol_eng_dict:', pol_eng_dict)
# copy_pol_eng_dict = pol_eng_dict.copy()

# print('copy_pol_eng_dict:', copy_pol_eng_dict)



# pol_eng_dict ={ 
 
#                'zemek': 'castle',
#                'woda'   : 'water',
#                'gleba'   : 'soil'
               
#                }

# pol_eng_dict['zamek'] = 'lock'
# item = pol_eng_dict['zamek']
# print('item:', item)



# phonebook = {} #Creating an empty dictionary named phonebook

# print(phonebook)

# phonebook['boss'] = 5551234567 #Adding a key-value pair to the phonebook dictionary, where the key is 'boss' and the value is 5551234567

# print(phonebook) #output:{'boss': 5551234567}

# del phonebook['boss']
# print(phonebook)


# pol_eng_dict ={ 'kwiat' : 'flower', 'drzewo' : 'tree', 'gleba' : 'soil' }

# pol_eng_dict.update({
#     'woda' : 'water',
#     'powietrze' : 'air'
# })

# print(pol_eng_dict)

# pol_eng_dict.popitem()
# print(pol_eng_dict)



# pol_eng_dict ={ 'kwiat' : 'flower', 'drzewo' : 'tree', 'gleba' : 'soil' }
# print(pol_eng_dict)
# print(len(pol_eng_dict))

# del pol_eng_dict['gleba']
# print(pol_eng_dict)
# print(len(pol_eng_dict))

# del pol_eng_dict
# print(pol_eng_dict)


# sd = {
    
# }
# while True:
#     name = input("Enter student name: ")
#     if name == '':
#         break
#     score = int(input(f"Enter {name}'s score: "))
    
#     if score not in range(1,11):
#         break
#     if name in sd:
#         sd[name] += (score,)
#     else:
#         sd[name] = (score,)
        
# print(sd)


# for name, mark in sd.items():
#     # print(name, '->', mark)
#     sum = 0
#     for m in mark:
#         sum += m
#     print(name, '->', sum/len(mark))






# OOPS





# class
# the class is a blueprint for creating objects. It defines a set of attributes and methods th
# at the objects created from the class will have. 
# An object is an instance of a class, which means it is a specific realization of the class 
# with its own unique data and behavior.
# property is a characteristic of an object, such as its name, age, or color. It 
# is defined in the class and can be accessed and modified by the objects created from the class.

# method is a function that is defined in a class and can be called on an object created 
# from the class. It defines the behavior of the object and can access and modify the object's properties.

# self is a special keyword in Python that refers to the instance of the class that is 
# currently being accessed. It is used to access the properties and methods of the object within the class definition.

# __dict__ is a special attribute in Python that is used to store the attributes and methods of an object.
# It is a dictionary that contains the names of the attributes and methods as keys and their corresponding values as values. 
# The __dict__ attribute can be accessed to view or modify the attributes and methods of an object.


# class ThisIsMyFirstClass:
#     name = 'Soyash'
#     age = 20
    
#     def get_name(self):
#         print(self.name)
        

# first_object = ThisIsMyFirstClass()
# print(first_object)

# first_object.get_name()
# print(first_object.name)


# class student:
#     def __init__(self,name, age, gender, grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade
    
#     def printDetails(self):
#         print('Name:', self.name)
#         print('Age:', self.age)
#         print('Gender:', self.gender)
#         print('Grade:', self.grade)
        
        
# yogesh = student("Yogesh Yadav", 20, "male", "A+")
# mayur = student("Mayur", 22, "male", "A")

# print(yogesh)
# print(mayur)

# yogesh.name = "Yogesh Yadav"
# yogesh.age = 20
# yogesh.gender = "male"
# yogesh.grade = "A+"

# print('Name:', yogesh.name)
# print('Age:', yogesh.age)
# print('Gender:', yogesh.gender)
# print('Grade:', yogesh.grade)
# yogesh.printDetails()
# mayur.printDetails()


# class ExampleClass:
#     def __init__(self,val=1):
#         self.first = val
        
#     def set_second(self,val):
#         self.second = val
        
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__) 
# print(example_object_3.__dict__)



# class classy:
#     def method(self, par):
#         print('method',par)
        
        
# obj = classy()
# obj.method(1)



# class classy:
#     varia = 2
#     def method(self):
#         print(self.varia,self.var)
        
# obj = classy()
# obj.var = 3 
# obj.method()


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
        
# sun = Star('Sun', 'Milky Way')
# print(sun)


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
#        return self.name + ' in '+ self.galaxy
# sun = Star('Sun', 'Milky Way')
# print(sun)


# class Vehicle:
#     pass 

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass



# class Vehicle:
#     pass 

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end='\t') #issubclass() is a built-in function in Python that checks if a class is a subclass of another class. It takes two arguments: the first argument is the class to check, and the second argument is the class to compare against. The function returns True if the first class is a subclass of the second class, and False otherwise.
#     print()


# class Super:
#     supVar = 1
    
# class Sub(Super):
#     subVar = 2
    
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


# class Super:
#     def __init__(self):
#         self.supVar = 11
        
# class Sub(Super):
#     def __init__(self):
#         super().__init__() #super() is a built-in function in Python that returns a temporary object of the superclass that allows you to call its methods. It is commonly used in the __init__ method of a subclass to call the __init__ method of the superclass and initialize its attributes.
#         self.subVar = 12
        
        
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)


# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = Level3()
# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())


#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# def factorial(n):
#     if n == 0:
#         return 1
#     # Write your code here
#     return n * factorial(n-1)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     result = factorial(n)

#     fptr.write(str(result) + '\n')

#     fptr.close()
    
    
# class ExampleClass:
#     counter = 0
#     def __init__(self,val=1):
#         self._first = val  
#         ExampleClass.counter += 1
        
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)


# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         ExampleClass.counter += 1
#         if val%2!= 0:
#             self.a =1
#         else:
#             self.b = 2
            
# example_object = ExampleClass(3)
# print(example_object.a)
# print(example_object.b)

# # Output: if we provide even value then it will print 2 and if we provide odd value then it will print 1. In this case, since we provided 3 (which is odd), it will print 1 for example_object.a and will raise an AttributeError for example_object.b because it does not exist in the object.

#Excaption handling:


# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         ExampleClass.counter += 1
#         if val%2!= 0:
#             self.a =1
#         else:
#             self.b = 2
            
# example_object = ExampleClass(8)

# try:
#     print('a = ',example_object.a)
# except AttributeError:
#     try:
#         print('b = ',example_object.b)
#     except AttributeError:
#         print('The error has occured! Sliently passing it!')
        
        
# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         ExampleClass.counter += 1
#         if val%2!= 0:
#             self.a =1
#         else:
#             self.b = 2
            
# example_object = ExampleClass(1)

# if hasattr(example_object, 'a'):
#     print('a = ',example_object.a)
    
# if hasattr(example_object, 'b'):
#     print('b = ',example_object.b)
    
    
    
# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         ExampleClass.counter += 1
#         if val%2!= 0:
#             self.a =1
#         else:
#             self.b = 2
            
            
# example_object = ExampleClass(1)


# if hasattr(example_object, 'a'):
#     print('a = ',example_object.a)
    
# if hasattr(example_object, 'b'):
#     print('b = ',example_object.b)
    
    
# print(hasattr(example_object, 'a'))
# print(hasattr(example_object, 'b'))


# class Python :
#     population =1
#     victims = 0
#     def __init__(self):
#         self.lengh_ft = 3
#         self.__venomous = False
        
# myObj = Python()
# print('myObj.population:', myObj.population)
# print('myObj.victims:', myObj.victims)
# print('myObj.lengh_ft:', myObj.lengh_ft)
# # print('myObj.__venomous:', myObj.__venomous) #This will raise an AttributeError because __venomous is a private attribute and cannot be accessed directly from outside the class. To access it, we would need to use a method defined within the class that returns its value or use name mangling to access it indirectly.
# # print('myObj.venomous:', myObj.venomous) #this will raise an AttributeError because the attribute is defined with double underscores, which makes it a private attribute and it cannot be accessed directly from outside the class. To access it, we would need to use a method defined within the class that returns its value or use name mangling to access it indirectly.
# print('myObj._Python__venomous:', myObj._Python__venomous) #This will print the value of the private attribute __venomous using name mangling, which allows us to access it indirectly by using the class name and the attribute name with double underscores. In this case, it will print False, which is the value assigned to __venomous in the __init__ method of the Python class.





#  Name mangling 


# Name mangling is a technique used in Python to access private attributes and methods of a class. When an attribute or method is defined with double underscores (e.g., __attribute), it is considered private and cannot be accessed directly from outside the class. However, Python provides a way to access these private members using name mangling, which involves prefixing the attribute or method name with the class name and a single underscore (e.g., _ClassName__attribute). This allows us to access the private members indirectly while still maintaining encapsulation.

# class Classy:
#     def visible(self):
#         print('This method is visible')  
    
#     def __hidden(self):
#         print('This method is hidden')
        
# obj = Classy()
# obj.visible() #output: visible
# try:
#     obj.__hidden() # This fails
# except:
#     print('Failed to access hidden method') #output: Failed to access hidden method
    
# obj._Classy__hidden() #output: This method is hidden

# obj = Classy()
# print(type(obj))
# print(type(obj).__name__)

#INHERITANCE CONTINUE


# class Vehicle:
#     pass 

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()


# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end='\t') #isinstance() is a built-in function in Python that checks if an object is an instance of a specified class or a subclass thereof. It takes two arguments: the first argument is the object to check, and the second argument is the class or a tuple of classes to compare against. The function returns True if the object is an instance of the specified class or any of its subclasses, and False otherwise.
#     print()
    
# class SampleClass:
#     def __init__(self,val):
#         self.val = val
        
# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_1 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)


# string_1 = 'Mary had a little '
# string_2 = 'Mary had a little lamb'
# string_1 += 'lamb' 

# print(string_1 == string_2, string_1 is string_2)


# class Super :
#     def __init__(self,name):
#         self.name = name
        
#     def __str__(self):
#         return 'My name is ' + self.name+ '.'
    
# class Sub(Super):
#     def __init__(self,name):
#         super().__init__(name)
        
# obj = Sub('Andy')
# print(obj)

# class SuperA:
#     var_a =10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b =20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

#MULTIPLE INHERITANCE 

# class Level1:
#     var = 100
#     def fun(self):
#         return 101
    
# class Level2:
#     var = 200
#     def fun(self): #Overriding the fun method of Level1 class in Level2 class
#         return 201 #overrides Level1.fun()

# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var, obj.fun())

#MULTIPLE INHERITANCE 



# class Left:
#     var = 'L'
#     var_left = 'LL'
#     def fun(self):
#         return 'Left'

# class Right:
#     var = 'R'
#     var_right = 'RR'
#     def fun(self):
#         return 'Right'
    
# class Sub(Left, Right):
#     pass

# obj = Sub()
# print(obj.var,obj.var_left, obj.var_right, obj.fun())

#polymorphism


# class One:
#     def do_it(self):
#         print('Do_it from one')
    
#     def doAnything(self):
#         self.do_it() #This line calls the do_it() method of the class. However, since the do_it() method is overridden in the Two class, when doAnything() is called on an instance of Two, it will use the overridden version of do_it() from the Two class instead of the one from the One class. This is an example of polymorphism, where a method can have different implementations in different classes, and the appropriate implementation is chosen at runtime based on the type of the object calling the method.
    
# class Two(One):
#     def do_it(self):
#         print('Do_it from two')
    
    
# one = One()
# two = Two()
# one.doAnything() #Output: Doing anything in One way
# two.doAnything() #Output: Doing anything in Two way because of polymorphism, where the method do_it() is overridden in the Two class, and when doAnything() is called on an instance of Two, it uses the overridden version of do_it() from the Two class instead of the one from the One class.



# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print('Division failed')
#         return 'Alibabaa ka chamatkar'
#     else:
#         print('Everything went well!')
#       # return n
#     finally:
#         print('Its time to say goodbye!')
#         return n
    
# print('---------')
# print('reciprocal(2):', reciprocal(2))   # uses else block
# print('---------')
# print('reciprocal(0):', reciprocal(0))
# print('---------')

# try:
#     i = int('Hello')
# except Exception as e:
#     print('An error occurred:', e)
#     print(e.__str__())
    
# class MyzeroDivisionError(ZeroDivisionError):
#     pass

# def do_the_division(mine):
#     if mine:
#         raise MyzeroDivisionError('Some worse news')
#     else:
#         raise MyzeroDivisionError('Some bad news')
    
# do_the_division(False)

# CONTINUE STRING MANIPULATION

# city = 'New York'

# print(city[0]) #Output: N
# print(city[1]) #Output: e
# print(city[2]) #Output: w
# print(city[-1]) #Output: k
# print(city[3]) #Output:  ' '
# print(city[4]) #Output: Y
# print(city[-2]) #Output: r
# print(city[5]) #Output: o
# print(city[6]) #Output: r
# print(city[7]) #Output: k

# print(city[::2]) #Output: NwYrk  #This slice notation means to take every second character from the string, starting from the first character (index 0). So it takes 'N' (index 0), skips 'e' (index 1), takes 'w' (index 2), skips ' ' (index 3), takes 'Y' (index 4), skips 'o' (index 5), takes 'r' (index 6), and skips 'k' (index 7). The resulting string is 'NwYrk'.


# text = 'Hello Python World'

# #Case

# print(text.upper()) #Output: HELLO PYTHON WORLD
# print(text.lower()) #Output: hello python world
# print(text.title()) #Output: Hello Python World
# print(text.capitalize()) #Output: Hello python world

# #Strip whitespace
# print(text.strip()) #Output: Hello Python World


# #search 
# print('Python' in text) #Output: True
# print(text.find('Python')) #Output: 6
# print(text.count('l'))

# #split and join 

# csv = 'Rahul,22,Bhopal,Engineer'
# parts  = csv.split(',') 

# print(parts)
# print(parts[0])

# rejoined = ' | '.join(parts)
# print(rejoined)

# #Chack content

# print('hello123'.isalnum())
# print('12345'.isdigit())
# print('Python'.isalpha())
# print(' '.isspace())

# #start/end check

# email = 'student@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))

# name, marks, rank = 'Anita', 92.567, 3

# #basic

# print(f'Hello, {name}')

# #format numbers 
# print(f'Marks:{marks:.2f}')
# print(f'marks: {marks:.0f}')
# print(f'Count:{10000000:,}')

# #padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')
# print(f'hello {name:^10}')
# print(f'hello {name:>10}')
# print(f'hello {name:<10}')
# print(f'hello {name:*^10}')

# #Expression inside{}

# price, gst = 500, 0.18
# print(f'Price:Rs{price} | GST:Rs{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')


#WITH OPEN FUNCTION

# with open('data.txt', 'r') as file:
#     data = file.read()
    
# print(data) 

# with open('student.txt','w') as f:
#     f.write('Rahul Sharma,85, Bhopal\n')
#     f.write('Priya Verma,92,Indore\n')
#     f.write('Amit Kumar, 73,Jabalpur\n')
    
# with open('student.txt', 'a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')
    
# with open('student.txt','r') as f:
#     content = f.read()
    
# print(content)

# with open('student.txt', 'r') as f:
#     for line in f:
#         name, marks, city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print('-----------------')

#Creating csv with python


import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','C'],
#     ['Amit',73,'Jabalpur','B'],
# ]

# with open('student.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)
    
#Reading a csv with python

# with open('student.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row['Name']}: {row['Marks']} marks ({row['City']})')
        


records = [
    ['Name','Age','Subject1','Subject2','Subject3'],
    ['Rahul',20,98,25,86],
    ['Yogesh',21,89,97,96],
    ['Priyansh',20,49,76,85],
]

with open('new.csv','w', newline='') as f:
    csv.writer(f).writerows(records)
    
# with open('new.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row['Name'] == 'Yogesh':
#             print(row['Yogesh'])


# flag =0
# with open('new.csv','r') as f:
#     name = input('Enter name : ')
#     for row in csv.DictReader(f):
#         if row['Name'] == name :
#             flag +=1
#             break
    
# if flag == 1:
#     print(f'{row['Name']}: Subject1 {row['Subject1']} Subject2 {row['Subject2']} Subject3 {row['Subject3']}')
    
# else:
#     print('Student data not found')


import numpy as np

# arr1d = np.array([1,2,3,4,5])
# print(arr1d)
# arr2d = np.array([[89,86,34],[86,33,83],[33,35,27]])

# print(arr2d.shape)
# print(arr2d.dtype)
# print(arr2d.ndim)

# zeros = np.zeros((3,4))
# print(zeros)

# ones = np.ones((2,5))
# print(ones)

# rng = np.arange(0,51.5)
# print(rng)

# lin = np.linspace(0,1,11)
# print(lin)

# random = np.random.randint(40,100,(5,3))
# print(random)

# arr = np.array([10,20,30,40,50])

# print(arr*2)
# # [ 20  40  60  80 100]
# print(arr+5)
# # [15 25 35 45 55]
# print(arr**2)
# # [ 100  400  900 1600 2500]


# marks_2d = np.array([[85,90,78],[86,47,89],[37,95,99]])

# print('Mean : ',np.mean(marks_2d))
# print('Mean of row : ',np.mean(marks_2d, axis= 1))
# print('Mean of column : ',np.mean(marks_2d,axis=0))
# print('highest value of arr :',np.max(marks_2d))
# print('Standard Deviation: ',np.std(marks_2d))

#Boolean indexing

# arr = np.array([55,36,83,73,86,46,97,44,79])
# print(arr[arr > 70])


import pandas as pd 

# data = {
#     'Name' : ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
#     'Age' : [22,21,23,20,24],
#     'Marks' : [85,92,78,88,73],
#     'City' : ['Bhopal','Indore','Bhopal','Jabalpur', 'Indore'],
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())



# print("df['Name']: \n", df['Name'])
# print(df[['Name', 'Marks']])

# # Filter rows
# print(df[df['Marks']>=85])
# print(df[df['City'] == 'Bhopal'])


# print( df[ (df['Marks']>=80) & (df['City'] == 'Indore') ] )


# def get_grade(x):
#     if x >= 90 :
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else :
#         return 'C'
    
    
# df['Grade']  = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print('-------------------')
# print(df)

#GroupBy - like Excel pivot
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)


#Read real CSV file and perform data cleaning 
# df2 = pd.read_csv('student.csv')

# # print(df2)
# df2.to_csv('clean_output.csv', index=False )

# df2['Name'] = df2['Name'].str.strip()
# print(df2['Name'])


# df2['Marks'] = df2['Marks'].str.replace('#','')
# print(df2['Marks'])

# print(df2)

# df2['City'] = df2['City'].str.replace('Dist','').str.replace('City','')
# print(df2['City'])

# df2['Grade'] = df2['Grade'].str.replace(r'@','')

# print(df2['Grade'])


# print(df2)

# df2.to_csv('clean_output.csv', index=False )

import matplotlib.pyplot as plt

# # Data 
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales = [45, 52, 48, 61, 58, 72, 69, 75, 68, 82, 90,  95] # in thousands 

# #LINE CHART - trend over a time 

# plt.figure(figsize=(12,5))
# plt.plot(months, sales, marker = 'o', color= 'steelblue', linewidth = 2, markersize=8)
# plt.fill_between(months, sales, alpha = 0.15, color= 'steelblue')
# plt.title('Monthly Sales 2024 (Rs. Thousands)', fontsize = 14, fontweight='bold')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs. K)')
# plt.grid(True, alpha = 0.3)
# plt.tight_layout()
# plt.show()


# cities = ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain']
# students =  [1200, 2800, 980, 850, 650]
# colors = [
#     "#0000FF",  # Blue
#     "#008000",  # Green
#     "#FFA500",  # Orange
#     "#FFC0CB",  # Pink
#     "#FF0000"   # Red
# ]

# #Baar chart 

# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, students, color= colors, edgecolor = 'white', linewidth = 1.5)
# plt.title('Students Enrolled per City')
# plt.ylabel('Number of students')
# for  bar,val in zip(bars, students):
#     plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha = 'center', fontweight='bold')
# plt.tight_layout()
# plt.show()         


# #SCATTER PLOT - Relation between x and y 

# study_hrs = np.random.uniform(2,10,50)
# marks = study_hrs*7 + np.random.normal(0,8,50)
# marks = np.clip(marks, 30, 100)

# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs, marks, c = marks, cmap = 'RdYlGn', s =100, alpha=0.8)
# plt.title('Study Hours vs Exam Marks')
# plt.colorbar(label = 'Marks')
# plt.xlabel('Study Hours/ Day')
# plt.ylabel('Exam Marks')
# plt.show()


import seaborn as sns

# np.random.seed(42)

df = pd.DataFrame({
    'marks' : np.random.randint(40,100,100),
    'study_hrs' : np.random.uniform(2,10,100),
    'city' : np.random.choice(['Bhopal', 'Indore', 'Jabalpur'],100),
    'gender' : np.random.choice(['Male', 'Female'], 100),
    
})

# #Histogram with KDE - See the distribution 

# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'], bins =20, kde =True, color = 'steelblue')
# plt.title('Distribution of Student Marks')
# plt.show()

# # Box plot - outliers and spread per group
# sns.boxplot(data = df, x ='city', y = 'marks', palette= 'Set1')
# plt.title('marks distribution by city')
# plt.show()

# # correlation heatmap - critical in data science 

# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks', 'study_hrs']].corr(), annot=True,cmap='coolwarm', vmin=-1,vmax=1)
# plt.title('Correlation Matrix')
# plt.show()

# # pair plot - all relationship at once 

# sns.pairplot(df[['marks', 'study_hrs']], diag_kind='kde')
# plt.show()



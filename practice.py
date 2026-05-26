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

my_tuple = (1,10,100)

t1 = my_tuple+ (1000,10000)
t2 = my_tuple*3

print(len(my_tuple))
print(len(t1))
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(10 not in my_tuple)
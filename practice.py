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


rooms =[[[False for r in range(20)] for f in range(15)] for t in range (3)]

print(rooms)

rooms[1][9][13] = True

rooms[1][9][1] = True


vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
        
print('Number of vacant rooms on floor 9:', vacancy)
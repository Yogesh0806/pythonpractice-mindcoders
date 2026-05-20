# print('Hello, World!')
# print('Welcome to Python programming.')
# print('testing ')

list = [8,10,6,2,4]
swapped = True
count = 0
while swapped:
    swapped = False
    for i in range(len(list)-1):
        count+=1
        if list[i] > list[i+1]:
            swapped = True
            list[i], list[i+1] = list[i+1], list[i]
print('Sorted list:', list)
print('Number of comparisons:', count)


list = [8,10,6,3,6,7,2,4]
list.sort()
print('Sorted list:', list)
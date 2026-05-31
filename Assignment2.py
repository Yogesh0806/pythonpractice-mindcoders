#LOOPS

# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prints the length of the existing list (Step 1).
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 3)

list = [1,2,3,4,5]
#step : 1
print(len(list))
# Step : 2
del list[-1]
print(list)

# step : 3 
number = int(input('Enter your number:'))

list[len(list)//2] = number

print(list)

# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print(beatles)

for name in range(2):
    name = input('Enter a name:')
    beatles.append(name)

print(beatles)

del beatles[3:]
print(beatles)

beatles.insert(0,'Ringo Starr')
print(beatles)

# Write a program to print numbers from 1 to 50 in this pattern
# [1, 2, Fiz, 4, Buzz, Fiz, 7, 8, Fiz, Buzz, 11, Fiz, 13, 14, FizBuzz, 16....50]
for i in range(1,51):
    if i%3==0 and i%5==0:
        print('FizBuzz', end=' ')
    elif i%3==0:
        print('Fiz', end=' ')
    elif i%5==0:
        print('Buzz', end =' ')
    else:
        print(i, end=' ')
        
# Write a Program to Count Numbers of Digits in this String
# Input: string = "MindCoders password2 is : 1234"
# Output: Total number of Digits = 5
string = "MindCoders password2 is : 1234"
count = 0
for char in string:
    if char.isdigit():
        count+=1
print('Total number of Digits =',count)

# Write a Program to Count Numbers of Digits in this String
# Input: string = "U r a a n S 0 f t s k i l l 1 s 1234"
# Output: Total number of Digits = 6
string = "U r a a n S 0 f t s k i l l 1 s 1234"
count = 0
for char in string:
    if char.isdigit():
        count+=1
print('Total number of Digits =',count)

# Write a program to find the count for the occurrence of 's' or 'S' character in a string
# Input: "MindCoders"
# Output: 3
word = 'MindCoders'
count =0

for char in word:
    if char =='s' or char =='S':
        count +=1
print(count)

# Write a program to count the number of repeated characters and unique characters in a string
# Input: "UraanSoftskills"
word ="UraanSoftskills"
unique =0
repeated = 0

for ch in set(word):
    if word.count(ch)>1:
        repeated+=1
    else:
        unique+=1
print("Unique characters:", unique)
print("Repeated characters:", repeated)

# Write a program to find the frequency of each character in a given string
# Input: "UraanSoftskills"
word = "UraanSoftskills"

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch, count in freq.items():
    print(ch, ":", count)
    
# You must design the (ugly) vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:
# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

word = input('Enter your word:')
word = word.upper()
# print(word)
word_without_vowels = ''
for i in word:
    if i in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        word_without_vowels += i
print(word_without_vowels)

# 1. Write a program to print the first 10 natural numbers using for loop
for number in range(1,11):
    print(number, end = ' ')
    
# 2. Write a program to print all the even numbers within the range of 10
for number in range(11):
    if number%2==0:
        print(number)
        number +=1
        
# 3. Write a program to calculate the sum of all numbers from 1 to a given number - 15
sum = 0
for i in range(16):
    sum = sum+i

print(sum)
# BEST APPROACH
# print(sum(range(16)))

# 4. Write a program to calculate the sum of all the odd numbers within the given range of 15
sum =0
for num in range(16):
    if num%2!=0:
        sum = sum+num

print(sum)

# 5. ⁠Write a program to print a multiplication table of a given number 15

for i in range(1,11):
    print(i*15)
    
# 6. ⁠Write a program to display numbers from a list using a for the loop [1,2,4,6,88,125]
list = [1,2,4,6,88,125]

for element in list:
    print(element)
    
# 7. ⁠Write a program to count the total number of digits in a number 129475
num = 129475
count = 0
while num>0:
    num = num//10
    count +=1

print('the total numbers in digit is :', count)
    
# 8. ⁠Write a program to check if the given string is a palindrome - madam
text = 'madam'
length =len(text)

for i in range(length//2):
    if text[i] != text[length-1-i]:
        print('not palindrome')
        break

else:
    print('palindrome')


# 9. ⁠Write a program that accepts a word from the user and reverses it
word = input('Enter your word: ')
rev = ''
for i in word:
    rev = i + rev
print(rev)


# 10. ⁠Write a program to check if a given number is an Armstrong number 153
num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10      # last digit nikalo
    sum = sum + digit**3   # cube karke add karo
    temp = temp // 10      # last digit hata do

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    
    
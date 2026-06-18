'''
- Write a program that utilizes the concept of conditional execution, takes a string as input, and:
1. prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen 
2. ⁠if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" 
3. if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
'''
plant = input("Enter which Plant is best: ")

if plant =='Spathiphyllum':
    print('Yes - Spathiphyllum is the best plant ever!')
elif plant =='spathiphyllum':
    print('No, I want a big Spathiphyllum!')
else:
    print(f'Spathiphyllum! Not {plant}!')

    '''OUTPUT:
    Enter which Plant is best: Rose
Spathiphyllum! Not Rose!
'''

# 1, 2, 3, 4, 5….50

for i in range(1,51):
    print(i, end = ' ')
    
# 1, t, 3, t, 5, t, 7, t, 9……50

for i in range(1,51,2):
    print(i, end = ', t, ')
    
# 1, 2, t, 4, 5, t, 7, 8, t…..50

count =0
for i in range(1,51):
    if count ==2:
        print('t',end=', ')
        count =0
    else:
        print(i, end =', ')
        count +=1
        
# 1, 2, fiz, 4, buz, fiz, 7, 8, fiz, buz, 11, fiz, 13, 14, fizbuz, 16……50

for i in range(1,51):
    if i%3 ==0 and i%5==0:
        print('fizbuz', end=' ')
    elif i%3 ==0:
        print('fiz', end=' ')
    elif i %5 ==0:
        print('buz', end=' ')
    else:
        print(i, end=' ')
        
'''Practice Question:
Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
1. if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
2. ⁠if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to 
1. write a tax calculator.
It should accept one floating-point value: the income.
2. Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
Note: this happy country never returned any money to its citizens. If the calculated tax was less than zero, it would only mean no tax at all (the tax was equal to zero). Take this into consideration during your calculations.
'''

income = float(input('Enter your Income: '))
    
if income <85528:
    tax = income*0.18-556.02
else:
    tax = 14839.02+(income-85528)*0.32
if tax<0:
    tax=0

print("Tax =", round(tax), "Thalers")

'''Practice Question:
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
1. if the year number isn't divisible by four, it's a common year;
2. ⁠otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, 
3. if the year number isn't divisible by 400, it's a common year;
4. ⁠otherwise, it's a leap year.
Write code – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period.
'''
year = int(input('Enter a year whether it is leap year or not'))

if year < 1582:
    print(f'{year} not in a Gregorian calendar period.')
elif year % 4 != 0:
    print('its common year!')
elif year %100!=0:
    print('its leap year')
elif year % 400 !=0:
    print('its common year')
else:
    print('Its leap year.')
    
'''Do you know what Mississippi is? 
It's the name of one of the states and rivers in the United States. The Mississippi River is about 2,340 miles long, which makes it the second longest river in the United States (the longest being the Missouri River). It's so long that a single drop of water needs 90 days to travel its entire length!
The word Mississippi is also used for a slightly different purpose: to count mississippily.
If you're not familiar with the phrase, we're here to explain to you what it means: it's used to count seconds.
The idea behind it is that adding the word Mississippi to a number when counting seconds aloud makes them sound closer to clock-time, and therefore "one Mississippi, two Mississippi, three Mississippi" will take approximately an actual three seconds of time! It's often used by children playing hide-and-seek to make sure the seeker does an honest count.
Your task is very simple here: write a program that uses a for loop to "count mississippily" to five. Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"
'''


for i in range(1,6):
    print(i, 'Mississippi')
    # i+=1

print('Ready or not, here I come!')
    
    
'''You must design the (ugly) vowel eater! Write a program that uses:
1. a for loop;
2. the concept of conditional execution (if-elif-else)
3. the continue statement.
Your program must:
1. ask the user to enter a word
2. use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
3. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
4. ⁠assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
'''

user_word = input('Enter your word:')

word_without_vowels = ''
user_word = user_word.upper()

for element in user_word:
    if element in 'AEIOU':
        continue

    word_without_vowels +=element

print(word_without_vowels)


'''Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.
Their pyramid is a bit weird, as it is actually a pyramid-shaped wall – it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
The figure illustrates the rule used by the builders:
Your task is to write a program which reads the number of blocks 
the builders have, and outputs the height of the pyramid that can 
be built using these blocks.
Note: the height is measured by the number of fully completed layers – 
if the builders don't have a sufficient number of blocks and cannot 
complete the next layer, they finish their work immediately.
'''


blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("The height of the pyramid:", height)


'''In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:
1. take any non-negative and non-zero integer number and name it c0;
2. ⁠if it's even, evaluate a new c0 as c0 ÷ 2;
3. ⁠otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4. ⁠if c0 ≠ 1, go back to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.
Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number (it may even require artificial intelligence), but you can use Python to check some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
Hint: the most important part of the problem is how to transform Collatz's idea into a while loop – this is the key to success.
'''


c0 = int(input('Enter a non-negative and non-zero number :'))
steps = 0 

while c0 !=1:
    print(c0)
    
    if c0%2==0:
        c0=c0//2
    else:
        c0=3*c0+1

    steps +=1

print(c0)
print('Steps : ',steps)


# @author: Kevin Kimani

# Import random module to be able to generate random numbers 
import random

# Declare dice faces and assign them an initial value of zero
f_one, f_two, f_three, f_four, f_five, f_six = 0, 0, 0, 0, 0, 0

# Range syntax is range(start, stop). Start specifies the start position. Stop specifies at which position to stop(not included)
for x in range(1, 1001):
    outcome = random.random()
    if outcome <= 1/6:
        f_one = f_one + 1
    elif outcome <= 2/6:
        f_two = f_two + 1
    elif outcome <= 3/6:
        f_three = f_three + 1
    elif outcome <= 4/6:
        f_four = f_four + 1
    elif outcome <= 5/6:
        f_five = f_five + 1
    elif outcome <= 6/6:
        f_six = f_six + 1

totalFrequency = f_one + f_two + f_three + f_four + f_five + f_six
totalPercentage = totalFrequency / 10

print('Face |   Frequency   |   Percentage')
print('-----------------------------------')
print('1        ', f_one, '         ', (f_one / 10), '%')
print('2        ', f_two, '         ', (f_two / 10), '%')
print('3        ', f_three, '         ', (f_three / 10), '%')
print('4        ', f_four, '         ', (f_four / 10), '%')
print('5        ', f_five, '         ', (f_five / 10), '%')
print('6        ', f_six, '         ', (f_six / 10), '%')
print('-----------------------------------')
print('Total:   ', totalFrequency, '        ', totalPercentage, '%')    
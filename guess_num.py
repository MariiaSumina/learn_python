'''
Guess the Number:
Generate a random number between 1 and 100.
Ask the user to guess the number. Use a while
loop to keep prompting the user for guesses
until they correctly guess the number.
'''
import random
userQuestion = int(input('Please enter number: '))
answer = int(input('Please enter answer: '))
count = 0

while userQuestion != answer:
    count += 1
    answer = int(input('Please enter answer: '))
print(f'You guessed the number in {count} times')
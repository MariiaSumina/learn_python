"""
Even or Odd Sum:
Create a program that calculates
the sum of all even or odd numbers
(user's choice) from 1 to a given
integer input using a while loop.
"""

user_choice = int(input("Please enter the number: "))
count = 0
even_sum = []
odd_sum = 0

while count < user_choice:
    count += 1
    if count % 2 == 0:
        even_sum.append(count)
    else:
        odd_sum += count
        print(odd_sum)

print(f"sum of odd number {odd_sum} and sum of even numbers is {sum(even_sum)}")
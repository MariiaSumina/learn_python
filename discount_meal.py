user_age = int(input('Please enter your age: '))
SENIOR_AGE = 60

if 1 <= user_age <= 13:
    print("Half off for the meal")
elif user_age > 60:
    print("20% off")
else:
    print("no discounts available")

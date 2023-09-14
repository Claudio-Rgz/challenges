# Program that asks the user for a number and then prints out a list of all the divisors of that number.

number = 235

divisors = []

for divisor in range(1, number+1):
    if number % divisor == 0:
        divisors.append(divisor)

print(divisors)
# First, we ask the user to input a number, and convert the str to int.pytho

num = int(input("Give me any number and I'll check if its a palindrome: "))

# We initialize an empty variable to store the reversed number and another variable that will go through the process of the loop to reverse the original number (so we don't affect the num variable that we will use at the end to compare the original number and the reversed number we got.)

check_num = num
reversed_num = 0

# We reverse the number by using the loop explained in reverse_an_int.

while check_num > 0:
    digit = check_num % 10
    reversed_num = (reversed_num * 10) + digit
    check_num = check_num // 10 

#Then we check if the reversed number is equal to the given number. 
if num == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")



# First, we ask the user to input a number, and convert the str to int. For this example we will suppose the number given is 1359.

num = int(input("Give me any number and I'll reverse it: "))

# We initialize an empty variable to store the reversed number.

reversed_num = 0

# We reverse the number by using modulo 10 (remainder of dividing by 10), storing it into a variable called "reversed num". Then we multiply our reversed number by 10 to compensate for the division (in this example it would look something like step 1: (0 * 10) + 9 which equals 9, step 2: (9 * 10) + 5 which equals 95, step 3: (95 * 10) + 3 which equals 953, and then step 4: (953 * 10) + 1 which equals 9531.

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10 

#Then we just simply print the variable containing the reversed number. 
print(reversed_num)



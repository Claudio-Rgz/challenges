def prime_or_not(number):
    """This function takes an int and prints if it's a prime number or not."""
    try:
        if number % 2 == 0 and number % number == 0:
            prime = True
            print(f"The number {number} is prime.")
        else:
            print(f"The number {number} is not prime.")
    except ZeroDivisionError:
        print("Zero can't be divided")
    
for i in range(100):
    prime_or_not(i)
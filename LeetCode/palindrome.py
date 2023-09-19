
def palindrome_checker(x):
    """Takes a random int and checks if it's a palindrome or not."""
    x = str(x)
    n = x[::-1]
    if x == n:
        print(f"{x} is a palindrome.")
    else:
        print(f"{x} is not a palindrome.")

palindrome_checker()
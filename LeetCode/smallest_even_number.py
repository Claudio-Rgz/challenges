def smallest_even_number(n):
    """Given a positive integer 'n', return the smallest positive integer that is a multiple of both 2 and 'n'."""
    if n % 2 == 0:
        print(n)
    while n % 2 != 0:
        n = n + n
        if n % 2 == 0:
            print(n)


smallest_even_number(13)
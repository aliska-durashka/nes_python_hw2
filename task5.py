def prime(n):
    if n <= 1:
        return False

    for divisor in range (2, n):
        if n % divisor == 0:
            return False


    return True

print(prime(7))
print(prime(18))
print(prime(33))
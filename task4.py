
def sumdigits(n):
    return sum(int(digit) for digit in str(n))
print(sumdigits(74632506475))
print(sumdigits(11111))
print(sumdigits(8956380))
print(sumdigits(000000))
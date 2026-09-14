def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

print(leap(2000))
print(leap(2026))
print(leap(2011))


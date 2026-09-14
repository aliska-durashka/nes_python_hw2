
def lrot(L,n):
    return L[-n:]+L[:-n]

print(lrot([10,30,46,22,71,75],2))
print(lrot([10,30,46,22,71,75], -2))
print(lrot([10,30,46,22,71,75],7))
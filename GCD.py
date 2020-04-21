#Greatest common divisor
def gcd(a,b):
    if a < b:
        (a,b) = (b,a)
    while b != 0:
        (a,b) = (b,a%b)
    return a
print(gcd(12,4))

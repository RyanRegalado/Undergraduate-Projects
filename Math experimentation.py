import math

print("Welcome to a binomial distrubution calculator")

p = float(input("What is your probability of success? MUST BE BETWEEN 0 AND 1. "))
n = int(input("How many trials are you running? "))
r = int(input("How many successes are you looking for? "))
c = math.comb(n,r)
binompdf = c*(p**r)*((1-p)**(n-r))

print(f"The probability of getting {r} successes out of {n} trials is {binompdf}")

var = 0
L = r
while L > 0:
    var = binompdf + var
    L = L-1
    c = math.comb(n, L)
    binompdf = c * (p ** L) * ((1 - p) ** (n - L))
var = math.comb(n,0)*(1-p)**n + var

print(f"The probability of getting {r} or less successes out of {n} trials is {var}")


## Main Areas of Confusion:
## Insert * binompdf)between every multiplication
## Using parenthesis like (2)(4) does not work
## Floats for decimals, int for integers
## ** is exponentiation
## define variables before making operations EX) var = 3 + r
##                                           Not) 3 + r = var(





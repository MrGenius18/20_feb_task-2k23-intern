'''
# Find LCM & HCF
    LCM ==> highest common factor of two numbers
    HCF ==> lowest common multiplier of the two numbers
'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find the HCF
HCF = 1
for i in range(2,a+1):
    if(a%i==0 and b%i==0):
        HCF = i
print(f"HCF of {a} and {b} will be {HCF}")

# Find the LCM
LCM = int((a*b)/(HCF))
print(f"LCM of {a} and {b} will be {LCM}")



from math import lcm
x = lcm(a,b)
print(x)

from math import gcd
x = gcd(a,b)
print(x)
'''
# given number is armstrong or not
    153 = 1^3+5^3+3^3 = 153
    1634 = 1^4+6^4+3^4+4^4 = 1634
'''

number = int(input("Enter the number: "))

count = 0
num = number

power = len(str(number))
print(f"power---> {power}")

while num!=0:
    index = num % 10
    count += index ** power
    num = num // 10

if number == count:
	print(f"The given number {number} is armstrong number")
else:
	print(f"The given number {number} is not armstrong number")


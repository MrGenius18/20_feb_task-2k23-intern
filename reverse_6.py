'''
# reverse a number 
    123 <==> 321
    456 <==> 654
'''

num = int(input("Enter the Number: "))
a = 0
while(num!=0):
    digit = num%10
    a = a*10 + digit
    num //= 10

print(f"Reversed Number:- {str(a)} ")
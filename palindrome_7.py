'''
# palindrome  
    121
'''

num = int(input("Enter a value you want to find :"))  
temp = num  
rev = 0  
while(num > 0):  
    digit = num % 10  
    rev = rev * 10 + digit 
    num = num // 10  

if(temp == rev):  
    print(f"{num} is a palindrome number!")  
else:  
    print(f"{num} is not a palindrome number!")
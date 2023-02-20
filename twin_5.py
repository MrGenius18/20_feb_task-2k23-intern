'''
# twin no: 
    123 ==> 1 + 2 + 3 = 6 
            1 * 2 * 3 = 6
'''

no=int(input("Enter Number"))
num=0
mul=1
sum=0
while no!=0:
    num=no%10
    sum=sum+num
    mul=mul*num
    no=no//10
if(sum==mul):
    print("Number is twin")
else:
    print("Number is not twin")
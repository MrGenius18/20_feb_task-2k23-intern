'''
# fibonacci series 
    0 1 1 2 3 5 8 13 ...
'''

num = int(input("Enter The Number :--"))
n1 = 0
n2 = 1
count = 0
for i in range(num):
    if i == 0:
        print(f"fibonacci series-->", 0)
    else:
        n1 = n2
        n2 = count
        count = n1+n2
        print(count,)

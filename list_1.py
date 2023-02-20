'''
  empty list ---->
    take element from user and add it to list....
    list with elements---->
        loops:
            for ==> user know how many data
            while ==> user don't know how many data
'''

list = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
    list.append(ele) # adding the element
      
print(list)

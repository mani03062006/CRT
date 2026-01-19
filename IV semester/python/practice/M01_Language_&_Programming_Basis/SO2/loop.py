'''
while loop:Iterates over a block of code as long as the test expression (condition) is true.
Example:
counter=0
while counter<5:
    print("Hello World")
    counter+=1
    '''
'''Read two integer numbers start and stop variables.
Display all even numbers between start and stop (inclusive).
Input:1 10
Output:2 4 6 8 10

start,stop=map(int,input().split())
while start<=stop:
    if start%2==0:
        print(start,end=" ")
    start+=1

start,stop=map(int,input().split())
while start<=stop:     
    if start%3==0 and start%5==0:
        print("fizzbuzz")
    elif start%3==0:
        print("fizz")
    elif start%5==0:
        print("buzz")  
    else:    
        print(start)    
    start+=

for i in range(0,5,1):
    print("Hello World")

n=int(input())
for i in range(1,n+1,1)::
    print(i)

n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")
    '''
li=[1,5,4,3,6.9]

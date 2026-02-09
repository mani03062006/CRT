'''n=int(input("Enter a number: "))
l=0
while n>0:
    n=n//10
    l=l+1
print(l)
'''
'''
sample input: 1234
sample output: 4

sample input: 123456789
sample output: 9    

'''

'''n=int(input("Enter a number: "))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)
'''
'''
n=int(input("Enter a number: "))
while n>0:
    d=n%10
    n=n//10
    if(d%2==0):
        print(d ,end=" ")
'''
'''
n=int(input("Enter a number: "))
num=0
while n>0:
    d=n%10
    num=num*10+d
    n=n//10
print(num) 
'''

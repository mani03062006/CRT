#sum  of n natural numbers
'''
def Natural_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(Natural_sum(5))
print(Natural_sum(10))

def Natural_Sum1(n):
    if n==1:
        return 1
    else:
        return n+Natural_Sum1(n-1)
print(Natural_Sum1(5))
print(Natural_sum(10))
'''
def fact(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    return pro
print(fact(5))
print(fact(10))

def fact1(n):
    if n<0:
        return "No factorial"
    elif n==0 or n==1:
        return 1
    else:
        return n*fact1(n-1)
print(fact1(5))
print(fact1(10))

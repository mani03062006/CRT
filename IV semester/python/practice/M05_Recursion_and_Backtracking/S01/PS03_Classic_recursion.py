def fibonacci(n):
    if n<=0:
        return "n value is  positive "
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(5))
def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(GCD(4,10))

def GCD1(a,b):
    if b==0:
        return a
    return GCD1(b,a%b)
print(GCD1(4,10))

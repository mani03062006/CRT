'''def linearthmic_time(arr):
    return sorted(arr)
print(linearthmic_time[10,20,30,10,40,60])
'''
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
n=int(input())
print(fibo(n))
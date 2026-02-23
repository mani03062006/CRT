'''
Arithmetic series:
input: 1  2 
output:1 3 5 7 9 11 13 15 17 19

start,d=map(int,input().split())
a=0
for i in range(0,10):
    a=start+i*d
    print(a,end=" ")

start,r=map(int,input().split())
for i in range(0,10):
    a=start*(r**i)
    print(a,end=" ")

n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

n=int(input())
arr=[0,1]
for i in range(2,n):
     arr.append(arr[i-2]+arr[i-1])
print(arr)
'''
n=int(input())
pro=1
if n<0:
    print("No factorial")
elif n==0 or n==1:
    print(i)
else:
    for i in range(1,n+1):
       pro=pro*i
    print(pro)
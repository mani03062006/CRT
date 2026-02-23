'''li=list(map(int,input().split()))
lio=[]
for i in range(len(li)):
    lio.append(li[i]**2)
print(lio)

ans=[i**2 for i in li]
print(ans)

li=list(map(int,input().split()))
ans=[i for i in li if i%2==0]
print(ans)

print("*"*5)
li=['a','b','c']
res=""
for ch in li:
    res=res+ch
print(res)

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    print()
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
    print()

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
    
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
       print(j,end=" ")
    print()
'''
n=int(input())
for i in range(1,n+1):
    if(i<3):
        print(" "*(n-i)+"* "*i,end=" ")
    elif(i>=3):
        
'''for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
else:
    print("loop completed")
'''
p1="abc123"
for i in range(3):
    p2=input()
    if p1==p2:
        print("login successful")
        break
    else:
        print("Account locked")
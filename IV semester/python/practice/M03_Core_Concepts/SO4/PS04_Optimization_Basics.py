'''
check for duplicates in a list
input:[1,2,3,4,5,1]
output:True
input:[1,2,3,4,5]
output:false

def check_dulipcates(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                return True
    return False
li=[1,2,3,4,5,1]
print(check_dulipcates(li))

def check_dulipcates(li):
    s=set(li)
    if len(s)==len(li):
        return False
    else:
        return True
li=[1,2,3,4,5]
print(check_dulipcates(li))

def check_dulipcates(li):
    s=set()
    for ele in li:
        if ele in s:
            return True
        s.add(ele)
    return False
li=[1,2,3,4,5,1]
print(check_dulipcates(li))
'''

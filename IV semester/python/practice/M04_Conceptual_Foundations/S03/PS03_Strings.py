'''
s="python"
print(s[2])
print(s[1:])
print(s.capitalize())
s=s.replace("p","P")
print(s)

s="python"
result=""
stop=-1*(len(s)+1)
for i in range(-1,stop,-1):
    result=result+s[i]
print(result)

si=input()
res=""
for ch in si:
    res=ch+res
print(res)

def reverse_string(st):
    res=""
    for ch in st:
        res=ch+res
    return res
print(reverse_string("abc"))

def is_palindrome(st):
    res=""
    for ch in st:
        res=ch+res
    if st==res:
        return "palindrome"
    else:
        return "not palindrome"
print(is_palindrome("abc"))

def frequency_count(s):
    d={}
    for ch in s:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
    return d

print(frequency_count("abcabc"))

def is_anagrams(st1,st2):
    d={}
    d1={}
    for ch in s:
        if ch not in d:
            d[ch]=
            '''
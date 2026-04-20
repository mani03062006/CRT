def digital_sum(n):
    if n<=9:
        return n
    s=sum([int(ch) for ch in str(n)])
    return digital_sum(s)
print(digital_sum(386))

def sorted_array(nums):
    pass
print(sorted_array([10,20,30,40,50]))
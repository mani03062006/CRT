'''#Sum of array elements
def Array_sum(nums):
    sum=0
    for i in range(len(nums)):
        sum=sum+nums[i]
    return sum
print(Array_sum([1,2,3,4,5]))
#Sum of array elements in recrusive 
def Array_sum1(num,index):
    if index==-1:
        return 0
    return num[index]+Array_sum1(num,index-1)
print(Array_sum1([1,2,3,4,5],4))

#recurive Approach-2
def Array_sum2(nums):
    if len(nums)==0:
        return 0
    return nums[-1]+Array_sum2(nums[:-1])
print(Array_sum2([1,2,3,4,5]))

def reverse_array(nums,i,j):
    if i>=j:
        return nums
    nums[i],nums[j]=nums[j],nums[i]
    return reverse_array(nums,i+1,j-1)
print(reverse_array([1,2,3,4,5],0,4))
'''
def reverse_string(s):
    if len(s)==0:
        return ""
    return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))

def is_palimdrome(s):
    return s==reverse_string(s)
print(is_palimdrome("abba"))
'''def Linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return 1
    return -1
print(Linear_search([12,15,45,67,89,20],15))
print(Linear_search([12,15,45,67,89,20],100))
'''
def Binary_search(nums,target):
    nums.sort()
    low=0
    high=len(nums)-1
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return -1
print(Binary_search([12,15,45,67,89,20],45))

    
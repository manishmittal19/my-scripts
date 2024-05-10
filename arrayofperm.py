def buildArray(nums):
    n = len(nums)
    ans = [0] * n  # Create a new array of size n filled with zeros
    print(ans)
    for i in range(n):
        print(nums[i])
        ans[i] = nums[nums[i]]
        print (ans[i])  # Assign nums[nums[i]] to ans[i]
    return ans
numbers = buildArray([4,5,7,0,1,2,3])
print(numbers)

def sol(nums):
    answer = 0
    pan = 0
    li = [2]
    for i in range(3,1001):
        for j in range(2,i-1):
            if i%j == 0 :
                break
            pan = 1
        if pan == 1:
            li.append(i)
            pan = 0
    
    print(li)
    for i in range(len(nums) - 2):
        for j in range(i+1,len(nums)-1):
            for p in range(j+1,len(nums)):
                temp = nums[i] + nums[j] + nums[p]
                if temp in li:

                    print(temp)
                    answer += 1
    
    return answer

nums = [1,2,3,4]
print(sol(nums))

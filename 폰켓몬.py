def sol(nums):
    answer = 0
    half = len(nums) / 2
    temp_set = set(nums)
    real = list(temp_set)
    leng = len(real)
    if half < leng:
        answer = half
    elif half > leng:
        answer = leng
    else :
        answer = leng
    return int(answer)

nums = [3,3,3,2,2,2]
print(sol(nums))

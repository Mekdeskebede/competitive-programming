n, a, b =  map(int, input().split())
nums = list(map(int, input().split()))

left = 0
curr_sum = 0
ans = 0

for right in range(n):
    curr_sum += nums[right]
    if curr_sum < a:
        continue
    while curr_sum > b and left <= right:
        curr_sum -= nums[left] 
        left += 1
    if a <= curr_sum <= b:
        ans += 1
        temp = curr_sum - nums[left]
        l = left + 1
        while a <= temp <= b:
            ans += 1
            temp -= nums[l]
            l += 1            
print(ans)

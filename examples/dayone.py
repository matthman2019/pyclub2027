n = int(input())
nums = []
for _ in range(n):
    number = int(input())
    nums.append(number)

nums.sort()
print(nums[n // 2])

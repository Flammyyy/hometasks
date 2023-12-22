list = [[], [], [],
        [], [], [],
        [], [], []]
nums = [*range(1, 10)]
for l in list:
        l.append(nums[0])
        nums.pop(0)
print([el for el in list])

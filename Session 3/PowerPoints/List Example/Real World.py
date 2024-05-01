nums = [1,1,1,1,2,2,2]
maj = len(nums)/2
uniques = set(nums)
for e in uniques:
    if nums.count(e) > maj:
        print("Majority is",e)
        break
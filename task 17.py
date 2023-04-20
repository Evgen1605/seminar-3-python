# 17'. Дан список чисел. Определите,
# сколько в нем встречается различных чисел.
# [1, 2, 3, 4, 1, 2, 3]

nums = [1, 2, 3, 4, 1, 2]
print(set(nums))

# кол-во чисел, встречающихся ровно 1 раз

uniq_nums1 = []
for i in nums:
    if nums.count(i) == 1:
        uniq_nums1.append(i)
print(uniq_nums1)

# можно записать короткой записью
uniq_nums = [i for i in nums if nums.count(i) == 1]

print(uniq_nums)

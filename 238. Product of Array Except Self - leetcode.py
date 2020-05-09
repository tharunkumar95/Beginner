import math
# https://leetcode.com/problems/product-of-array-except-self/

nums = [1, 2, 3, 4]
result = []
len_nums = len(nums)
first = None
last = None

for num in range(len_nums):
    # num = 0, 1, 2, 3
    target = num  # target = num = 0
    print(f'target: {target}')
    # if target is the start element, find the prod of elements to right
    if target == 0:
        print(f'inside first: {target}')
        first = math.prod(nums[target + 1:])
        result.append(first)

    # if target is the end element, find the prod of elements to left
    elif target == len_nums - 1:
        print(f'inside last: {target}')
        last = math.prod(nums[:len_nums-1])
        result.append(last)

    # if target not equal to first element or target not equal to last element
    # elif (target != 0) or (target != len_nums - 1):
    else:
        print(f'inside else: {target}')
        # print(f'inside target != 0 or target != len_nums - 1: {target}')
        # if target is the middle element, find the prod of elements left and right of item.
        middle_left = math.prod(nums[:num])
        middle_right = math.prod(nums[num+1:])

        product = middle_left * middle_right
        result.append(product)

print(f'result: {result}')

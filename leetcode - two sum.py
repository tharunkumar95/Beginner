def two_sum(int_arr, target):
    # length of the int_arr
    arr_len = len(int_arr)

    # first for loop
    for item1 in range(arr_len):
        # item1 = 0, 1, 2, 3
        num1 = int_arr[item1]  # num1 = 2
        # step
        step = item1 + 1
        # constraint
        if step != arr_len:
            # second for loop
            for item2 in range(step, arr_len):
                # item2 = 1, 2, 3
                num2 = int_arr[item2]  # num2 = 7
                # compare num1 and num2 with our target
                if num1 + num2 == target:
                    return [item1, item2]


int_arr = [2, 7, 11, 15]
target = 13

# function call
result = two_sum(int_arr, target)
print(result)

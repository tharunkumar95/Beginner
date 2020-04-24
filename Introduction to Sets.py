# Introduction to Sets - HackerRank
def average(array):
    array_list = array
    summation = sum(set(array_list))
    no_of_distinct = len(set(array_list))
    average_array = summation / no_of_distinct
    return average_array


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(list(arr))
    print(result)


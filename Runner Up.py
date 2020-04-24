if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    final_list = list(set(arr_list))
    # [2, 3, 5, 6, 6]
    final_list.sort()
    list_len = len(final_list)
    print(final_list[list_len - 2])
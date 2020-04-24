# Find a string - HackerRank
def count_substring(string, sub_string):
    count = 0
    len_s = len(string)
    len_ss = len(sub_string)
    for cur in range(len_s - 1):
        next_three = cur + len_ss
        three = string[cur:next_three]
        if three == sub_string:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
# String Split and Join - HackerRank

def split_and_join(string):
    str_list = string.split(' ')
    req_str = '-'.join(str_list)
    return req_str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

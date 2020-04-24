# Mutations - HackerRank
# Method 1
# def mutate_string(string, position, character):
#     str_list = list(string)
#     str_list.insert(position, character)
#     req_str = ''
#     for x in str_list:
#         req_str = req_str + x
#     return req_str
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# Method 2
def mutate_string(string, position, character):
    str_list2 = list(string)
    str_list2[position] = character
    req_str = ''.join(str_list2)
    return req_str


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Method 3
# def mutate_string(string, position, character):
#     # abracadabra
#     ind1 = position - 1
#     ind2 = position
#     req_str = string[:ind1] + character + string[position:]
#     return req_str
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
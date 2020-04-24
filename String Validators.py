# String Validators - HackerRank

if __name__ == '__main__':
    string = input()
    alnum_list = []
    alpha_list = []
    digit_list = []
    upper_list = []
    lower_list = []
    for x in string:
        if x.isalnum():
            alnum_list.append(True)
        else:
            alnum_list.append(False)

        if x.isalpha():
            alpha_list.append(True)
        else:
            alpha_list.append(False)

        if x.isdigit():
            digit_list.append(True)
        else:
            digit_list.append(False)

        if x.isupper():
            upper_list.append(True)
        else:
            upper_list.append(False)

        if x.islower():
            lower_list.append(True)
        else:
            lower_list.append(False)


if alnum_list.__contains__(True):
    print(True)
else:
    print(False)

if alpha_list.__contains__(True):
    print(True)
else:
    print(False)

if digit_list.__contains__(True):
    print(True)
else:
    print(False)

if lower_list.__contains__(True):
    print(True)
else:
    print(False)

if upper_list.__contains__(True):
    print(True)
else:
    print(False)


# print(alnum_list)
# print(digit_list)
# print(upper_list)
# print(lower_list)

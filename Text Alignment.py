string = '1 2 3 4  5'
str_list = string.split()
new_list = []
for x in str_list:
    if x[0].isdigit():
        new_list.append(x)
    else:
        new_list.append(x.title())

req_str = ' '.join(new_list)
print(req_str)

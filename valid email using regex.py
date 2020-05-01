import re

# '^' - startswith
# '$' - endswith
# '^' and '$' are metacharacters, these are interpreted in a different way by the RegEx engine - "[].^$*+?{}()\|"
# pattern = '^a...s$'
# pattern = '[^0-9]'   # [a-p] is same as [abcdefghijklmnop]
# pattern = '..'  # any single character

# '\' is used to escape the escape character

pattern = "[\w]*@[\w]*.[\w]+.[\w]+"

email_list = ['tharunkumar_s@yahoo.co.in', 'tharunkumar_s@outlook.com',
              'mesimerisertharun@gmail.com', 'tharun@gmx.com', 'tharunkumar95gmail.com']

valid_email = []

print('the below are the valid email addresses,')
for email in email_list:
    result = re.findall(pattern, email)
    if len(result) != 0:
        for valid in result:
            valid_email.append(valid)


enum = enumerate(valid_email, start=1)
for x in enum:
    print(x)
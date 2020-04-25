stk_dict = {'username': 'tharunkumar95', 'website': 'github', 'online': True}
# Print only the 'Keys'
# print(stk_dict.keys())

# Print only the 'Values'
# print(stk_dict.values())

# Returns items in list format of (Key, Value) tuple pairs
# print(stk_dict.items())

# Prints the 'stk_dict'
# print(stk_dict)

# Iterating the 'stk_dict'
# for k,v in stk_dict.items():
#     print(k, v)

# To add/modify elements in Dictionary use either 'dict[key] = value' or 'dict.update({key: value})'
# stk_dict['website'] = 'Bitbucket'
# stk_dict.update({'online': False})
# print(stk_dict)

# To remove a key-value pair
del stk_dict['online']
print(stk_dict)

# Deletes all the key-value entries
stk_dict.clear()
print(stk_dict)

# Deletes the entire dictionary
del stk_dict
print(stk_dict)

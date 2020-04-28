file_loc = 'C:\\Users\\tharu\\OneDrive\\Desktop\\My Carrer\\core python - 3.8.txt'
mode = 'r'
file_obj = open(file_loc, mode)

open_file = file_obj.read()

flag = False
if open_file.__contains__('good'):
    flag = True

else:
    None

if flag:
    print('Good Document')

else:
    print('Bad Document')
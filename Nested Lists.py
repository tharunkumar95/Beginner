# Nested Lists - HackerRank

if __name__ == '__main__':
    name_list = []
    score_list = []
    index_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # add the names to the 'name_list'
        name_list.insert(_, name)
        # add the scores to the 'score_list'
        score_list.insert(_, score)

    # sort the 'score_list' and store in new list 'sorted_score_list'
    sorted_score_list = sorted(score_list)

    # find the second lowest score from 'score_list'
    second_lowest = sorted_score_list[1]

    # find the index of all students with 'second_lowest' score
    get_index = []
    for x in range(len(score_list)):
        if score_list[x] == second_lowest:
            get_index.append(x)

    # find the names of the students with 'second_lowest' score
    get_name = []
    for y in get_index:
        get_name.append(name_list[y])

    # sort the names of the students with 'second_lowest' score in asending order
    # print the names of the students
    get_name.sort()
    for stud_name in get_name:
        print(stud_name)
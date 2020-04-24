# Finding the percentage - HackerRank

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # store the scores of the student in 'average_list'
    average_list = student_marks[query_name]

    # sum of all the elements of the list
    summation = sum(average_list)

    # total number of elements in the list
    total = len(average_list)
    total_float = float(total)

    # average = sum of all the elements / total number of elements
    average = summation / total

    # format to two decimal places
    formatted_average = '{:.2f}'.format(average)

    # print the average
    print(formatted_average)


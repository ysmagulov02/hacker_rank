if __name__ == '__main__':
    # inserting each student and their score in the student list
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    # print(students)

    # bubble sort
    def Sort(sub_li):
        l = len(sub_li)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (sub_li[j][1] > sub_li[j + 1][1]):
                    tempo = sub_li[j]
                    sub_li[j]= sub_li[j + 1]
                    sub_li[j + 1]= tempo
        return sub_li

    Sort(students)
    # print(Sort(students))


    # list of people of everyone but people with lowest score(s)
    output_list = []
    for i in students:
        if i[1] != students[0][1]:
            output_list.append(i)
    # print(output_list)
    
    # list of people with second lowest scores
    result = []
    for i in output_list:
        lowest = output_list[0][1]
        if i[1] == lowest:
            result.append(i)
    # print(result)
    result.sort()
    # print(result)

    # final output for names
    for i in result:
        print(i[0])





    
        
        


    

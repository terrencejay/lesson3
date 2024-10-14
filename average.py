def classave():

    grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
    total = sum(grades)
    average = total/len(grades)
    print(f'The class average is {average}')
    descending=sorted(grades, reverse=True)
    print (descending)
classave()
grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny' , 'Billbo' , 'Steve' , 'Khendrik','Aaron'}
lst = list(students)
res = lst.sort()


average = sum(grades[0]) /len(grades[0])
average_1 = sum(grades[1])/len(grades[1])
average_2 = sum(grades[2])/len(grades[2])
average_3 = sum(grades[3])/len(grades[3])
average_4 = sum(grades[4])/len(grades[4])

grades_1 = [average , average_1 , average_2 , average_3, average_4]



dictionary = {}
for i in range(len(lst)):
   dictionary[lst[i]] = grades_1[i]
print(dictionary)
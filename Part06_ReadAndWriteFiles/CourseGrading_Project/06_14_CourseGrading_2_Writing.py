# Part 1-5
if True:  # change to False when testing
    """"For test: hidden in the False branch of an if statement. It will never be executed."""
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information:")
else:  
    # now this is the False branch, and is never executed
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
    course_info = "course1.txt"
print('Results written to files results.txt and results.csv')


"""1. reads the files, and then prints out the total number of exercises completed by each student."""
name = {}
with open (student_info) as studentInfoFile:
    for line in studentInfoFile:
        line = line.strip()
        part = line.split(';')
        if part[0] == 'id':
            continue
        name[part[0]] = (part[1],part[2])

excercises = {}
with open (exercise_data) as exerciseFile:
    for line in exerciseFile:
        complete_list = []

        line = line.strip()
        part = line.split(';')
        if part[0] == 'id':
            continue

        # 转化为int
        for num in range(1, len(part)):
            complete_list.append(int(part[num]))

        excercises[part[0]] = complete_list



"""2. Aim: The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student."""
points = {}
with open (exam_points) as points_file:
    for line in points_file:
        line = line.strip()
        part = line.split(';') #list
        if part[0] == 'id':
            continue

        points_list = []
        for item in part[1:]:
            points_list.append(int(item))

        points[part[0]] = points_list
# print(points)

def scale(points:float):
    if 0 <= points < 15: 
        return 0
    elif 15 <= points < 18: 
        return 1
    elif 18 <= points < 21: 
        return 2
    elif 21 <= points < 24: 
        return 3
    elif 24 <= points < 28: 
        return 4
    else:
        return 5



'''4. add a file containing information about the course.'''
course_credit = [] # [Introduction to Programming, 5]
with open (course_info) as course_file:
    for line in course_file:
        part = line.split(':')
        course_credit.append(part[1].strip())
# print(course_credit)


'''3. print out some statistics based on the CSV files:
    Each row contains the information for a single student. 
    The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. 
    The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.'''

print_sheet = {('name',''): ['exec_nbr', 'exec_pts.', 'exm_pts.', 'tot_pts.', 'grade','person_id']}

for key, value in name.items(): # person
    person_id = key
    if key in points:
        points_sum = sum(points[key])
        excercises_sum = sum(excercises[key])

        total = points_sum + excercises_sum * (10/40) # Completing all 40 exercises awards 10 points
        # print(total)
        grade = scale(total) 
        # print(f'{value[0]} {value[1]} {grade}')

        # coloum names
        exec_nbr = excercises_sum
        exec_pts = int(excercises_sum * (10/40))
        exm_pts = points_sum
        tot_pts = int(total)
        full_name = name[key] # tuple

        print_sheet[(full_name)]=[exec_nbr, exec_pts, exm_pts, tot_pts, grade,person_id]
# print(print_sheet)

# # print a table --放在后面csv里了
# for key, value in print_sheet.items():
#     full_name = f"{key[0]} {key[1]}"
#     print(f'{full_name:<30}{value[0]:<10}{value[1]:<10}{value[2]:<10}{value[3]:<10}{value[4]:<10}')


'''5. The program should then create two files. 
a. There should be a file called results.txt: The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.
b. Additionally, there should be a file called results.csv with format of: 12345678;pekka peloton;0'''
with open('results.txt', 'w') as result_file:
    header = f'{course_credit[0]}, {course_credit[1]} credits'
    dividor = len(header)*'='
    result_file.write(f'{header}\n')
    result_file.write(f'{dividor}\n')
    for key, value in print_sheet.items():
        full_name = f"{key[0]} {key[1]}"
        result_file.write(f'{full_name:<30}{value[0]:<10}{value[1]:<10}{value[2]:<10}{value[3]:<10}{value[4]:<10}\n')


with open('results.csv','w') as csv_file:
    for key, value in print_sheet.items():
        if key[0] == 'name': # header
            continue
        person_id = value[-1] 
        first_name = key[0]
        last_name = key[1]
        grade = value[-2]
        # print(f'{person_id};{first_name} {last_name};{grade}')

        csv_file.write(f'{person_id};{first_name} {last_name};{grade}\n')

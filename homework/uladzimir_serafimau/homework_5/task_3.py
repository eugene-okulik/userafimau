students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_list = ', '.join(students)
subjects_list = ', '.join(subjects)

result = f'Students {students_list} study these subjects: {subjects_list}'
print(result)

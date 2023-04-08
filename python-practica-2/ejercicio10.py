names = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

marks_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

marks_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


def create_list_from_string(names_string):
    """This function receives a concatenation of quoted student names, separated by 
    commas, in the form of a single string. It returns a list of those names."""

    names_list = names_string.split(",")
    modified_names_list = list(
        map(lambda name: name.strip("', \n"), names_list))
    return modified_names_list


def generate_dictionary(names, marks_1, marks_2):
    """This function generates a dictionary from three lists ordered in such a way 
    that the elements in the same position correspond to the same student. Each 
    dictionary key is a student name taken from the first parameter of the function. 
    Each dictionary value is a list o two marks of that same student, taken from 
    the second and third parameters, respectively."""

    students_marks_dicc = {name: [mark_1, mark_2]
                           for name, mark_1, mark_2
                           in zip(names, marks_1, marks_2)}
    return students_marks_dicc


def calculate_student_average(student_marks_dicc):
    """This function receives a dictionary with student names as keys and their 
    marks as values. It returns a new dictionary with each student name as key and 
    the average of their marks as value."""

    students_avg = {name: sum(marks)/len(marks)
                    for name, marks
                    in student_marks_dicc.items()
                    if len(marks) > 0}
    return students_avg


def calculate_general_average(student_marks_dicc):
    """This function receives a dictionary with student names as keys and their 
    marks as values. It returns the general average of the course."""

    students_avg = calculate_student_average(student_marks_dicc)
    return round(sum(students_avg.values()) / len(students_avg)
                 if len(students_avg) > 0
                 else 0, 2)


def highest_avg_student(student_marks_dicc):
    """This function receives a dictionary with student names as keys and their 
    marks as values. It returns the name of the student with the highest mark 
    average."""

    students_avg = calculate_student_average(student_marks_dicc)
    return max(students_avg.items(), key=lambda x: x[1])[0]


def lowest_mark_std(student_marks_dicc):
    """This function receives a dictionary with student names as keys and their 
    marks as values. It returns the name of the student with the lowest mark."""

    return min(student_marks_dicc.items(), key=lambda x: x[1])[0]


# Clause A:
student_marks_dicc = generate_dictionary(
    create_list_from_string(names),
    marks_1,
    marks_2
)
print(f"Clause A resolution: \n {student_marks_dicc} \n")

# Clause B:
student_marks_average = calculate_student_average(student_marks_dicc)
print(f"Clause B resolution: \n {student_marks_average} \n")

# Clause C:
students_general_average = calculate_general_average(student_marks_dicc)
print(
    f"Clause C resolution: \nThe general average of the class is: {students_general_average} \n")

# Clause D:
highest_average_student = highest_avg_student(student_marks_dicc)
print(
    f"Clause D resolution: \nThe student with the highest average is: {highest_average_student} \n")

# Clause E:
lowest_mark_student = lowest_mark_std(student_marks_dicc)
print(
    f"Clause E resolution: \nThe student with the lowest mark is: {lowest_mark_student} \n")

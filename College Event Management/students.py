def add_student(student_list, name):
    if name not in student_list:
        student_list.append(name)

def remove_student(student_list, name):
    if name in student_list:
        student_list.remove(name)

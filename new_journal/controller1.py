import model1
import view1

def start():
    global journal1
    global _class_1
    user_input=0
    _class_1=view1.open_class()
    journal1=model1.open_journal(_class_1)
    while user_input != 6:
        user_input=view1.main_menu()
        match user_input:
            case 1:
                view1.show_journal(journal1,_class_1)
            case 2:
                subject_num=view1.open_subject(journal1,_class_1)
                view1.show_subject(journal1,_class_1,subject_num)
            case 3:
                student_num=view1.open_student(journal1,_class_1)
                view1.show_student(journal1,_class_1,student_num)
            case 4:
                subject_num=view1.open_subject(journal1,_class_1)
                student_num=view1.open_student(journal1,_class_1)
                view1.show_subject_student(journal1,_class_1,subject_num,student_num)
            case 5:
                subject_num=view1.open_subject(journal1,_class_1)
                student_num=view1.open_student(journal1,_class_1)
                view1.show_subject_student(journal1,_class_1,subject_num,student_num)
                bal=view1.Get_bal()
                model1.append_bal(journal1,subject_num,student_num,bal)
                view1.show_subject_student(journal1,_class_1,subject_num,student_num)
    model1.save_journal(_class_1)







# def start():
#     num_class = 0
#     while num_class != "":
#         num_class = view1.open_class()
#         if num_class != "":
#             new_num_class=num_class
#             journal1 = model1.open_journal1(num_class)
#             if journal1 != "":
#                 subject = 0
#                 while subject != "":
#                     view1.show_subject(journal1)
#                     subject = view1.open_subject()
#                     if subject != "":
#                         student = 0
#                         while student != "":
#                             view1.show_students(journal1, subject)
#                             student = view1.open_student()
#                             if student != "":
#                                 view1.performance_student(student)
#                                 view1.new_bal(journal1, subject, student)
#                                 bal = 0
#                                 while bal != "":
#                                     bal = view1.estimate()
#                                     if bal != "":
#                                         model1.append_bal(journal1, subject, student, bal)
#                                         view1.performance_student(student)
#                                         view1.new_bal(journal1, subject, student)

    # model1.save_journal1(new_num_class)

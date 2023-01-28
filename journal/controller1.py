import model1
import view1


def start():
    num_class = 0
    while num_class != "":
        num_class = view1.open_class()
        if num_class != "":
            new_num_class=num_class
            journal = model1.open_journal(num_class)
            if journal != "":
                subject = 0
                while subject != "":
                    view1.show_subject(journal)
                    subject = view1.open_subject()
                    if subject != "":
                        student = 0
                        while student != "":
                            view1.show_students(journal, subject)
                            student = view1.open_student()
                            if student != "":
                                view1.performance_student(student)
                                view1.new_bal(journal, subject, student)
                                bal = 0
                                while bal != "":
                                    bal = view1.estimate()
                                    if bal != "":
                                        model1.append_bal(journal, subject, student, bal)
                                        view1.performance_student(student)
                                        view1.new_bal(journal, subject, student)

    model1.save_journal(new_num_class)

students = []
passed = 0
failed = 0

while True:
    name = input("Enter Student Name: ")
    q1 = input("Enter Grade in Quiz #1: ")
    q2 = input("Enter Grade in Quiz #2: ")
    q3 = input("Enter Grade in Quiz #3: ")
    cp = input("Enter Grade in Class Participation: ")
    fExam = input("Enter Grade in Final Exam: ")

    qTotal = (float(q1) + float(q2) + float(q3)) / 3
    grade = (float(qTotal) * .40) + (float(cp) * .20) + (float(fExam) * .40)

    if int(grade) >= 75:
        status = "Passed"
        passed = passed + 1

    elif int(grade) < 75:
        status = "Failed"
        failed = failed + 1

    students.append(f"{'{:<30}'.format(name)} {'{:<5}'.format(q1)} {'{:<5}'.format(q2)} {'{:<5}'.format(q3)} {'{:<5}'.format(cp)} {'{:<12}'.format(fExam)} {'{:<10}'.format(int(grade))} {status}")

    choice = input("Do you want to enter new student record? [yes/no] ".lower())
    if choice == "yes":
        continue
    elif choice == "no":
        print()
        print(f"{'{:<30}'.format('Name')} {'{:<5}'.format('Q1')} {'{:<5}'.format('Q2')} {'{:<5}'.format('Q3')} {'{:<5}'.format('CP')} {'{:<12}'.format('Final Exam')} {'{:<10}'.format('Grade')} Status")
        for index, student in enumerate(students):
            print(student)
        print()
        print(f"Total Number of Students Passed: {passed}")
        print(f"Total Number of Students Failed: {failed}")

        break
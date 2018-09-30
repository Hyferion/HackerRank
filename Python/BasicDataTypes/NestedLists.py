if __name__ == '__main__':

    def secondlow(students):
        studentss = []
        grades = [student[1] for student in students]
        grades = set(grades)
        seclow_grade = sorted(grades)[1]
        for student in students:
            if student[1] == seclow_grade:
                studentss.append(student[0])
        return studentss


    students = [[input(), float(input())] for _ in range(int(input()))]
    for i in sorted(secondlow(students)):
        print(i)
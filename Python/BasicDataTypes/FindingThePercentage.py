# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    studentmarks = student_marks[query_name]
    studentmarks = student_marks[query_name]
    print("{0:.2f}".format(sum(studentmarks) / studentmarks.__len__()))

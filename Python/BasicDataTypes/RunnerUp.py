# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    secondmax = None
    max = max(arr)
    for a in arr:
        if a != max:
            if secondmax == None:
                secondmax = a
            if a > secondmax:
                secondmax = a
    print(secondmax)
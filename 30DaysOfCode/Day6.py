if __name__ == '__main__':
    t = int(input())
    string = []
    for st in range(t):
        string.append(input())

    for str in string:
        even = ''
        uneven = ''
        for index,char in enumerate(str):
            if index % 2 != 0:
                uneven = uneven + char
            else:
                even = even + char
        print(even + " " + uneven)
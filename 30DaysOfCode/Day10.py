if __name__ == '__main__':
    n = int(input())
    count = 0
    counts = []
    remainder = 0
    while n > 0:
        if remainder == 1:
            count = count + 1
            counts.append(count)
            if n == 1:
                count = count + 1
                counts.append(count)
        else:
            count = 0
        remainder = int(n % 2)
        n = int(n / 2)
    print(max(counts))

arr = [['red', 'black', 'green'], ['red', 'blue', 'black']]

bestcount = 0
liste = []

for i in arr:
    for k in i:
        if sum(x.count(k) for x in arr) >= bestcount:
            bestcount = sum(x.count(k) for x in arr)
            liste.append(k)

print(list(set(liste)))

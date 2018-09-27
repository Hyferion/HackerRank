x = 1
y = 1
z = 1
n = 2

x = [[xx, yy, zz] for xx in range(x + 1) for yy in range(y + 1) for zz in range(z + 1) if ((xx + yy + zz) != n)]

print(x)

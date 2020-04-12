# 方案一
n = 0
while n < 9:
    print("*" * (n + 1))
    n += 1
# 方案二
n = 1
while n < 10:
    i = n
    while i > 0:
        print("*", end='')
        i -= 1
    print()
    n += 1
# 方案三
row = 1
while row < 10:
    col = 0
    while col < row:
        col += 1
        print("%d * %d = %3d" % (col, row, col * row), end=" , ")
    print()
    row += 1
# 方案四
# 方案三
row = 1
while row < 10:
    col = 0
    while col < row:
        col += 1
        print("%d * %d = %d" % (col, row, col * row), end="\t")
    print()
    row += 1
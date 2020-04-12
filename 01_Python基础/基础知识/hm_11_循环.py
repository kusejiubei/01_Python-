i = 0
sum = 0
number = 100
while i < number:
    print("hello python %d" % i)
    if i % 2 == 0:
        if i == 80:
            print("哈哈 continue %d" % i)
            i += 2
            continue
        sum += i
    if i // 3 == 33:
        print("哈哈 breck %d" % i)
        break
    i += 1
print("%d 以内的偶数之和为： %d" % (number, sum))
while i > 0:
    print("一级循环 %d" % i)
    while i > 10:
        print("二级循环 %d" % i)
        i -= 1
    i -= 3
    print("二级循环end")

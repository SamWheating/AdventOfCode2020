last = 0
for i in range(100000):
    if (i-102)%221 == 0 and (i+3) % 19 == 0:
        print(i, i - last)
        last = i
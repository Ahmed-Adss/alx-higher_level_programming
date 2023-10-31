#!/usr/bin/python3
for i in range(0, 10):
    for l in range(i, 10):
        if i == l or (i == 8 and l == 9):
            continue
        print("{:d}{:d}".format(i, l), end=" ,")
print("{:d}{:d}".format(8, 9))

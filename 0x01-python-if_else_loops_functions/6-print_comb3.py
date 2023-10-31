#!/usr/bin/python3
for i in range(0, 10):
    for w in range(i, 10):
        if i == w or (i == 8 and w == 9):
            continue
        print("{:d}{:d}".format(i, w), end=", ")
print("{:d}{:d}".format(8, 9))

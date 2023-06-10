import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=200) 

drawing = np.zeros((6, 40), dtype = str)
drawing[:] = "."
cycle = 1
register = 1
crt = [0, 0]
file = open ("input.txt")

def increment_crt(crt):
    if crt[0] <= 39:
        crt[0] += 1

    else:
        crt[0] = 1
        crt[1] += 1
    return crt

for line in file:

    if line[0] == "n":
        cycle += 1
        if crt[0] == register or crt[0] == register + 1 or crt[0] == register - 1:
            drawing[crt[1], crt[0]] = "#"
        crt = increment_crt(crt)

    if line[0] == "a":
        cycle += 1
        if crt[0] == register or crt[0] == register + 1 or crt[0] == register - 1:
            drawing[crt[1], crt[0]] = "#"
        crt = increment_crt(crt)
        cycle += 1
        if crt[0] == register or crt[0] == register + 1 or crt[0] == register - 1:
            drawing[crt[1], crt[0]] = "#"
        crt = increment_crt(crt)
        register += int(line[5:])

for i in range (0, 6):
    print(drawing[i])

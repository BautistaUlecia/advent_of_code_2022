def main():
    acum=0
    with open ("input.txt") as file:
        for x in file:
            acum+=score(x)
        print(acum)

def score(x):
    sum = 0
    if x[0] == 'A':
        if x[2] == 'X':
            sum += 4
        elif x[2]=='Y':
            sum += 8
        elif x[2]=='Z':
            sum += 3
    elif x[0] == 'B':
        if x[2] =='X':
            sum += 1
        elif x[2] == 'Y':
            sum += 5
        elif x[2] == 'Z':
            sum += 9
    elif x[0] == 'C':
        if x[2] == 'X':
            sum += 7
        elif x[2] == 'Y':
            sum += 2
        elif x[2] == 'Z':
            sum += 6
    return sum

main()
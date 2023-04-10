def main():
    acum=0
    with open ("input.txt") as file:
        for x in file:
            acum+=score(x)
        print(acum)

def score(x):
    sum = 0
    #Tengo que ganar perder o empatar segun x[2]
    #Si x[2] es X pierdo, Y empato, Z gano
    #Segun lo que elija calculo puntaje de la misma forma
    #WIN: 6 | EMPATE: 3 | DERROTA: 0 | PIEDRA: 1 | PAPEL: 2 | TIJERA: 3

    enemy = x[0]
    my_move = x[2]

    if enemy == 'A':
        if my_move == 'X':
            sum += 3
        elif my_move == 'Y':
            sum += 4
        elif my_move == 'Z':
            sum += 8
    elif enemy == 'B':
        if my_move == 'X':
            sum+=1
        elif my_move == 'Y':
            sum+=5
        elif my_move == 'Z':
            sum+=9
    elif enemy == 'C':
        if my_move == 'X':
            sum+=2
        elif my_move =='Y':
            sum += 6
        elif my_move == 'Z':
            sum += 7

    return sum

main()
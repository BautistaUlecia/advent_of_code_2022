def main():
    # Lista con n caracteres marco inicio y final de la secuencia evaluo si alguno se repite. si lo hacen, aumento inicio y final
    # Evaluo de nuevo hasta que ninguno se repita, en ese caso devuelvo la posicion del final de la secuencia.

    with open ("input.txt") as file:
        for x in file:
            string = x

    mylist = []
    start = 0
    end = 14
    count = 0

    for x in range (len(string)):
        sequence = string[start:end]
        mylist = []
        count = 0


        for x in sequence:
            mylist.append(x)

        for c in sequence:
            count += mylist.count(c)

        if count == 14:
            print(end)
            return
        else:
            start += 1
            end += 1



main()
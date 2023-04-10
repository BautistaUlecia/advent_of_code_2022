def main():
    count = 0
    with open ("input.txt") as file:
        for x in file:
            if (included(x)==True):
                count += 1
        print (count)


def included(x):
    bounds_list=[]
    val=''
    for c in x:
        if c != '-' and c != ',' and c!='\n':
            val += c
        else:
            bounds_list.append(int(val))
            val=''
    print(bounds_list)
    # Casos en los que no overlappea:
    # minimo del segundo es mayor que maximo del primero
    # maximo del segundo es menor que minimo del primero

    if bounds_list[2] > bounds_list[1]:
        return False
    elif bounds_list[3] < bounds_list[0]:
        return False
    else:
        return True

main()


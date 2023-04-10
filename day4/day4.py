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
    #first pair contains second pair
    if bounds_list[0] <= bounds_list[2] and bounds_list[1] >= bounds_list[3]:
        return True
    #second pair contains first pair
    elif bounds_list[2] <= bounds_list[0] and bounds_list[3] >= bounds_list[1]:
        return True
    else:
        return False

main()

def main():
    sum = 0
    mylist=[]
    count=0
    result=[]
    with open ("input.txt") as file:
        for x in file:

            mylist.append(x)
            count+1

            if len(mylist) == 3:
                sum+=(convert(value(mylist)))
                count=0
                mylist = []
    print(sum)
                


def value(mylist):
    for x in mylist[0]:
        for y in mylist[1]:
            for z in mylist[2]:
                if x in y and x in z:
                    return x


def convert(x):
    x = ord(x)
    if x < 97:
        x = x - 65 + 27
    elif x > 97 :
        x = x - 97 + 1
    return x

main()

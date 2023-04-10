def main():
    sum=0
    max=0
    sums=[]
    with open ("day1input.txt") as file:
        for x in file:
            if x!='\n':
                sum+=int(x)
            else:
                sums.append(sum)
                sum=0
                
    sums.sort(reverse=True)
    print (sums[0]+sums[1]+sums[2])

main()

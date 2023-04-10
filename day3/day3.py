#divido string en dos substrings del mismo largo comparo caracter por caracter
#moviendome sobre el primero si encuentro un match lo anoto
#creo que si hago valor ascii de la letra menos valor ascii de 'a' o 'A' +1 me da la prioridad
def main():
    sum = 0
    with open ("input.txt") as file:
        for x in file:
            sum += value(x)
    print(sum)

def value(x):
    value = 0
    first_half = x[:len(x)//2]
    second_half = x[len(x)//2:]

    for x in first_half:
        if x in second_half:
            value = ord(x)
            if value < 97:
                value = value - 65 + 27
            elif value > 97 :
                value = value - 97 + 1
    return value

main()
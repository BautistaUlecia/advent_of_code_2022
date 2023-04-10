#Tengo que crear un stack para cada uno de los numeritos
#Y leer el archivo haciendo operaciones (puedo usar la funcion que use en el programa pasado, que leia recortando)

# Ejemplo operacion
# move 1 from 2 to 1
# move 3 from 1 to 3

# Podria llamar al numero despues de move como "n", a la primer pila "a" y a la segunda "b"

def main():
    n=0
    with open("input.txt") as file:
        for x in file:
            n = len(x)
            break

    print(n)
    stacks=[]
    for i in range (1, n, 4):
        stacks.append(load(i))
    #print(stacks)
    move_stack(stacks)



def load(i):
    string = ''
    with open("input.txt") as file:
        for x in file:
            if '1' not in x:
                string += x[i]

            else:
                return string[::-1].strip()

# En este punto tengo stacks cargado con las cajas que hay en cada pila (XD)
# Usar strip para leer los strings de las instrucciones y guardar al numero despues de move como "n", a la primer pila "a" y a la segunda "b"

def move(stacks):
    instructions=[]
    instructions_list=[]
    with open("input.txt") as file:
        for x in file:
            if 'move' in x:
                instructions.append(''.join (a for a in x if a.isdigit() or a == ' '))

    instructions = [e[1:] for e in instructions]
    #print(instructions)

    for x in instructions:
        ins = list(filter(None, x.split(' ')))
        n = int(ins[0])
        a = int(ins[1])
        b = int(ins[2])

        for q in range (n):
            a_list = list(stacks[a-1])
            removed = a_list.pop()
            b_list = list(stacks[b-1])
            b_list.append(removed)

            stacks[a-1] = a_list
            stacks[b-1] = b_list

    print(stacks)

def move_stack(stacks):
    instructions=[]
    removed=''
    instructions_list=[]
    with open("input.txt") as file:
        for x in file:
            if 'move' in x:
                instructions.append(''.join (a for a in x if a.isdigit() or a == ' '))

    instructions = [e[1:] for e in instructions]
    #print(instructions)

    for x in instructions:
        removed=''
        ins = list(filter(None, x.split(' ')))
        n = int(ins[0])
        a = int(ins[1])
        b = int(ins[2])
        
        a_list = list(stacks[a-1])
        b_list = list(stacks[b-1])


        for q in range (n):
            if len(a_list) >= 0:
                removed+=a_list.pop()
        
        removed=list(removed)
        removed.reverse()
        m = len(removed)
        

        for k in range (m):
            b_list.append(removed[k])


        stacks[a-1] = a_list
        stacks[b-1] = b_list

    print(stacks)
    [print (stack[-1], end="") for stack in stacks]
        
main()
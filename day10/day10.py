# trackear ciclo y fuerza actual de la señal (register). 
# leo input, si veo noop ciclo +1 // si veo addx ciclo +1 ciclo +1 señal + numero que lei. 
# para cada operacion chequeo que mi ciclo no sea igual a 20 60 100 140 180 o 220. si es, calculo y sumo a total final

cycle = 1
register = 1
result = 0
file = open ("input.txt")
relevant_cycles = [20, 60, 100, 140, 180, 220]


for line in file:

    print(f"cycle = {cycle}")
    print(f"register = {register}")


    if line[0] == "n":

        if cycle in relevant_cycles:
            result += cycle * register

        cycle += 1



    if line[0] == "a":
        if cycle in relevant_cycles:
            result += cycle * register

        cycle += 1

        if cycle in relevant_cycles:
            result += cycle * register

        cycle += 1

        register += int(line[5:])

print(result)
        

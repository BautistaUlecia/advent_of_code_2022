# Had to rewrite the whole solution, turns out my approach was not really usable for part 2
values = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}

def rope(length):
    knots = [[0, 0] for _ in range(length)]
    visited = set()
    visited.add((0,0))

    with open("input.txt") as file:
        for line in file:
            direction = line[0]
            steps = int(line[2:])
            for x in range(steps):
                knots[0][0] += values[direction][0]
                knots[0][1] += values[direction][1]
                for i in range(1, len(knots)):
                    current_x, current_y = knots[i-1][0] - knots[i][0], knots[i-1][1] - knots[i][1]
                    if max(abs(current_x), abs(current_y)) > 1:
                        knots[i][0] += (1 if current_x > 0 else 0 if current_x == 0  else -1)
                        knots[i][1] += (1 if current_y > 0 else 0 if current_y == 0 else -1)
                visited.add(tuple(knots[-1]))
        return len(visited)

print(rope(10))
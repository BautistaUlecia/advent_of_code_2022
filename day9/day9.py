import numpy as np
rows = cols = 1000

def main():

    # Im sure there is a way to not hardcode the size of the matrix. 
    # Still, it works well and i got an idea of how the original Snake game was made (i think? :P)

    # My approach was to declare a boolean matrix and flip to 1 if tail passes through

    grid = np.zeros((rows, cols), dtype=int)

    # Start in the middle of the matrix so any direction of movement is valid
    head_position = {"x": int(rows/2), "y": int(cols/2)}
    tail_position = {"x": int(rows/2), "y": int(cols/2)}

    with open ("input.txt") as file:
        for line in file:
            # Parse input: first char is direction, then space (ignore it), then number of steps
            direction = line[0]
            steps = int(line[2:])
            move(direction, steps, head_position, tail_position, grid)
            
        # Part 1 answer
        print(count_ones(grid))

def move(direction, steps, head_position, tail_position, grid):
    for x in range (0, steps):
        # Flip original tail position in boolean matrix
        grid[tail_position["x"]][tail_position["y"]] = 1

        # Move head, if head and tail are not touching, move tail
        head_position = move_head(direction, head_position)
        if touching(head_position, tail_position) == False:
            tail_position = move_tail(head_position, tail_position)
            # Flip tail position in boolean matrix
            grid[tail_position["x"]][tail_position["y"]] = 1



def move_head(direction, head_position):
    # Self explanatory
    if direction == "R":
        head_position["y"] += 1
    if direction == "L":
        head_position["y"] -= 1
    if direction == "U":
        head_position["x"] -= 1
    if direction == "D":
        head_position["x"] += 1
    return head_position


def touching(head_position, tail_position):
    # Use absolutes to check if tail and head are touching
    if abs(head_position["y"] - tail_position["y"]) <= 1 and abs(head_position["x"] - tail_position["x"]) <= 1:
        return True  
    return False

def move_tail(head_position, tail_position):
    # Store distance between tail and head x and y
    offset = {"x": 0, "y": 0}
    offset["y"] = head_position["y"] - tail_position["y"]
    offset["x"] = head_position["x"] - tail_position["x"]

    if offset["x"] == 0:
        if offset["y"] > 0:
            # If same x and positive y difference, tail position should be x, y - 1 of head position
            tail_position["y"] = head_position["y"] - 1
        else:
            # Same x negative y difference, tail should be x, y + 1
            tail_position["y"] = head_position["y"] + 1
        return tail_position
    
    if offset["y"] == 0:
        # Same as above but checking y axis
        if offset["x"] > 0:
            tail_position["x"] = head_position["x"] - 1
        else:
            tail_position["x"] = head_position["x"] + 1
        return tail_position
    
    # Same as above but for diagonal differences (if here, offset y and offset x are NOT zero)
    if abs(offset["y"]) > abs(offset["x"]):
        if offset["y"] > 0:
            tail_position["x"] = head_position["x"] 
            tail_position["y"] = head_position["y"] - 1
        else:
            tail_position["x"] = head_position["x"] 
            tail_position["y"] = head_position["y"] + 1

        return tail_position
    
    if abs(offset["x"]) > abs(offset["y"]):
        if offset["x"] > 0:
            tail_position["x"] = head_position["x"] - 1
            tail_position["y"] = head_position["y"] 
        else:
            tail_position["x"] = head_position["x"] + 1
            tail_position["y"] = head_position["y"] 
    
        return tail_position
    
def count_ones(grid):
    count = 0
    for x in range (rows):
        for y in range (cols):
            if grid[x][y] == 1:
                count +=1
    return count

main()
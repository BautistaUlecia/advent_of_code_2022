import numpy as np

matrix = np.genfromtxt("input.txt", dtype=int, delimiter=1)
rows, columns = matrix.shape


def main():
    visible_trees = 0
    max_score = 0

    # iterate through inner matrix (matrix except edges)
    for x in range (1, rows -1):
        for y in range (1, columns -1):

            # If visible from any direction, tree is visible
            if visible_bottom(x, y) or visible_left(x, y) or visible_right(x, y) or visible_top(x, y):
                visible_trees+=1

            # Count "scenic score" of current tree, store max
            score = count_bottom(x, y) * count_left(x, y) * count_right(x, y) * count_top(x, y)
            if score > max_score:
                max_score = score

    # All trees on edges are visible from outside the matrix so calculate them and add them to the inner visible ones
    edge_trees = rows * 2 + (columns - 2) * 2
    print (visible_trees + edge_trees) # part 1
    print(max_score) # part 2


# Functions are pretty self explainatory, iterate through matrix in a number of different ways comparing current to others to find out what is asked.

# In visible functions just check for a taller tree in path, if none, return true

# In count functions, iterate from current towards the outside, counting trees smaller than. Counter starts from 1 since all trees see a min of 1 tree on any direction

def visible_right(x, y):
    for n in range (y + 1, columns):
        if matrix[x][y] <= matrix[x][n]:
            return False
    return True

def count_right(x, y):
    right = 1
    for n in range (y + 1, columns-1):
        if matrix[x][y] <= matrix[x][n]:
            return right
        else:
            right += 1
    return right


def visible_left(x, y):
    for n in range (0, y):
        if matrix[x][y] <= matrix[x][n]:
            return False
    return True

def count_left(x, y):
    left = 1
    for n in range (y - 1, 0, -1):
        if matrix[x][y] <= matrix[x][n]:
            return left
        else:
            left += 1
    return left

def visible_top(x, y):
    for n in range(0, x):
        if matrix[x][y] <= matrix[n][y]:
            return False
    return True

def count_top(x, y):
    top = 1
    for n in range(x-1, 0, -1):
        if matrix[x][y] <= matrix[n][y]:
            return top
        else:
            top += 1
    return top

def visible_bottom(x, y):
    for n in range(x + 1, rows):
        if matrix[x][y] <= matrix[n][y]:
            return False
    return True

def count_bottom(x, y):
    bottom = 1
    for n in range(x + 1, rows - 1):
        if matrix[x][y] <= matrix[n][y]:
            return bottom
        else:
            bottom += 1
    return bottom

main()

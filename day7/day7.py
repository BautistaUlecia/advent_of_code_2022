# Originally solved using stack and dictionary, read post about structural pattern matching and decided to re-solve trying that.
from collections import defaultdict
from itertools import accumulate

folders = defaultdict(int)
with open ("input.txt") as file:
    for line in file:
        
        # Easily parse data using structural pattern matching
        # https://peps.python.org/pep-0636/

        match line.split():
            case "$", "cd", "/": curr = ["/"]
            case "$", "cd", ".." : curr.pop()
            case "$", "cd", x: curr.append(x+"/")
            case "$", "ls": pass
            case "dir", _: pass
            case size, _:
                # Accumulate generates a list of ancestor folders. accumulate(["a", "b", "c"]) creates ["a", "ab", "abc"]
                for x in accumulate(curr):
                    folders[x] += int(size)

    print(sum(s for s in folders.values() if s <= 100000))
    print(min(s for s in folders.values() if s >= folders["/"] - 40000000))
                



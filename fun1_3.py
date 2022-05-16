def solve(numheads, numlegs):
    return (numlegs-2*numheads)/2
numheads=35
numlegs=94
print("Sum of rabbits =",solve(numheads,numlegs))
print("Sum of chickens =",numheads-solve(numheads,numlegs))
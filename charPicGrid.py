import copy

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x=0
y=0
rotate = copy.deepcopy(grid)
for x in range(len(grid)):
    for y in range(len(grid[x])):
        print(grid[x][y],end="")
    if(grid[x][y]==grid[x][-1]):
        print(grid[x][y],end='\n')
    else:
        print(grid[x][y],end="")
print("\nThis was the original grid. Now the altered one next...\n")
# Now to actually rotate this mofo 90 degrees.
# Basically just swap x's with y's
a = 0
b = 0
for a in range(len(rotate[a])):
    for b in range(len(rotate)):
        print(rotate[b][a],end="")
    if(rotate[b][a]==rotate[b][-1]):
        print(rotate[b][a],end="\n")
    else:
        print(rotate[b][a],end="")

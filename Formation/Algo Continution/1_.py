'''
Conway's Game Of Life

Conway's Game of Life (see https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a famous example of a cellular automaton devised as a thought experiment for modeling local populations and other networks.

The game takes an initial state which is a matrix of booleans. True represents a live cell. False is dead. On every turn, each cell computes it's next state based on its own state and that of its neighbors along horizontals, verticals, or diagonals. The rules are:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

For ease of viewing the states, we'll use strings instead of booleans. An "X" will represent a live cell, a space will represent a dead cell.




 - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

EXAMPLE(S)
blinker = [
  [" ", " ", " ", " ", " "], 0
  [" ", " ", "X", " ", " "], 1
  [" ", " ",  "X", " ", " "], 2
  [" ", " ", "X", " ", " "], 3
  [" ", " ", " ", " ", " "], 4
]

conway(blinker, 1) =>
[
  [ ' ', ' ', ' ', ' ', ' ' ],
  [ ' ', ' ', ' ', ' ', ' ' ],
  [ ' ', 'X', 'X', 'X', ' ' ],
  [ ' ', ' ', ' ', ' ', ' ' ],
  [ ' ', ' ', ' ', ' ', ' ' ]
]
conway(blinker, 2) =>
[     0  1   2  3  4     5
 0 [ ' ', ' ', ' ', ' ', ' ' ], 0
 1 [ ' ', ' ', 'X', ' ', ' ' ], 1
 2  [ ' ', ' ', 'X', ' ', ' ' ], 2
  [ ' ', ' ', 'X', ' ', ' ' ], 3
  [ ' ', ' ', ' ', ' ', ' ' ] 4
]

Notice that this pattern cycles between horizontal and vertical orientations. Look in the the wikipedia article for more interesting and well known patterns!

Brute force
    constraints: len(row), len(col)
    direction = [(0,1), (1,0),(1,1),... ]
    initiate a condition variable
    loop through each row, for each cell, we loop through each direction as long as it stays within boundary.

    check if its neighbor is X, if so, we increment the neighbor_count
    1. cell is live:
        1.1  if neighbor_count < 2 -> condition is " " -> append to an array
        1.2 if >=2 <=3 -> X -> "X"
        1.3 >3 -> ""
    2. cell is dead:
        check if neighbor_count =3 -> live




FUNCTION SIGNATURE
function conway(board, rounds) {
def conway(board, rounds):
'''


def conway(board, rounds):
    result = []
    lenCol = len(board[0])

    lenRow = len(board)
    directions = ((0, 1), (1, 0), (1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1))

    newRow = []
    for c in range(lenCol):
        for r in range(lenRow):
            count = helper(r, c)
            if isAlive(board[r][c], count):
                newRow.append("X")
            else:
                newRow.append(" ")

        result.append(newRow)

    if rounds > 1:
        result = conway(result, rounds - 1)
    else:
        return result

    """


 - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    """

    def isValid(r, c):
        return r >= 0 and r < lenRow and c >= 0 and c < lenCol

    def isAlive(currentCondition, count):

        if currentCondition == "X" and count < 2:
            return False

        if currentCondition == "X" and count in [2, 3]:
            return True

        if currentCondition == "X" and count > 3:
            return False

        if currentCondition == " " and count == 3:
            return True

    def helper(r, c):
        ## determine number of neighbors in
        neighbor_count = 0
        for direction in directions:
            dr, dc = direction
            if isValid(r + dr, c + dc) and board[r + dr][c + dc] == "X":
                neighbor_count += 1
        return neighbor_count


blinker = [
    [" ", " ", " ", " ", " "], 0
    [" ", " ", "X", " ", " "], 1
    [" ", " ", "X", " ", " "], 2
    [" ", " ", "X", " ", " "], 3
    [" ", " ", " ", " ", " "], 4
]

print(conway(blinker, 1))






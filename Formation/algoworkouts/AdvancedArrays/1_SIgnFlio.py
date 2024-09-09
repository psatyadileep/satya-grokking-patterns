/ *
'''
Reversi (https://en.wikipedia.org/wiki/Reversi), also called Othello, is a game where each piece has two sides, black and white, and after being placed, further moves cause other pieces to flip tiles. Specifically, a line of pieces of one color gets flipped when they become surrounded by pieces of the opposite color on both ends.

In this problem, we will be given a 2-dimensional array representing the board. Each position will contain a value of “B”, “W”, or “*” representing empty. Additionally, we get a position that is currently empty. Update the board to the new state after that play, including any flips if it is black’s turn to play. You can modify the existing array, but either way, return the board (2d array) with the new state.

Follow-up:
1. Update this code to take a parameter of a “B” or “W,” indicating which player is making a move.


EXAMPLE(S)
For example, consider the row:

1 2 3 4 5 6 7 8
* B W W W W * *

If black places a piece at position 7, the white pieces in between get flipped, so the result is:

1 2 3 4 5 6 7 8
* B B B B B B *

This can happen on a row, column, or diagonal and even at the same time. In the following example, if white place on position (5, 5), then all of the black pieces flip to white!

  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * W * * * * * *
3 * * B * * * * *
4 * * * B * * * *
5 W B B B ! * * *
6 * * * * B * * *
7 * * * * B * * *
8 * * * * W * * *

check each direction
  if white
    keep going until there's a black / out of bounds
    if there's no black
       don't change anything
    if there is
       update to B in the opposite direction
       until you hit the original position
  keep going through each direction

[(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]

// or a loop?
for (let i = -1; i < 2; i++) {
  for (let j = -1; j < 2; j++) {
    // skips the [0,0] coordinate
    if (!i && !j) continue
  }
}

FUNCTION SIGNATURE
function reversi(board, x, y)
def reversi(board, x, y):

The follow up adds another parameter, c.

  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * W * * * * * *
3 * * B * * * * *
4 * * * B * * * *
5 W B B B ! * * * --> playing as W
6 * * * * B * * *
7 * * * * B * * *
8 * * * * W * * *



  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * W * * * * * *
3 * * W * * * * *
4 * * * W * * * *
5 B W W W ! * * * --> playing as B
6 * * * * W * * *
7 * * * * W * * *
8 * * * * B * * *
'''
* /
function
reversi(board, x, y)
{

for (let i = -1; i < 2; i++) {
for (let j = -1; j < 2; j++) {
// skips the[0, 0] coordinate
if (!i & & !j)
continue
let
xDelta = x + i;
let
yDelta = y + j;

while (isInBound(xDelta, yDelta, board) & & board[xDelta][yDelta] == 'W') {
xDelta += i
yDelta += j
}

// at
this
point, either
out
of
bounds, B, or '*'
if (!isInBound(xDelta, yDelta, board) | | board[xDelta][yDelta] !== 'B') continue;

while (xDelta !== x & & yDelta != = y) {
board[xDelta][yDelta] = 'B';
xDelta -= i;
yDelta -= j;
}

}
}

return board
}

function
isInBound(row, col, board)
{
if (row >= 0 | | row < board.length) return true;
if (col >= 0 | | col < board[0].length) return true;

return false;
}

function
printBoard(board)
{
for (let i = 0; i < board.length; i++) {
    console.log(board[i].join(''));
}

}

let
board = ['*', 'B', 'W', 'W', 'W', 'W', '*', '*']
console.log(reversi(board, 6, 0))

const
board2 = [
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', 'B', '*', '*', '*', '*', '*', '*'],
['*', '*', 'W', '*', '*', '*', '*', '*'],
['*', '*', '*', 'W', '*', '*', '*', '*'],
['B', 'W', 'W', 'W', '!', '*', '*', '*'],
['*', '*', '*', 'W', 'W', '*', '*', '*'],
['*', '*', '*', '*', 'W', '*', '*', '*'],
['*', '*', '*', '*', 'B', '*', '*', '*']
]
console.log('board2', reversi(board2, 4, 4))
printBoard(board2)

const
board3 = [
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', 'W', '*', '*', '*', '*', '*', '*'],
['*', '*', 'W', '*', '*', '*', '*', '*'],
['*', '*', '*', ' W', '*', '*', '*', '*'],
['B', 'W', 'W', 'W', '!', '*', '*', '*'],
['*', '*', '*', '*', 'W', '*', '*', '*'],
['*', '*', '*', '*', 'W', '*', '*', '*'],
['*', '*', '*', '*', 'B', '*', '*', '*']
]
console.log('board3', reversi(board3, 4, 4))

[
[
    '*', '*', '*', '*', '*', '*', '*', '*'
],
[
    '*', 'W', '*', '*', '*', '*', '*', '*'
],
[
    '*', '*', 'W', '*', '*', '*', '*', '*'
],
[
    '*', '*', '*', ' W', '*', '*', '*', '*'
],
[
    'B', 'W', 'W', 'W', '!', '*', '*', '*'
],
[
    '*', '*', '*', '*', 'W', '*', '*', '*'
],
[
    '*', '*', '*', '*', 'W', '*', '*', '*'
],
[
    '*', '*', '*', '*', 'B', '*', '*', '*'
]
]

// *, *, *, *, *, *, *, *
// *'W' * * * * * *
    // * * 'W' * * * * *
    // * * * 'W' * * * *
    // 'B' 'W' 'W' 'W'! * * *--> playing as B
                                            // * * * * 'W' * * *
                                            // * * * * W * * *
                                            // * * * * B * * *

                                            // board = [
// ["B", "W", "*"],
// ["W", "W", "*"],
// ["*", "*", "*"],
//];
// printBoard(board);
// reversi(board, 0, 2);
// printBoard(board);

// board = [
// ["B", "W", "*"],
// ["W", "W", "*"],
// ["*", "*", "*"],
//];
// reversi(board, 2, 0);
// printBoard(board);

// board = [
// ["B", "W", "*"],
// ["W", "W", "*"],
// ["*", "*", "*"],
//];
// reversi(board, 2, 2);
// printBoard(board);

// board = [
// ["*", "W", "B"],
// ["W", "W", "B"],
// ["B", "B", "B"],
//]
// reversi(board, 0, 0);
// printBoard(board);

// // board = [
// // ['B', 'B', 'B', 'B', 'B', 'B'],
// // ['B', 'W', 'W', 'W', 'W', 'B'],
// // ['B', 'W', '*', '*', 'W', 'B'],
// // ['B', 'W', '*', '*', 'W', 'B'],
// // ['B', 'W', 'W', 'W', 'W', 'B'],
// // ['B', 'B', 'B', 'B', 'B', 'B']
// //];

// // reversi()

function
flip(c)
{
if (c !== "B" & & c != = "W") {
console.log(`Unexpected piece to flip: $
    {c}
`);
}
return c == "B" ? "W": "B";
}

function
findAndFlipOneDirection(board, x, y, dx, dy, c)
{
const
size = board[0].length; // for easy one dimensional testing.Board assumed to be square
if (x >= 0 & & x < size & & y >= 0 & & y < size) {
const position = board[x][y];
if (position == = c) {
// we found an opposing end!
return true;
} if (position == flip(c)) {
const
doFlip = findAndFlipOneDirection(board, x + dx, y + dy, dx, dy, c);
if (doFlip) {

board[x][y] = flip(position);
}
return doFlip;
}
}
return false;
}

function
reversi(board, x, y, c)
{
const
directions = [
                 [0, 1], // Up
             [1, 1], // Up and right
[1, 0], // Right
[1, -1], // Down and right
[0, -1], // Down
[-1, -1], // Down and left
[-1, 0], // Left
[-1, 1], // Up and left
];

board[x][y] = c;

for (let i = 0; i < directions.length; i++) {
    const[dx, dy] = directions[i];
findAndFlipOneDirection(board, x + dx, y + dy, dx, dy, c);
}
return board;
}
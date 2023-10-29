#multiply (copy reference)
board = [[0]*3 for i in range(3)]

print("New Board")
print(board)

board[0][0] = 1 #player 1 moves
board[2][2] = 2 #player 2 moves

print("Current Board")
print(board)

'''
Before
[ [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0] ]

After
[ [1, 0, 0],
  [0, 0, 0],
  [0, 0, 2] ]

'''
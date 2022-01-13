
import random 

print("Welcome to tic tac toe game!!")

def main():
    board=make_a_grid()
    player = get_random_first_player()
    while not (there_is_a_winner(board) or is_a_draw(board)):
        display_grid(board)
        
        make_move(player, board)
        player = swap_palyer_turn(player)
    display_grid(board)
    print("Good game. Thanks for playing!") 
    
def make_a_grid():
    grid=[]
    for i in range(9):
        grid.append(i + 1)
    return grid 

def display_grid(grid):
    print()
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print('-+-+-')
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print('-+-+-')
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print()

def get_random_first_player():
    if random.randint(0, 1) == 1:
       player= 'X'
    else:
        player='O'
    print(f"Player {player} turn")
    return player

def make_move(player,board):
    
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def swap_palyer_turn(player):
    return 'X' if player == 'O' else 'O'
def there_is_a_winner(grid):
    return (grid[0]==grid[1]==grid[2] or 
    grid[3]==grid[4]==grid[5] or 
    grid[6]==grid[7]==grid[8] or 
    grid[0]==grid[3]==grid[6] or
    grid[1]==grid[4]==grid[7] or 
    grid[2]==grid[5]==grid[8] or 
    grid[0]==grid[4]==grid[8] or 
    grid[2]==grid[4]==grid[6] )

def is_a_draw(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 

if __name__ == "__main__":
    main()
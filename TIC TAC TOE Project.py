#!/usr/bin/env python
# coding: utf-8

# # Design and print the Game Board:
# 

# In[11]:


board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# # Handle Player Moves:
# 

# In[12]:


def get_player_move(board, player):
    while True:
        try:
            row = int(input("Enter row (0-2) for your move: "))
            col = int(input("Enter column (0-2) for your move: "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")


# # Check for a Win:

# In[13]:


def check_win(board, player):
    for row in board:
        if all(square == player for square in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# # Check for a Tie:

# In[14]:


def check_tie(board):
    return all(all(square != "" for square in row) for row in board)


# # Main Game Loop:
# 

# In[15]:


def main():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    players = ["X", "O"]
    current_player = players[0]
    
    while True:
        print_board(board)
        get_player_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





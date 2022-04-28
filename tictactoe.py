"""
Author: Bryce Sanders
Assignment: W02 Prove: Developer - Solo Code Submission

The program must meet the following requirements:
1.) The program must have a comment with assignment and author names.
2.) The program must have at least one if/then block.
3.) The program must have at least one while loop.
4.) The program must have more than one function.
5.) The program must have a function called main.
"""

def main():
    """
    The main body of code. Facilitates the game of Tic-Tac-Toe.
    """

    # Set up variables to keep track of the Tic-Tac-Toe
    # and if there is a game over.
    board = [i for i in range(1, 10)]
    game_over = False

    # Print greeting message to players.
    print("\033[33m" + """
Welcome to Tic-Tac_Toe! Let's get started!
Decide who is X's and who is O's. Xs go first.""" + "\033[39m")

    # Loop until a game over occurs
    while not game_over:

        # Check how many square on the Tic-Tac-Toe board are
        # occupied.
        open_squares = 9
        for i in board:
            if i == "\033[31m" + "X" + "\033[39m" or i == "\033[36m" + "O" + "\033[39m":
                open_squares -= 1
        
        # Decide who's turn it is or if it is a game over.
        if open_squares == 0:
            game_over = True
            break
        elif open_squares % 2 != 0:
            is_turn = "X"
        elif open_squares % 2 == 0:
            is_turn = "O"

        # Check for three X's or O's in a row.
        game_over = check_for_three(board)
        if game_over == True:
            break

        # Display the current state of the Tic-Tac-Toe board
        # to the palyers.
        draw_board(board)

        # Decide who's turn it is and prompt them to pick a spot
        # on the Tic-Tac-Toe board.
        if is_turn == "X":
            choice = int(input("\033[31m" + "X's turn to choose a square (1-9): " + "\033[39m"))
            if board[choice - 1] not in ["X", "Y"]:
                board[choice - 1] = "\033[31m" + "X" + "\033[39m"
            else:
                print("\033[33m" + "That spot is taken!" + "\033[39m")
        else:
            choice = int(input("\033[36m" + "O's turn to choose a square (1-9): " + "\033[39m"))
            if board[choice - 1] not in ["X", "Y"]:
                board[choice - 1] = "\033[36m" + "O" + "\033[39m"
            else:
                print("\033[33m" + "That spot is taken!" + "\033[39m")

    # There was a game over. End the game.
    end_of_game(board)


def draw_board(board):
    """
    Displays the current state of the board.
    """

    # Print the board and each square's current value.
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def check_for_three(board):
    """
    Checks if there are three X's or O's in a row anywhere
    on the board.
    """

    # Check for three X's or O's in a row anywhere
    # on the board.
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):

            # There was three in a row. Return a game over.
            return True

    else:

        # There was not three in a row.
        return False


def end_of_game(board):
    """
    Informs the players that the game is over and asks if
    they would like to play another round.
    """
    
    # Display the final Tic-Tac-Toe board to the user.
    draw_board(board)

    # Prompt the user for a response
    answer = input("\033[33m" + "Good game! Would you like to play again? y/n " + "\033[39m")

    # If they answered in the affirmative, start a new round.
    if answer.lower() == "y":
        main()


# Call to main function.
if __name__ == "__main__":

    main()

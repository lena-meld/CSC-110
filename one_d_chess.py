'''
Magdalena Sammut
CSC 110-002
Project -4
This script is meant to simulate 1 dimensional chess
This script contains eight functions:
    The first accepts no arguments and returns the initial state of the board as
        a list
    The second iterates over each item of a board to return a visual depiction 
        of the board. It accepts one list argument
    The third accepts three arguments -- a list, integer representing an index, 
        and a string -- that confirms the player is making a valid move. If the 
        move is valid, it will return True. Otherwise, it will return False
    The fourth accepts three arguments -- a list, integer representing an index,
        and a string -- that will move a king piece. The function will return
        the new board
    The fifth accepts three arguments -- a list, integer representing an index, 
        and a string -- that will move a knight piece. The function will return
        the new board. If moving the knight piece will move the knight off the
        board, the function will stop running
    The sixth function determines if the piece being moved at a given index is
        a king or knight. After determining this, it calls the appropriate
        function (either the fourth or fifth) to move the piece. It returns the
        new state of the board
    The seventh function determines if the game is still in process by checking
        whether or not both kings are still on the board. If one of the kings is
        not on the board, the function will return True. If both of the kings
        are still on the board, the function will return False
    The eighth function determins who won the game. If the white king is
        missing, the function returns "Black", indicating the black team won. If
        the black king is missing, the function returns "White", indicating the
        white team won. If both teams are still in the game, the function will
        return False
'''

def create_board():
    '''
    This function accepts no argument. It exists to save the original state of 
        the board.
    Arg:
        None
    Return:
        A list with the initial state of the board
    '''
    # return the inital state of the board
    return ["WKi", "WKn", "WKn", 
            "EMPTY", "EMPTY", "EMPTY", 
            "BKn", "BKn", "BKi"]

def printable_board(board):
    '''
    This function accepts one list argument. Using the given values, it will
        return a visual depiction of the chess board. If one of the items in the
        list is empty, its associated spot on the board will appear blank
    Arg:
        board: a list representing the position of each chess piece
    Return:
        A visual depiction of the board
    '''
    # create the top edge of the board
    chess_board = "+-----------------------------------------------------+\n"
    # initialize the index
    index = 0
    # use a while loop to iterate through each item of the board's list
    while index < len(board):
        # save the value at a given index to a variable
        item = board[index]
        # check if there is a piece on the spot of the board
        if item == "EMPTY":
            # use spaces to visually illustrate the absence of a piece
            item = "   "
        # alter the chess_board variable to visually show the current state of 
        # the board
        chess_board += "| " + item + " "
        # check if the last item in the list is being checked
        if index == len(board) - 1:
            # if above condition met, create the bottom edge of the board
            chess_board += "|\n+-----------------------------------------------"
            chess_board += "------+"
        # iterate over each item in the list
        index += 1
    # return the current board
    return chess_board

def is_valid_move(board, position, player):
    """
    This function confirms the player is trying to make a valid move. To
        accomplish this, the function accepts a list argument, and integer
        argument representing an index, and a string argument representing the
        player's team
    Arg:
        board: a list representing the position of each piece on the board
        position: an integer representing which piece the player wants to move
            (index of the piece)
        player: a string argument representing the player's team. It can either
        be "BLACK" or "WHITE"
    Return:
        The function will return False if:
            the position is out of range
            a player tries moving a piece at an empty space
            the player controlling the white pieces tries to move a black piece
            the player controlling the black pieces tries to move a white piece
        The function will return True if:
            the player controlling the white pieces tries to move a white piece
            the player controlling the black pieces tries to move a black piece
    """
    # ensure the position is not out of range
    if position < 0 or position >= len(board):
        # if the position is out of range, return False
        return False
    # check if player team is "BLACK"
    if player == "BLACK":
        # confirm the player is trying to move a black piece, not a white one
        if board[position] == "BKn" or board[position] == "BKi":
            # confirm that there is a piece at the given position
            if board[position] != "EMPTY":
                # if all above conditions are met, return True
                return True
        # run if the player is trying to move a white piece
        else:
            # if the player is trying to move a white piece, return False
            return False
    # check if player team is "WHITE"
    if player == "WHITE":
        # confirm the player is trying to move a white piece, not a black one
        if board[position] == "WKn" or board[position] == "WKi":
            # confirm that there is a piece at the given position                
            if board[position] != "EMPTY":
                # if all above conditions are met, return True
                return True
        # run if player is trying to move a black piece
        else:
            # if player is trying to move a black piece, return False
            return False
    else:
        return False

def move_king(board, position, direction):
    """
    This function is used when moving a king piece. To do this, it accepts three
        arguments —— a list argument, an integer argument representing an index,
        and a string argument representing the direction of motion
    Args:
        board: a list representing the position of each piece on the board
        position: an integer representing which piece the player wants to move
            (index of the piece)
        direction: a string representing which diretion the player wants to move
            the piece. It can either be "LEFT" or "RIGHT"
    Return:
        This function has no returns. It serves to update the board
        """
    # check direction of motion
    if direction == "LEFT":
        # iterate list only when the position is greater than zero
        while position > 0:
            # check if space to the left is empty
            if board[position - 1] == "EMPTY":
                # move the king to the empty space
                board[position - 1] = board[position]
                # space king moved from is now empty
                board[position] = 'EMPTY'
            # run if space to the left is not empty
            else:
                # kill piece to the left
                board[position - 1] = board[position]
                # space king moved from is now empty
                board[position] = 'EMPTY'
                # update position to an index that is out of range to end the
                # while loop
                position = -1
            # repeat while loop until king kills a piece
            position -= 1
    # check direction of motion
    if direction == "RIGHT":
        # iterate list only when position is less than the length of the list
        while position < len(board) - 1:
            # check if space to the right is empty
            if board[position + 1] == "EMPTY":
                # move the king to the empty space
                board[position + 1] = board[position]
                # space king moved from is now empty
                board[position] = 'EMPTY'
            # run if space to the right has a piece
            else:
                # kill piece to the right
                board[position + 1] = board[position]
                # space king moved from is now empty
                board[position] = 'EMPTY'
                # update position to an index that is out of range to end the
                # while loop
                position = 9
            # repeat while loop until king kills a piece
            position += 1

def move_knight(board, position, direction):
    """
    This function is used when moving a knight piece. To do this, it accepts three
        arguments —— a list argument, an integer argument representing an index,
        and a string argument representing the direction of motion
    Args:
        board: a list representing the position of each piece on the board
        position: an integer representing which piece the player wants to move
            (index of the piece)
        direction: a string representing which diretion the player wants to move
            the piece. It can either be "LEFT" or "RIGHT"
    Return:
        This function has no returns, it serves to update the board. That being
        said, the return statements in line 218 and 237 are used to stop running
        the function if moving the knight from its position would move the
        knight off the board. In other words, the board will remain unchanged.
    """
    # check direction of motion
    if direction == "LEFT":
        # ensure that moving the knight from this space will not move the knight
        # off the board
        if position - 2 < 0:
            # stop running function if above condition met
            return
        # check if two spaces to the left of knight is empty
        if board[position - 2] == "EMPTY":
            # move knight to the empty space if above condition met
            board[position - 2] = board[position]
            # space from which knight moved is now empty
            board[position] = "EMPTY"
        # run if two spaces to the left of the knight has a piece
        else:
            # kill piece two spaces left
            board[position - 2] = board[position]
            # space from which knight moved is now empty
            board[position] = "EMPTY"
    # check direction of motion
    if direction == "RIGHT":
        # ensure that moving the knight from this space will not move the knight
        # off the board
        if position + 2 > 8:
            # stop running function if above condition met
            return
        # check if two spaces to the right of knight is empty
        if board[position + 2] == "EMPTY":
            # move knight to the empty space if above condition is met
            board[position + 2] = board[position]
            # space from which knight moved is now empty
            board[position] = "EMPTY"
        # run if two spaces to the right of the knight has a piece
        else:
            # kill piece two spaces right
            board[position + 2] = board[position]
            # space from which knight moved is now empty
            board[position] = "EMPTY"

def move(board, position, direction):
    """
    This function is used to move any piece. To do this, it accepts three
        arguments: a list argument, an integer argument representing an index,
        and a string argumnet representing the direction of motion. This
        function calls the move_king function if the player wants to move a king
        piece. If the player wants to move a knight, this function will call the
        move_knight function
    Args:
        board: a list representing the position of each piece on the board
        position: an integer representing which piece the player wants to move
            (index of the piece)
        direction: a string representing which diretion the player wants to move
            the piece. It can either be "LEFT" or "RIGHT"
    Returns:   
        This function has no returns. It is used to update the board when moving
            a piece
    """
    # check if piece player wishes to move is a king
    if board[position] == "WKi" or board[position] == "BKi":
        # if above condition met, call the move_king function to move the piece
        move_king(board, position, direction)
    # check is piece player wishes to move is a knight
    if board[position] == "WKn" or board[position] == "BKn":
        # if above condition met, call the move_knight function to move the 
        # piece
        move_knight(board, position, direction)

def is_game_over(board):
    '''
    This function determines if the game is over. To do so, it accepts one list
        argument
    Arg:
        board: a list representing the position of each piece on the baord
    Returns:
        The function will return True if there is only one king left on the
            board
        The function will return False if both kings are still on the board
    '''
    # determine if white king is still alive
    if "WKi" not in board:
        # if white king no longer in game, the game is over
        return True
    # determine if the black king is still alive provided the white king is
    # still alive
    if "BKi" not in board:
         # if black king is not longer in game, the game is over
        return True
    # run if both kings are still in the game
    else:
        # if both kings are still alive, return False. The game is still not
        # over
        return False

def whos_the_winner(board):
    """
    This function will determine which player won the game. To do so, it uses
        one list argument
    Arg:
        board: a list representing the position of each piece on the board
    Return:
        If the white king is no longer in board, the function will return
            "Black". This indicates the player controlling the black pieces won
        If the black king is no longer in board, the function will return
            "White". This indicates the player controlling the white pieces won
        If both kings are still in board, the function will return None. This
            indicates the game is still in process
    """
    # determine whether or not the white king is still on the board
    if "WKi" not in board:
        # if white king no longer on board, black team wins
        return "Black"
    # determine whether or not the black king is still on the board provided the
    # white king is
    if "BKi" not in board:
        # if black king is no longer in the game, white team wins
        return "White"
    # run if first two conditions did not run
    else:
        # if game is still in progress, there is no winner. Continue playing.
        return None

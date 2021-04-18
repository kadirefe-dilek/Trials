# Source code for a simple XOX game written in Python 3.8


# creating a list to hold the game plane
room = []


# function to print the game table
def print_table():
    print(" " + room[0] + " | " + room[1] + " | " + room[2])
    print("-----------")
    print(" " + room[3] + " | " + room[4] + " | " + room[5])
    print("-----------")
    print(" " + room[6] + " | " + room[7] + " | " + room[8])


# function to actually play the game
def play_game(order):
    place = int(input("Which room  you're gonna play on? "))  # asking user for her move

    if 1 <= place <= 9 and room[place - 1] == ' ':  # checking for game rules
        if order == 1:  # means it is turn for X
            room[place - 1] = 'X'
        elif order == 2:  # means it is turn for O
            room[place - 1] = 'O'
    else:  # Input not matching rules
        print("Type a number from 1 to 9 whose room is currently empty")  # error message
        play_game(order)  # self calling


# to check if there is a winner
def is_finished():
    # conditions to x
    if (room[0] == room[1] and room[0] == room[2] and room[0] == 'X' or  # horizontal
            room[3] == room[4] and room[3] == room[5] and room[3] == 'X' or
            room[6] == room[7] and room[6] == room[8] and room[6] == 'X' or
            room[0] == room[3] and room[0] == room[6] and room[0] == 'X' or  # vertical
            room[1] == room[4] and room[1] == room[7] and room[1] == 'X' or
            room[2] == room[5] and room[2] == room[8] and room[2] == 'X' or
            room[0] == room[4] and room[0] == room[8] and room[0] == 'X' or  # cross
            room[2] == room[4] and room[2] == room[6] and room[2] == 'X'):
        print("X is the winner!")
        return 1        # means there is a winner

    # conditions to y
    elif (room[0] == room[1] and room[0] == room[2] and room[0] == 'O' or  # horizontal
          room[3] == room[4] and room[3] == room[5] and room[3] == 'O' or
          room[6] == room[7] and room[6] == room[8] and room[6] == 'O' or
          room[0] == room[3] and room[0] == room[6] and room[0] == 'O' or  # vertical
          room[1] == room[4] and room[1] == room[7] and room[1] == 'O' or
          room[2] == room[5] and room[2] == room[8] and room[2] == 'O' or
          room[0] == room[4] and room[0] == room[8] and room[0] == 'O' or  # cross
          room[2] == room[4] and room[2] == room[6] and room[2] == 'O'):
        print("O is the winner!")
        return 1        # means there is a winner

    return 0        # means no winner


# main function starts
def main():
    
    for i in range(9):
        room.append(' ')  # initializing a 9-element-list with ' 's (space characters) -for aesthetic-

    print_table()  # printing table once at the beginning

    # playing the game
    for i in range(9):
        turn = (i % 2) + 1  # deciding on whose turn it is, and normalizing values for player 1 and 2
        print("Player" + str(turn) + "'s turn: ")  # message to users
        play_game(turn)
        print_table()

        # checking if the winning condition is met
        if i > 3:       # starts checking after 5th loop
            if is_finished() == 1:
                print("Congrats to the winner!")
                return 0
# end of main function


if __name__ == "__main__":
    main()

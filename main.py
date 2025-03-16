"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
"""
import time

separator = "=" * 30

def playing_board(board):
    '''
    definování hrací desky pomocí cyklu
    :param board: herní deska 3x3
    '''
    print(separator)
    for row in board:
        print("+---+---+---+")
        print("|", row[0], "|", row[1], "|", row[2], "|")
    print("+---+---+---+")
    print(separator)
"""
#testovací výpis
test = [
        ["0", " ", "x"],
        ["0", " ", "x"],
        ["0", " ", "x"],
    ]

playing_board(test)
"""

def check_game(board, player):
    """
    kontroluje zda hráč vyhrál hru

    :param board: herní deska 3x3
    :param player: Symbol pro hráče 'X' nebo 'O'
    :return: True pokud hráč vyhrál jinak False
    """
    #kontrola symbolů v řádkách jestli jsou tři stejné symboly v řádku
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True  #pokud ano hráč vyhrál

    ##kontrola symbolů ve sloupcích jestli jsou tři stejné symboly ve sloupci
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == player:
            return True #pokud ano hráč vyhrál

    #kontrola diagonály zleva -> do prava dolů
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True #pokud ano hráč vyhrál

    #kontrola diagonály zprava -> doleva dolů
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True #pokud ano hráč vyhrál

    #pokud žádná podmínka neplatí vrátí False(nevyhrál) hra pokračuje
    return False
"""
#testovací výpis
test = [
        ["O", " ", "x"],
        ["O", "O", "O"],
        ["O", " ", "x"],
    ]

print(check_game(test, "O"))
"""

def draw(board):
    """
    Kontrola polí pokud jsou všechna pole obsazená je remíza

    :param board: herní deska 3x3
    :return: True pokud je remíza jinak False
    """
    for row in board:
        for box in row:
            if box == " ":
                return False

    return True
"""
#test remízy
test = [
    ["X", "O", "X"],
    ["X", "X", "O"],
    ["O", "X", "O"]
]

print(draw(test)) 
"""

def tic_tac_toe():
    """
    hlavní funkce pro spuštění hry
    pravidla hry
    počítání času hry

    """

    print("Welcome to Tic Tac Toe")
    print(separator)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print(separator)
    print("Let's start the game")
    print("-" * 30)

    #vytvoření prázdné hrací desky - i vytváři řádky, j vytváří sloupce
    board = [[" " for i in range(3)] for j in range(3)]
    #prní hráč X druhý hráč O
    players = ["X", "O"]
    #sleduje který hráč je na řadě
    turn = 0
    #začátek měřění času hry
    start_time = time.time()

    #hlavní smyčka hry
    while True:
        playing_board(board)  #aktualní stav hrací desky
        player = players[turn % 2] #určení hráče který je aktuálně na řadě

        while True:
            #hráčovo volba
            try:
                choice = int(input(f"Player {player} | Please enter your move number (1-9): "))
                if choice < 1 or choice > 9:
                    print("Invalid input! Enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Enter a number between 1 and 9.")
                continue
            #kontrola obsazeného pole
            row, column = (choice - 1) // 3, (choice - 1) % 3
            if board[row][column] != " ":
                print("This spot is already taken! Try again")
                continue
            break  #pokud je tah správný ukončí smyčku a pokračuje dál

        board[row][column] = player  #aktualizace hrací desky

        if check_game(board, player):
            playing_board(board)
            print(f"Congratulations, the player {player} WON!")
            print(separator)
            #konec měření času
            end_time = time.time()
            result_time = end_time - start_time
            round_time = round(result_time, 2)
            print(f"Game time: {round_time: }s")
            break
        elif draw(board):
            playing_board(board)
            print("It's a DRAW!")
            print(separator)
            # konec měření času
            end_time = time.time()
            result_time = end_time - start_time
            round_time = round(result_time, 2)
            print(f"Game time: {round_time: }s")

            break

        turn += 1

if __name__ == "__main__":
    tic_tac_toe()





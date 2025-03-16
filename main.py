"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
"""
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

    #kontrola symbolů ve sloupcích jestli jsou tři stejné symboly v řádku
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
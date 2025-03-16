"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Ledvina
email: ledvinajakub@seznam.cz
"""
separator = "=" * 30

def playing_board(board):
    '''
    definování hrací desky pomocí cyklu

    '''
    print(separator)
    for row in board:
        print("+---+---+---+")
        print("|", row[0], "|", row[1], "|", row[2], "|")
    print("+---+---+---+")
    print(separator)
"""
testovací výpis
test = [
        ["0", " ", "x"],
        ["0", " ", "x"],
        ["0", " ", "x"],
    ]

playing_board(test)
"""
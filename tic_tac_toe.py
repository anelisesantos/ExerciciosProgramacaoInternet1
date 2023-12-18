def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for cell in row:
            print("|   " + str(cell) + "   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")



def enter_move(board):
    move = -1
    while move not in range(1, 10):
        try:
            move = int(input("Enter your move (1-9): "))
            row, col = (move - 1) // 3, (move - 1) % 3
            if str(board[row][col]) not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("This square is already taken. Choose another one.")
                move = -1
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")



def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if str(board[i][j]) not in ['O', 'X']:
                free_fields.append((i, j))
    return free_fields



def victory_for(board, sign):
    # Verificar linhas e colunas
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def draw_move(board):
    from random import randrange
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'



def main():
    # Inicializando o tabuleiro
    board = [['1', '2', '3'], 
             ['4', '5', '6'], 
             ['7', '8', '9']]

    # O primeiro movimento do computador é fixo - colocar um 'X' no meio do tabuleiro
    board[1][1] = 'X'

    # Loop principal do jogo
    while True:
        display_board(board)  # Mostra o tabuleiro

        # Turno do jogador
        enter_move(board)
        display_board(board)  # Mostra o tabuleiro após o movimento do jogador
        if victory_for(board, 'O'):
            print("Parabéns! Você venceu!")
            break
        elif not make_list_of_free_fields(board):
            print("Empate!")
            break

        # Turno do computador
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)  # Mostra o tabuleiro após o movimento do computador
            print("Você perdeu! O computador venceu.")
            break
        elif not make_list_of_free_fields(board):
            print("Empate!")
            break

# Executando o jogo
main()

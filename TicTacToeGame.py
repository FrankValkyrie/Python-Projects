board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
current_marker = ''
current_player = 0

def draw_board():
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print("-----------")

def place_marker(slot):
    if slot < 1 or slot > 9:
        print("That slot is invalid! Slots are numbered from 1 to 9.")
        return False

    row = (slot - 1) // 3
    col = (slot - 1) % 3

    if board[row][col] not in ('X', 'O'):
        board[row][col] = current_marker
        return True
    else:
        print("That slot is occupied! Try another slot.")
        return False

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return current_player
        if board[0][i] == board[1][i] == board[2][i]:
            return current_player
    if board[0][0] == board[1][1] == board[2][2]:
        return current_player
    if board[0][2] == board[1][1] == board[2][0]:
        return current_player
    return 0

def swap_player_and_marker():
    global current_marker, current_player
    current_marker = 'O' if current_marker == 'X' else 'X'
    current_player = 2 if current_player == 2 else 1

def game():
    global current_player, current_marker
    print("Player one, choose your marker between X and O: ")
    marker_p1 = input().upper()
    if marker_p1 not in ('X', 'O'):
        game()

    current_marker = marker_p1

    draw_board()

    player_won = None

    for _ in range(9):
        print(f"It's player {current_player}'s turn. Enter your slot: ")
        #slot = int(input())
        slot = None
        while True:
            try:
                slot = int(input(""))
            except ValueError:
                print("Please type a number in numerical form. Try again")
                continue
            else:
                break
        
        if not place_marker(slot):
            continue

        draw_board()

        player_won = check_winner()

        if player_won == 1:
            print("Player one won! Congratulations!")
            exit()
        elif player_won == 2:
            print("Player two won! Congratulations!")
            exit()

        swap_player_and_marker()

    if player_won == 0:
        print("It's a tie!")

def main():
    game()
if __name__ == "__main__":
    main()
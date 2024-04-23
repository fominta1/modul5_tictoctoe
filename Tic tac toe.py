# дано поле 3Х3, с системой от 0 до 2, оси Х и У

from random import randrange

#     0    1    2
board = [
    [".", ".", "."],  # 0
    [".", ".", "."],  # 1
    [".", ".", "."],  # 2
]


def draw_board():
    for row in board:
        print()
        print("------------------")
        for col in row:
            print(f"| {col} ", end=" ")


x2 = randrange(0, 2)
y2 = randrange(0, 2)
x2 = 3


def get_input(player):
    # пример от Сергея Ежова
    print("Ход", player)
    x1, y1 = input("Введите координаты: ").split()
    if not x1.isdigit() or not y1.isdigit():
        print("введите заново")
        # код на повтор - вызов функции ввода
    x1, y1 = int(x1), int(y1)
    # print(f"Вы ввели x = {x1} и y = {y1}")
    return x1, y1


# ??? как поставить loop функцию на выбор координатов

# проверка


def check_winning(x1, y1, x_or_o):

    if (x1 < 0 or x1 > 2) or (y1 < 0 or y1 > 2):
        print("выберите координаты от 0 до 2")

    x2 = randrange(0, 2)
    y2 = randrange(0, 2)

    if board[x1][y1] != ".":
        print("Введите заново")
        # код на повтор ввода

    # диагональ
    if (board[0][0] == x_or_o and board[1][1] == x_or_o and board[2][2]) or (
        board[0][2] == x_or_o and board[1][1] == x_or_o and board[2][0] == x_or_o
    ):
        pass
        print(f"{x_or_o} wins!")
        exit

    # горизонталь
    if (
        (board[0][0] == x_or_o and board[1][0] == x_or_o and board[2][0])
        or (board[1][0] == x_or_o and board[1][1] == x_or_o and board[1][2])
        or (board[2][0] == x_or_o and board[2][1] == "X" and board[2][2] == "X")
    ):
        pass
        print(f"{x_or_o} wins!")
        exit

    # вертикаль
    if (
        (board[0][0] == x_or_o and board[1][0] == x_or_o and board[2][0])
        or (board[0][1] == x_or_o and board[1][1] == x_or_o and board[1][2])
        or (board[0][2] == x_or_o and board[1][2] == x_or_o and board[2][2])
    ):
        pass
        print(f"{x_or_o} wins!")
        exit


# ??? я не вижу у себя, что я залинковала логику что один пользователь ставит 0, а другой Х

x_or_y = "X"
while True:
    draw_board()
    x, y = get_input(x_or_y)
    if board[x][y] == ".":
        board[x][y] = x_or_y
    else:
        print("this position is already occupied, try again")
        continue
    check_winning(x, y, x_or_y)
    x_or_y = "O" if x_or_y == "X" else "X"

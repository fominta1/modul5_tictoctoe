from random import randrange


#дано поле 3Х3, с системой от 0 до 2, оси Х и У


# какие нам нужны функции
# - отрисовки текущего состояния доски
# - приём пользовательского ввода (должна определять X ты или Y)
# - проверка выигрышная ли комбинация
# - проверка ввода координат
# - проверка "незанятости" клетки

# как выглядит цикл
# начинаем с Х
# - отрисовка
# - ввода
# - проверка корректности
# - проверка незанятости
# - проверка выигрыша или ничьей
# если Х, то О и наоборот

#     0    1    2
board = [
    [".", ".", "."], # 0
    [".", ".", "."], # 1
    [".", ".", "."], # 2
]

# диагональ
if (board[0][0] == "X" and board[1][1] == "X" and board[2][2]) or (board[0][2] == "X" and board[1][1] == "X" and board[2][0]):
    pass


# to send via telegram
#```python
#
#```


# горизонталь
if (board[0][0] == "X" and board[1][0] == "X" and board[2][0]) or (board[1][0] == "X" and board[1][1] == "X" and board[1][2]) or (board[2][0] == "X" and board[2][1] == "X and board[2][2]"):
    pass


# вертикаль
if (board[0][0] == "X" and board[1][0] == "X" and board[2][0]) or (board[0][1] == "X" and board[1][1] == "X" and board[1][2]) or (board[0][2] == "X" and board[1][2] == "X" and board[2][2]):
    pass


def draw_board():
    for row in board:
        print()
        print("------------------")
        for col in row:
            print(f"| {col} ", end=" ")


draw_board()



def get_input(player):
    #пример от Сергея Ежова
    print("Ход", player)
    x1,y1 = input("Введите координаты: ").split()
    if not x1.isdigit() or not y1.isdigit():
        print("введите заново")
        # код на повтор - вызов функции ввода
    x1,y1 = int(x1),int(y1)
    print(f"Вы ввели x = {x1} и y = {y1}")
    return x1, y1

x, y = get_input("O")


# x2 = randrange(0,2)
# y2 = randrange(0,2)
# x2 = 3



# проверка
if (x1<0 or x1>2) or (y1<0 or y1>2):
    print("выберите координаты от 0 до 2")

x2 = randrange(0,2)
y2 = randrange(0,2)


if board[x1][y1] != ".":
    print("Введите заново")
    # код на повтор ввода

#проверить выйгрыш если 0,0,0 или Х,Х,Х

print("Победитель: ") ??{User1} or {User2}

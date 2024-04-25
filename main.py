from battleship_game import BattleshipGame

while True:
    size = input("Введите размер поля. Это должно быть целое число. Размер: ")
    try:
        size = int(size)
    except ValueError:
        print("Пожалуйста, введите целое число")
        continue
    if size > 26:
        print("Размер поля не может превышать 26")
        continue
    break

while True:
    ships = input("Введите количество кораблей. Это должно быть целое число. Количество кораблей: ")
    try:
        ships = int(ships)
        break
    except ValueError:
        print("Пожалуйста, введите целое число")
        continue

battleshipGame = BattleshipGame(size, ships)

battleshipGame.play()


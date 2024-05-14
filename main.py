from battleship_game import BattleshipGame

while True:
    size = input("Введите размер поля. Это должно быть целое число. Размер: ")
    try:
        size = int(size)
    except ValueError:
        print("Пожалуйста, введите целое число")
        continue
    if size > 26 or size <= 0:
        print("Размер поля должен находиться в диапазоне от 1 до 26")
        continue
    break

min_ships, max_ships = size ** 2 // 9, size ** 2 // 6

while True:
    ships = input(f"Введите количество кораблей. Это должно быть целое число. "
                  f"Рекомендуемое количество кораблей от {min_ships} до {max_ships}. "
                  f"При выборе значения >{max_ships} возможно зависание игры. Количество кораблей: ")
    try:
        ships = int(ships)
    except ValueError:
        print("Пожалуйста, введите целое число")
        continue
    if ships <= 0:
        print("Количество кораблей не должно быть равно 0 и меньше")
        continue
    break


battleshipGame = BattleshipGame(size, ships)

battleshipGame.play()

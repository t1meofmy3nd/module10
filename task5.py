user_height = int(input("Ввндите высоту пирамиды: "))
count = 0

for row in range(user_height):
    for cow in range(1):
        print(f"{' ' * (user_height - row)}{'#' * row}#{'#' * row}", end="")
    print()
#цикл cow можно убрать. Добавил из за темы модуля

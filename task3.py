row_user = int(input("Введите высоту: "))
col_user = int(input("Введите широту: "))

for row in range(1, row_user + 1):
    for col in range(1, col_user + 1):
        if (1 < col < col_user) and (row == 1 or row == row_user):
            print("-", end="")
        elif col == 1 or col == col_user:
            print("|", end="")
        else:
            print(" ",end="")
    print()
user_height = int(input("Ввндите высоту пирамиды: "))
count = 0

for row in range(user_height):
    count += 1
    print(f"{' ' * (user_height - count)}{'#' * row}#{'#' * row}", end="")
    print()


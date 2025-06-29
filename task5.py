user_height = int(input("Введите высоту пирамиды: "))
count = 0

for row in range(user_height):
    count += 1
    print(f"{' ' * (user_height - count)}{'#' * row}#{'#' * row}", end="")
    print()
#Я могу решить с вложенным циклом, но с одним проще

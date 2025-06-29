user_number = int(input("Введите число: "))

for row in range(1, user_number + 1):
    for col in range(row):
        print(row, end=" ")
    print()
user_number = int(input("Введите количество чисел: "))
count_simple_numbers = 0

for first in range(user_number):
    number_for_check = int(input("Введите число: "))
    if number_for_check < 2:

        continue

    is_prime = True
    for second in range(2, int(number_for_check ** 0.5) + 1):
        if number_for_check % second == 0:
            is_prime = False
            break
    if is_prime:
        count_simple_numbers += 1

print(f"Количество простых чисел в последовательности: {count_simple_numbers}")

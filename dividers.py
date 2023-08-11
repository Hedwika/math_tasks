import math

def sum_of_digits(digit_sum):
    digit_sum_str = str(digit_sum)
    final_digit_sum = sum(int(digit_char) for digit_char in digit_sum_str)
    return final_digit_sum

def last_two_digits(number):
    num = int(number[-2]) + int(number[-1])
    return num

def divisor(number):
    dividers = [1]
    number_int = int(number)
    num_digits = int(math.log10(abs(int(number)))) + 1
    last_digit_str = number[-1]
    evens = [0, 2, 4, 6, 8]

    if num_digits > 1:
        digit_sum = sum_of_digits(number_int)

        while digit_sum > 1:
            digit_sum = sum_of_digits(digit_sum)

    # 2
    if last_digit_str == "2":
        dividers.append(2)

    # 3
    if not (digit_sum % 3):
        dividers.append(3)

    # 4
    if number == 8 or not (last_two_digits(number) // 4):
        dividers.append(4)

    # 5
    if last_digit_str == "5" or last_digit_str == "0":
        dividers.append(5)

    # 6
    if 2 in dividers and 3 in dividers:
        dividers.append(6)

    # 7
    if not (int(number[0:-1]) - int(number[-1])*2) % 7:
        dividers.append(7)

    # 8
    if ((len(number) == 2) and not number_int % 8) or (len(number) > 2 and not (int(number[-2:-1]) % 8) and int(number[-3]) in evens):
        dividers.append(8)

    # 9
    if not (digit_sum // 9):
        dividers.append(9)

    # 10
    if last_digit_str == "0":
        dividers.append(10)

    dividers.append(int(number))
    print(f"Číslo je dělitelné těmito čísly: {dividers}.")

number_to_check = input("Please enter a number: ")
divisor(number_to_check)

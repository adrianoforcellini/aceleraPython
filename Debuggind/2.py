from math import factorial


def map_factorial(numbers):
    result = []

    for num in numbers:
        result.append(factorial(num))

    return result


def main():
    input_list = [1, 2, 3, 4, 5]
    return map_factorial(input_list)


if __name__ == "__main__":
    main()

# Sem alterar o código, descubra qual exceção é levantada se:

# Um dos elementos da input_list for um inteiro negativo.
#   R: ValueError('factorial() not defined for negative values')

# Um dos elementos da input_list for uma string.
#   R: TypeError("'str' object cannot be interpreted as an integer")

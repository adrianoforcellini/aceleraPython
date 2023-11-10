# Apesar de sistemas TTS serem bastante complexos, sua missão é “somente”
# ajudar no pré-processamento do texto, transformando números em palavras
# Isso significa que você deve construir uma função que recebe um número
# inteiro e retorna uma string em português, em que cada dígito é
# representado por uma palavra.

# Ou seja:

# 1 = “um”
# 2 = “dois”
# 3 = “três”


import random


DIGITS_MAP = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
}


def generate_int_description(integer):
    """Transforma dígitos de um número em texto PT-BR"""
    digits = list(str(integer))

    description = f"{DIGITS_MAP.get(digits[0])}"
    for digit in digits[1:]:
        description += f" {DIGITS_MAP.get(digit)}"

    return description


def main():
    integer = random.randint(10000, 99999)

    description = generate_int_description(integer)

    print(f"Descrição do número {integer}: '{description}'")


if __name__ == "__main__":
    main()


# A correção pode ser feita de duas formas: alterar as chaves do
# DIGITS_MAP para str; converter os valores da lista digits para
# int antes das chamadas DIGITS_MAP.get(...

ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def from_base_to_dec(num: str, base: int) -> float:
    if '.' in num:
        int_part_of_num_in_string, float_part_of_num_in_string = num.split(".")
    else:
        int_part_of_num_in_string = num
        float_part_of_num_in_string = ""

    result_number = 0

    for i, symbol in enumerate(int_part_of_num_in_string[::-1]):
        symbol_index = ALPHABET.find(symbol)
        if symbol_index >= base or symbol_index < 0:
            raise ValueError(f"Invalid symbol '{symbol}'")
        result_number += symbol_index * (base ** i)

    for i, symbol in enumerate(float_part_of_num_in_string, 1):
        symbol_index = ALPHABET.find(symbol)
        if symbol_index >= base or symbol_index < 0:
            raise ValueError(f"Invalid symbol '{symbol}'")
        result_number += symbol_index * (base ** (-i))

    return result_number


def dec_to_base(num: int, base: int = 10, float_part_symbol_limit=300) -> str:
    if base > len(ALPHABET):
        raise ValueError("Very big base")

    int_part = int(num)
    float_part = num - int_part

    int_part_result = float_part_result = ""

    while int_part > 0:
        int_part_result = ALPHABET[int_part % base] + int_part_result
        int_part //= base

    while not float(float_part).is_integer() and len(float_part_result) < float_part_symbol_limit:
        float_part *= base
        float_part_result += str(int(float_part))
        float_part -= int(float_part)

    additional = "..." if len(float_part_result) == float_part_symbol_limit else ""

    return f"{int_part_result:0<1}{'.' if float_part_result else ''}{float_part_result}{additional}"


def convert_number_from_one_base_to_another(source_number: str, from_base, to_base=10) -> str:
    if from_base == 10:
        number = float(source_number)
    else:
        number = from_base_to_dec(source_number, from_base)

    if to_base == 10:
        return str(number)
    else:
        return dec_to_base(number, to_base)


if __name__ == '__main__':
    number = input(">>> Enter a number: ")
    from_base = int(input(">>> Enter a from base: "))
    to_base = int(input(">>> Enter a to base: "))
    print(f"Answer: {convert_number_from_one_base_to_another(number, from_base, to_base)}")

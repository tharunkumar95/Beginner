def print_formatted(number):

    for x in range(1, number + 1):
        # Decimal
        decimal = x

        # Binary
        binary = bin(x)
        bin_str = str(binary)

        # Hexadecimal (capitalized)
        hexadec = hex(x).upper()
        hex_str = str(hexadec)

        # Octal
        octal = oct(x)
        oct_str = str(octal)

        print(decimal, '\t', oct_str[2:], '\t', hex_str[2:])


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
def printDecimal(i):
    return str(i)

def printOctal(i):
    return str(oct(i))[2:]

def printHexadecimal(i):
    return str(hex(i))[2:]

def printBinario(i):
    return str(bin(i))[2:]


def imprimirTabela():
    print("{:7s} {:5s} {:11s} {:7s}".format("Decimal", "Octal", "Hexadecimal",  "Binario"))
    for i in range(226):
        print("{:7s} {:5s} {:11s} {:7s}".format("-" * 7, "-" * 5, "-" * 11,  "-" * 7))
        print("{:^7s} {:^5s} {:^11s} {:^7s}".format(printDecimal(i),printOctal(i),printHexadecimal(i),printBinario(i)))



imprimirTabela()
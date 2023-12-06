def decimalToBinary(n): 
    return bin(n).replace("0b", "") 


def NAND_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    print( "The 'NAND' of a and b is ", ~(a & b))

NAND_decimal()

def NAND_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    c = a & b
    c = ~c
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c) 
    print( "The 'NAND' of a and b is ", c)
    
NAND_binary()
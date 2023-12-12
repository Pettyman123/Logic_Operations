def decimalToBinary(n): 
    return bin(n).replace("0b", "") 


def XNOR_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    print( "The 'XNOR' of a and b is ", ~(a ^ b))

XNOR_decimal()

def XNOR_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    c = a ^ b
    c = ~c
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c) 
    
    print( "The 'XNOR' of a and b is ", c)
    
XNOR_binary()
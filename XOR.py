def decimalToBinary(n): 
    return bin(n).replace("0b", "") 


def XOR_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    print( "The 'XOR' of a and b is ", a ^ b)

XOR_decimal()

def XOR_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    c = a ^ b
    
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c) 
    print( "The 'XOR' of a and b is ", c)
    
XOR_binary()
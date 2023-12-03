def decimalToBinary(n): 
    return bin(n).replace("0b", "") 


def AND_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    print( "The 'AND' of a and b is ", a & b)

AND_decimal()

def AND_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    c = a & b
    
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c) 
    print(a)
    print(b)
    print( "The 'AND' of a and b is ", c)
    
AND_binary()
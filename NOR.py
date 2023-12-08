
def NOR_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    
    print( "The 'NOR' of a and b is ", ~(a | b))

NOR_decimal()

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
   

    
def NOR_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    # Driver code 
    c = a | b
    c = ~c
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c)
    print(a)
    print(b)
    print( "The 'NOR' of a and b is ", c)

NOR_binary()
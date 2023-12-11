
def OR_decimal():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    
    print( "The 'OR' of a and b is ", a | b)

OR_decimal()

def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
   

    
def OR_binary():
    a = int(input("Enter the first binary digit: "))
    b = int(input("Enter the second binary digit: "))
    # Driver code 
    c = a | b
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        b = decimalToBinary(b)
        c = decimalToBinary(c)
    print(a)
    print(b)
    print( "The 'OR' of a and b is ", c)

OR_binary()
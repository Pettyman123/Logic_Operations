def decimalToBinary(n): 
    return bin(n).replace("0b", "") 


def NOT_decimal():
    a = int(input("Enter the first decimal digit: "))
    
    print( "The 'NOT' of a is ", ~a )

NOT_decimal()

def NOT_binary():
    a = int(input("Enter the first decimal digit: "))
    a = ~a
    
   #  print("The 'NOT' of a is ", a)
    if __name__ == '__main__': 
        a = decimalToBinary(a)
        
    print( "The 'NOT' of a is ", a)
    
NOT_binary()
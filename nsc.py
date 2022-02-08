import string

def dec():
    number=list() #binary
    number1=list() #list for octal
    number2=list() #list for hexa
    while True: #check for valid input
        try:
            dec=dec1=dec2=input('\nInput decimal number: ')
            dec=int(dec)
            dec1=int(dec1)
            dec2=int(dec2)
            break
        except ValueError:
            print('Invalid input. Please try again.')
    while dec>=1:
        rem=dec%2 #get remainder
        if rem==0:
            number.append('0')
        else: #if remainder is not 1 or 0
            number.append('1')   
        dec=dec/2
        dec=int(dec) #convert float to int
    number.reverse() #reverse the list
    print('The binary value is: ',''.join(number))

    while dec1>=1: #convert to octal
        rem=dec1%8 #get remainder
        if rem>=1:
            number1.append(rem)
        elif rem==0:
            number1.append('0')
        else: #if remainder is not 1 or 0
            number1.append('1')   
        dec1=dec1/8
        dec1=int(dec1) #convert float to int
    number1.reverse() #reverse the list
    print('The octal value is: ',''.join(map(str, number1))) #output value

    while dec2>=1: #convert to hexa
        rem=dec2%16 #get remainder
        if rem<9 and rem>=1:
            number2.append(rem)
        elif rem==0:
            number2.append('0')
        elif rem==10:
            number2.append('A')
        elif rem==11:
            number2.append('B')
        elif rem==12:
            number2.append('C')
        elif rem==13:
            number2.append('D')
        elif rem==14:
            number2.append('E')
        elif rem==15:
            number2.append('F')
        else: #if remainder is not 1 or 0
            number2.append('1')   
        dec2=dec2/16
        dec2=int(dec2) #convert float to int
    number2.reverse() #reverse the list
    print('The hexadecimal value is: ',''.join(map(str, number2)),'\n\n') #output value

def bin():
    number=list()
    number1=list() #octal
    number2=list() #hexa
    binary=['1','0'] #binary inputs
    binarychecker=list()
    while True:
        try:
            bin=input('\nInput binary number: ') #input
            binarychecker=list(bin) #add input to list
            check=all(item in binary for item in binarychecker) #check if input is valid
            if check is True:
                break     
            else: 
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
    number=list(bin) #add input to list
    number.reverse() #reverse the list
    i=0
    result=0 #output and conversion to octal
    result1=0 #conversion to hexadecimal
    while i!=len(number):    
        digit=int(number[i]) #get the binary digit
        digit=digit*(2**i) #get the decimal value
        result+=digit #get the sum of the decimal values
        result1+=digit #get sum for hexadecimal conversion
        i+=1
    print('The decimal value is: ',result) #decimal
    while result>=1: #convert to octal
        rem=result%8 #get remainder
        if rem>=1:
            number1.append(rem)
        elif rem==0:
            number1.append('0')
        else: #if remainder is not 1 or 0
            number1.append('1')   
        result=result/8
        result=int(result) #convert float to int
    number1.reverse() #reverse the list
    print('The octal value is: ',''.join(map(str, number1))) #output value

    while result1>=1: #convert to hexa
        rem=result1%16 #get remainder
        if rem<9 and rem>=1:
            number2.append(rem)
        elif rem==0:
            number2.append('0')
        elif rem==10:
            number2.append('A')
        elif rem==11:
            number2.append('B')
        elif rem==12:
            number2.append('C')
        elif rem==13:
            number2.append('D')
        elif rem==14:
            number2.append('E')
        elif rem==15:
            number2.append('F')
        else: #if remainder is not 1 or 0
            number2.append('1')   
        result1=result1/16
        result1=int(result1) #convert float to int
    number2.reverse() #reverse the list
    print('The hexadecimal value is: ',''.join(map(str, number2)),'\n\n') #output value

def oct():
    number=list() #decimal
    number1=list() #binary
    number2=list() #hex
    octal=list(string.octdigits)
    octalchecker=list()
    while True:
        try:
            oct=input('\nInput octal number: ') #input
            octalchecker=list(oct) #add input to list
            check=all(item in octal for item in octalchecker) #check if input is valid
            if check is True:
                break     
            else: 
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
    number=list(oct) #add input to list
    number.reverse() #reverse the list
    i=0
    result=0
    dec=0
    dec1=0
    while i!=len(number):    
        digit=int(number[i]) #get the octal digit
        digit=digit*(8**i) #get the decimal value
        result+=digit #get the sum of the decimal values
        dec+=digit
        dec1+=digit
        i+=1
    #output decimal after binary

    while dec>=1: #convert to binary
        rem=dec%2 #get remainder
        if rem==0:
            number1.append('0')
        else: #if remainder is not 1 or 0
            number1.append('1')   
        dec=dec/2
        dec=int(dec) #convert float to int
    number1.reverse() #reverse the list
    print('The binary value is: ',''.join(number1))

    while dec1>=1: #convert to hexa
        rem=dec1%16 #get remainder
        if rem<9 and rem>=1:
            number2.append(rem)
        elif rem==0:
            number2.append('0')
        elif rem==10:
            number2.append('A')
        elif rem==11:
            number2.append('B')
        elif rem==12:
            number2.append('C')
        elif rem==13:
            number2.append('D')
        elif rem==14:
            number2.append('E')
        elif rem==15:
            number2.append('F')
        else: #if remainder is not 1 or 0
            number2.append('1')   
        dec1=dec1/16
        dec1=int(dec1) #convert float to int
    number2.reverse() #reverse the list

    print('The decimal value is: ',result)
    print('The hexadecimal value is: ',''.join(map(str, number2)),'\n\n') #output value

def hex():
    number=list() #decimal
    number1=list() #octal
    number2=list() #binary
    hexa=list(string.hexdigits)
    hexadecimalchecker=list()
    while True:
        try:
            hex=input('\nInput hexadecimal number: ').upper() #input
            hexadecimalchecker=list(hex) #add input to list
            check=all(item in hexa for item in hexadecimalchecker) #check if input is valid
            if check is True:
                break     
            else: 
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')
    number=list(hex) #add input to list
    number.reverse() #reverse the list
    i=0
    result=0
    dec=0
    dec1=0
    while i!=len(number):
        if number[i]=='A': #convert letters to numbers
            digit=10
        elif number[i]=='B': #convert letters to numbers
            digit=11
        elif number[i]=='C': #convert letters to numbers
            digit=12
        elif number[i]=='D': #convert letters to numbers
            digit=13
        elif number[i]=='E': #convert letters to numbers
            digit=14
        elif number[i]=='F': #convert letters to numbers
            digit=15
        else:
            digit=int(number[i]) #get the hexadecimal digit
        digit=digit*(16**i) #get the decimal value
        result+=digit #get the sum of the decimal values
        dec+=digit #to use for octal conversion
        dec1+=digit #to use for binary conversion
        i+=1
    #output decimal after binary
    

    while dec>=1: #convert to octal
        rem=dec%8 #get remainder
        if rem>=1:
            number1.append(rem)
        elif rem==0:
            number1.append('0')
        else: #if remainder is not 1 or 0
            number1.append('1')   
        dec=dec/8
        dec=int(dec) #convert float to int
    number1.reverse() #reverse the list
    #print octal after decimal
    

    while dec1>=1: #convert to binary
        rem=dec1%2 #get remainder
        if rem==0:
            number2.append('0')
        else: #if remainder is not 1 or 0
            number2.append('1')   
        dec1=dec1/2
        dec1=int(dec1) #convert float to int
    number2.reverse() #reverse the list
    print('The binary value is: ',''.join(number2))
    print('The decimal value is: ',result)
    print('The octal value is: ',''.join(map(str, number1)),'\n\n') #output value

def userinput(): #choose which number system to be converted
    counter=1
    while counter==1:
        digit=input('Number System Conversion\n[1] Binary\n[2] Decimal\n[3] Octal\n[4] Hexadecimal\n[5] Exit\nEnter your input: ')
        if digit=='1': #binary
            bin()
                       
        elif digit=='2': #decimal
            dec()
            
        elif digit=='3': #octal
            oct()
            
        elif digit=='4': #hex
            hex()
            
        elif digit=='5': #exit
            counter-=1
        else:
            print('Invalid Input')

userinput()
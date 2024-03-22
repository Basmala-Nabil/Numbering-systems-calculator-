#name:Rabab Mohamed Abd El-Gafour Okasha 
#name:Basmalah Nabil El-Said Muhammed 

def menu_1():
    print('* Numbering system converter *')
    print('A) Insert a new number')
    print('B) Exit program\n')
    
def menu_2():
        print('* Please select the base you want to convert a number from *')
        print('A) Decimal')
        print('B) Binary')
        print('C) Octal')
        print('D) Hexadecimal')
        
def menu_3():
        print('* Please select the base you want to convert a number to *')
        print('A) Decimal')
        print('B) Binary')
        print('C) Octal')
        print('D) Hexadecimal')
        
def get_user_choice(): # get user choice from menu1
     choice_1 = input("Please Enter Your Choice\n ").upper()
     return choice_1
    
def check_from_base_choice(from_base_choice):
    while from_base_choice not in ['A', 'B', 'C', 'D']: # if the input isn't one of the options tell user to insert a valid input.
          print('Please Insert a Valid Choice.\n').upper() # Ask for input again if invalid choice.
          from_base_choice = get_user_choice()
          menu_2()
 
def check_to_base_choice(to_base_choice):
    while to_base_choice not in ['A', 'B', 'C', 'D']: # if the input isn't one of the options tell user to insert a valid input.
         print('Please Insert a Valid Choice.\n').upper() # Ask for input again if invalid choice.
         to_base_choice = get_user_choice()
         menu_3()

def check_choice_menu_1(choice):
    while choice not in ['A', 'B']: # if the input isn't one of the options tell user to insert a valid input.
         print('Please Insert a Valid Choice.\n')
         menu_1()
         choice = get_user_choice() # Ask for input again if invalid choice.
    action_menu_1(choice)

def decimal_to_binary(num):
    binary=""
    while not num.isdigit():
        print ('please insert a valid number')
        num = input('Enter decimal number: ')
# Replacing each decimal digit to binary and concatenating the results
    while int(num) > 0 :
            remainder= int(num) % 2
            binary = str(remainder)+ binary
            num = int(num) // 2
    print('the binary representation is ',str(binary))


def decimal_to_octal(num):
    octal=""
    if int(num)==0:
        print('the octal representation is 0 ')
# Replacing each decimal digit to octal and concatenating the results
    while int(num)>0 :
        remainder= int(num)%8
        octal = str(remainder)+octal
        num = int(num)// 8
    print('the octal representation is ',str(octal))


def decimal_to_hexadecimal(num):
    hexadecimal=""
    if int(num)==0:
        print('the hexadecimal representation is ',num)
# Replacing each decimal digit to hexadecimal and concatenating the results
    while int(num)>0 :
        remainder= int(num) %16
        if  remainder== 10:
            remainder='A'
        elif remainder==11:
            remainder='B'
        elif remainder==12:
            remainder='C'
        elif remainder==13:
            remainder='D'
        elif remainder==14:
            remainder='E'
        elif remainder==15:
            remainder='F'    
        hexadecimal = str(remainder)+hexadecimal
        num =int(num) // 16

    print('the hexadecimal representation is ',str(hexadecimal))


def binary_to_decimal(num):
    decimal=0
    if int(num)==0:
        print('the decimal representation is ',num)
# Replacing each binary bit to decimal and concatenating the results
    for bit in range(len(num)):
        decimal +=  int(num[len(num)-1-bit])*(2**bit)
    print('the decimal representation is ',str(decimal))


def binary_to_octal(num):
    octal=''
# List of binary digits to their octal equivalents
    num_to_octa = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'}

# Padding the binary to ensure groups of 3 bits       
    while len(num) % 3 != 0:
        num = '0' + num
# Splitting the binary result into groups of 3 bits
    groups_of_three = [num[bit:bit+3] for bit in range (0, len(num),3)]
# Replacing each group of 3 bits to octal
    for group in groups_of_three:
        octal = octal + num_to_octa[group]
    print('the octal representation is ',str(octal))


def binary_to_hexadecimal(num):
    hexadecimal=''
# List of binary groups to their hexadecimal equivalents
    num_to_hexa = {
          '0000': '0', '0001': '1', '0010': '2', '0011': '3',
          '0100': '4', '0101': '5', '0110': '6', '0111': '7',
          '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
# Padding the binary result to ensure groups of 4 bits
    while len(num) % 4 != 0:
        num = '0' + num

# Splitting the binary result into groups of 4 bits
    groups_of_four = [num[bit:bit+4] for bit in range(0, len(num), 4)]

# Replacing each group of 4 bits to hexadecimal
    hexadecimal = ""
    for group in groups_of_four:
        hexadecimal = hexadecimal + num_to_hexa[group]
    print('the hexadecimal representation is ',str(hexadecimal))    
   

def octal_to_decimal(num):
    decimal=0
    if num==0:
        print('the octal representation is ',num)
# Replacing each octal digit to decimal and concatenating the results
    for digit in range(len(num)):
        decimal = decimal + int(num[len(num)-1-digit])*(8**digit)
    print('the decimal representation is ',str(decimal))
        

def octal_to_binary(num):
# List of octal digits to their binary equivalents  
    num_to_binary = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'}
    binary= ""
# Replacing each octal digit to binary and concatenating the results
    for digit in num:
        binary = binary + num_to_binary[digit]
    print('the binary representation is ',str(binary))


def octal_to_hexadecimal(num):
    binary = ""
# List of octal digits to their binary equivalents
    num_to_binary = {
          '0': '000', '1': '001', '2': '010', '3': '011',
          '4': '100', '5': '101', '6': '110', '7': '111'}

# list of binary groups to their hexadecimal equivalents
    binary_to_hexa = {
          '0000': '0', '0001': '1', '0010': '2', '0011': '3',
          '0100': '4', '0101': '5', '0110': '6', '0111': '7',
          '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

# Replacing each octal digit to binary
    for digit in num:
        binary = binary + num_to_binary[digit]

# Padding the binary result to ensure groups of 4 bits
    while len(binary) % 4 != 0:
        binary = '0' + binary
# Splitting the binary result into groups of 4 bits
    groups_of_four = [binary[bit:bit+4] for bit in range(0, len(binary), 4)]

# Replacing each group of 4 bits to hexadecimal
    hexadecimal = ""
    for group in groups_of_four:
        hexadecimal = hexadecimal + binary_to_hexa[group] 
    print('the hexadecimal representation is ',str(hexadecimal))


def hexadecimal_to_decimal(num): 
    decimal = 0
    if num == "0":
        print('The decimal representation is', num)
    else:
# Replacing each hexadecimal digit to decimal and concatenating the results
        for digit in range(len(num)):
            decimal += int(num[len(num) - 1 - digit], 16) * (16 ** digit)
        print('The decimal representation is', str(decimal))


def hexadecimal_to_binary(num):
    binary=''
# List of hexadecimal digits to their binary equivalents  
    num_to_binary = {
        '0':'0000', '1':'0001', '2':'0010','3':'0011'
    ,   '4':'0100', '5':'0101', '6':'0110','7':'0111'
    ,   '8':'1000', '9':'1001', 'A':'1010','B':'1011'
    ,   'C':'1100', 'D':'1101', 'E':'1110','F':'1111'}
# Replacing each hexa digit to binary    
    for digit in num:
        binary +=  num_to_binary[digit]
    print('the binary representation is ',binary)
        
        
def hexadecimal_to_octal(num):
    octal=''
    binary=''
# List of hexadecimal digits to their binary equivalents  
    num_to_binary = {
        '0':'0000', '1':'0001', '2':'0010','3':'0011'
    ,   '4':'0100', '5':'0101', '6':'0110','7':'0111'
    ,   '8':'1000', '9':'1001', 'A':'1010','B':'1011'
    ,   'C':'1100', 'D':'1101', 'E':'1110','F':'1111'}
# List of binary digits to their octal equivalents
    binary_to_octa = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'}
# Replacing each hexa digit to binary    
    for digit in num:
        binary = binary + num_to_binary[digit]
# Padding the binary result to ensure groups of 3 bits       
    while len(binary) % 3 != 0:
        binary = '0' + binary
# Splitting the binary result into groups of 3 bits
    groups_of_three = [binary[bit:bit+3] for bit in range (0, len(binary),3)]
# Replacing each group of 3 bits to octal
    for group in groups_of_three:
        octal = octal + binary_to_octa[group]
    print ('the octal represenation is ',str(octal))
    

def action_menu_2_3(num, from_base_choice, to_base_choice): # if conditions
    # If user choosed to convert a number to the same number system the output is the same num
    if from_base_choice == to_base_choice :
        print(num)
# If user choosed to convert a number from decimal (A) to ......
    if from_base_choice == 'A':
        if to_base_choice == 'B' : # binary
           decimal_to_binary(num)
        elif to_base_choice == 'C': # octal
            decimal_to_octal(num)
        elif to_base_choice == 'D': #hexa
            decimal_to_hexadecimal(num)
        
# If user choosed to convert a number from binary (B) to ......
    elif from_base_choice == 'B':
        if to_base_choice == 'A': # decimal
           binary_to_decimal(num)
        elif to_base_choice == 'C': # octal
            binary_to_octal(num)
        elif to_base_choice == 'D': # hexa
            binary_to_hexadecimal(num)
        
# If user choosed to convert a number from octal (C) to ......
    elif from_base_choice == 'C' :
        if to_base_choice == 'A': # decimal
            octal_to_decimal(num)
        elif to_base_choice == 'B': #binary
            octal_to_binary(num)
        elif to_base_choice == 'D': # hexa
            octal_to_hexadecimal(num)
        
# If user choosed to convert a number from hexa (D) to ......        
    elif from_base_choice == 'D':
        if to_base_choice == 'A': # decimal
            hexadecimal_to_decimal(num)
        elif to_base_choice == 'B': # binary
            hexadecimal_to_binary(num)
        elif to_base_choice == 'C': #octal
            hexadecimal_to_octal(num)
# If user did not choose one of the options 
    else:
        print('Please Select a Valid Choice.')

def action_menu_1(choice):
    if choice == 'A':
       num = input("Please Enter a Number:\n")
       menu_2()
       from_base_choice = get_user_choice()
       check_from_base_choice(from_base_choice)
       menu_3()
       to_base_choice = get_user_choice()
       check_to_base_choice(to_base_choice)
       action_menu_2_3(num, from_base_choice, to_base_choice)
       menu_1()
       choice = get_user_choice()
       action_menu_1(choice)
    elif choice == 'B':
        quit()
    else:
        print("Please Select a Valid Choice(A\B)\n")
        menu_1()
        choice = get_user_choice()
        check_choice_menu_1(choice)
    
def main():
    menu_1()
    choice = get_user_choice()
    action_menu_1(choice)

main()


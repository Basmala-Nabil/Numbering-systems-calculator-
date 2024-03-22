#name:Rabab Mohamed Abd El-Gafour Okasha 
#name:Basmalah Nabil El-Said Muhammed


import re # Library for re.match
# menu 1
def display_menu_1():
    print("Menu 1:")
    print("A. Insert a new number")
    print("B. Exist")
    
# menu 2
def display_menu_2():
    print("Please select the operation:")
    print("A. Compute one's complement")
    print("B. Compute two's complement")
    print("C. addition")
    print("D. subtraction\n")
    
def get_user_choice():
     choice_1 = input("Please Enter Your Choice\n ").upper()
     return choice_1

def check_choice_menu_1(choice):
    while choice not in ['A', 'B']:
         print('Please Insert a Valid Choice.\n')
         display_menu_1()
         choice = get_user_choice()
    perform_action_menu_1(choice)
    
# check a number is binary 
def validate_binary_number(number):
    pattern = r'^[01]+$'  # Regular expression pattern for binary numbers
    if re.match(pattern, number):
        return True
    else:
        return False

def insert_number(): # Ask the user to enter a valid binary until he enters a valid binary number
     num_2 = input("Please enter second  number \n")
     while not validate_binary_number(num_2):
        print("Please insert a valid binary number\n")
        num_2 = input("Please enter second number again\n")
     return num_2

def addition(num_1,num_2): 
        num_1 = str(num_1)
        num_2 = str(num_2)
        result = ""
        carry = 0
        i, j = len(num_1) - 1, len(num_2) - 1
        while i >= 0 or j >= 0 or carry != 0:
            sum = carry
            if i >= 0:
                sum += int(num_1[i])
                i -= 1
            if j >= 0:
                sum += int(num_2[j])
                j -= 1
            carry = sum // 2
            result = str(sum % 2) + result
        return result
    
def one_complement(number):
    result = ""
    for i in number:
        if i == '0':
            result += "1"
        else: 
            result += "0"
    return result
    
def two_complement(num_1):
    result = one_complement(num_1)
    result_twos_complement = addition(result,1)
    return  result_twos_complement
    
def subtraction(num_1,num_2):
    if int(num_1, 2) < int(num_2, 2): # if the second number is greater,  then it swaps the values of num_1 and num_2
        num_1, num_2 = num_2, num_1   # to get the subtraction be always positive
    num_1 = str(num_1)
    num_2 = str(num_2)
    result = ""
    borrow = 0
    i, j = len(num_1) - 1, len(num_2) - 1
    while i >= 0 or j >= 0 or borrow != 0:
        diff = borrow
        if i >= 0:
            diff+= int(num_1[i])
            i -= 1
        if j >= 0:
            diff -= int(num_2[j])
            j -= 1
        if diff <0:
            borrow=1
        else :
            borrow=0
        result = str(diff % 2) + result
    return result

def perform_action_menu_2(choice,num_1):
    if choice == 'A':
         result_one_complement = one_complement(num_1)
         print(f'Result of ones complement = {result_one_complement}\n')
    elif choice == 'B':
          result_two_complement = two_complement(num_1)
          print(f'Result of twos complement = {result_two_complement}\n')
    elif choice == 'C':
         num_2 = insert_number()
         sum = addition(num_1,num_2)
         print(f'Sum = {sum}\n')
    elif choice == 'D':
         num_2 = insert_number()
         sub = subtraction(num_1,num_2)
         print(f'Subtraction = {sub}\n')
    main()
        
def perform_action_menu_1(choice):
    if choice == 'A':
        num_1 = input("Please Enter First Number:\n")
        while not validate_binary_number(num_1): # Ask the user to enter a valid binary until he enters a valid binary number
            print("Please insert a valid binary number.\n")
            num_1 = input("Please Enter First Number Again\n")
        display_menu_2()
        choice = get_user_choice()
        perform_action_menu_2(choice,num_1)
    elif choice == 'B':
         quit()
    else:
        print("Please select a valid choice(A\B) \n")
        display_menu_1()
        choice = get_user_choice()
        check_choice_menu_1(choice)
        
def main(): # main function contains other functions in sequence
    display_menu_1()
    choice = get_user_choice()
    perform_action_menu_1(choice)
    
main()
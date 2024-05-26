problem_1:

Numbering System Converter:

-Menu 1:

   Presents the user with options to either insert a new number or exit the program.
   
-Menu 2: 

   Asks the user to select the base (Decimal, Binary, Octal, Hexadecimal) of the number they want to convert from.
   
-Menu 3: 

   Asks the user to select the base they want to convert the number to.


 
Conversion Functions: 

 Includes several functions to handle conversions between different numbering systems:
 
   -decimal_to_binary, decimal_to_octal, decimal_to_hexadecimal: Convert from decimal to other bases.
  
   -binary_to_decimal, binary_to_octal, binary_to_hexadecimal: Convert from binary to other bases.
  
   -octal_to_decimal, octal_to_binary, octal_to_hexadecimal: Convert from octal to other bases.
  
   -hexadecimal_to_decimal, hexadecimal_to_binary, hexadecimal_to_octal: Convert from hexadecimal to other bases.

  
Flow Control Functions:

   -get_user_choice, check_from_base_choice, check_to_base_choice, check_choice_menu_1: Handle user input and validation for choices in the menus.
 
   -action_menu_2_3: Executes the appropriate conversion based on user input.
 
   -action_menu_1: Handles the main flow of Menu 1.


 
Binary Operations:

 -Menu 1:
 
   Presents the user with options to insert a new number or exit.


 -Menu 2:
 
  Asks the user to select the operation (One's Complement, Two's Complement, Addition, Subtraction).


Binary Validation Function:

   -Validates whether the input is a binary number.



Binary Operation Functions:

   -one_complement, two_complement, addition, subtraction: Perform binary operations.

 
Flow Control Functions:

   -perform_action_menu_1, perform_action_menu_2:
   
   Handle user input and execution of the selected binary operation.















problem_2:




Numbering System Converter:
   This part of the program converts numbers between different numbering systems: Decimal, Binary, Octal, and Hexadecimal.

-Functions and Flow
   Menu Functions:

   -menu_1():
   
   Displays the main menu options to insert a new number or exit the program.
    
   -menu_2(): 
   
   Displays options to select the base of the number to convert from.
   
   -menu_3(): 
   
   Displays options to select the base to convert the number to.

   
   
User Choice Functions:

  -get_user_choice():  
  
   Gets the user's choice from the current menu and converts it to uppercase for uniformity.
   
-check_from_base_choice(from_base_choice), check_to_base_choice(to_base_choice): 

Validate the user's base selection and prompt for a valid choice if needed.

-check_choice_menu_1(choice):
Ensures the user enters a valid choice in the main menu and calls action_menu_1 with the validated choice.

-Conversion Functions:

These functions handle conversions between different numbering systems.

-decimal_to_binary(num), decimal_to_octal(num), decimal_to_hexadecimal(num): Convert from Decimal to Binary, Octal, or Hexadecimal respectively.

-binary_to_decimal(num), binary_to_octal(num), binary_to_hexadecimal(num): Convert from Binary to Decimal, Octal, or Hexadecimal respectively.

-octal_to_decimal(num), octal_to_binary(num), octal_to_hexadecimal(num): Convert from Octal to Decimal, Binary, or Hexadecimal respectively.

-hexadecimal_to_decimal(num), hexadecimal_to_binary(num), hexadecimal_to_octal(num): Convert from Hexadecimal to Decimal, Binary, or Octal respectively.



Action Functions:

-action_menu_2_3(num, from_base_choice, to_base_choice): Performs the conversion based on user choices.

-action_menu_1(choice): Handles the main flow of the program, guiding the user through menus and calling appropriate functions based on the user's choices.



Main Function:

-main():

Starts the program by displaying the main menu and getting the user's choice.

Binary Operations:

This part of the program allows users to perform various binary operations such as computing one's complement, two's complement, addition, and subtraction.


Functions and Flow
Menu Functions:

-display_menu_1():

Displays the main menu options to insert a new number or exit.

-display_menu_2(): 

Displays options to select the binary operation to perform.



User Choice Functions:

-get_user_choice(): 

Gets the user's choice from the current menu and converts it to uppercase.

-check_choice_menu_1(choice): 

Ensures the user enters a valid choice in the main menu and calls perform_action_menu_1 with the validated choice.



Validation Functions:

-validate_binary_number(number):

Uses a regular expression to check if the input is a valid binary number.

-insert_number(): 

Asks the user to enter a valid binary number until a valid input is provided.



Binary Operation Functions:

-one_complement(number):

Computes the one's complement of a binary number.

-two_complement(num_1):

Computes the two's complement of a binary number.

-addition(num_1, num_2):

Adds two binary numbers.

-subtraction(num_1, num_2):

Subtracts one binary number from another, ensuring the result is always positive.




Action Functions:


-perform_action_menu_2(choice, num_1): 

Performs the selected binary operation based on the user's choice.

-perform_action_menu_1(choice): 

Handles the main flow of the program, guiding the user through menus and calling appropriate functions based on the user's choices.



Main Function:

-main():

Starts the program by displaying the main menu and getting the user's choice.


Overall Flow:

The user starts by running the main() function, which displays the main menu of the numbering system converter.
Based on the user's choice, they can either insert a new number for conversion or exit the program.
If the user chooses to insert a new number, they are guided through selecting the base to convert from and the base to convert to.
The appropriate conversion function is called to perform the conversion, and the result is displayed.
The user is then returned to the main menu to choose again.



For the binary operations:

The user starts by running the main() function, which displays the main menu of the binary operations program.
Based on the user's choice, they can either insert a new binary number for operations or exit the program.
If the user chooses to insert a new number, they are guided through selecting the binary operation to perform.
The appropriate binary operation function is called to perform the operation, and the result is displayed.
The user is then returned to the main menu to choose again.

 
insert_number: 

 -Asks for a valid binary number input.

This problem required me to implement a program that prompts the use for an arithmetic expression and calculates and outputs the result as a floating-point value formatted to one decimal place. For example,if the user inputs 1 + 1, the program should output 2.0.

When I saw the problem, I realised that I needed a command that could split the user input into operand 1, operator and operand 2. I also understood that the program had to check the operator and decide what operation to implement.

I started the program with a prompt asking user to enter a basic arithmetic operation. In the second lie, I achieved the splitting of user input using .split() command. By default, the command splits the specified string using the whitespace into a list.

Next, I used a series of conditional statements to check the operator and determine the mathematical operation to be performed. Each conditional statement started by checking the element on index 1 of the string(which should be the operator). Then the other elments were changed to integers. The variable 'expression' now stored the value of the mathematical operation performed and the value displayed by print is formated to float.

The program was tested with: 1 + 1, 2 / 2, 100 * 3
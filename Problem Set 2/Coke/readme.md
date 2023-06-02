Thsi program required me to implement a program that behaved like a coke vending machine. The prie for coke was 50 cents. The program prompted user for a coin between 25, 10 and 5 cents, one at each time an each time informing the user of the amount due. Once teh user has inputted at least 50 cents, the change owed to user is outputted. Any input that is not accepted coin dnominaton is ignored.

When I encountered this problem, I understood that I needed to implement a while loop because I needed to iterate until the user had inputted at least 50 cents.

I started the program by initialising 'Amount' as 50 cents then on line 2, I simply outputted the amount due to the user. In line 3, I started my iteration. 

I basically told my program that while 'Amount' was greater that 0, it should prompt the user for an input with 'Insert Coin: ' and store the input in coin. Using Match-Case conditional, the program checked whether the value of 'coin' was 25 or 10 0r 5(Line 6), if so, the program then proceeded to check if the coin value was greater than present AMount using 'if' statement. If the coin was greater than Amount the program should output the change owed to user as present amount. then stop break out of the loop with the break statement(Line 9).

If the coin was not Greater that amount then th program continued to subtract the inputted value of coin from the current Amount and assigned the new value to Amount. If the resulting amount was 0, the the program would output change owed as 0 else the program prints Amount due as the new value of Amount from line 11.

Under case _, the program I told my program that if the coin as neither 25 0r 10 or 5, Amount Due shuld be outputted the same.

Problems Encoutered while running/testing the program:

Test cases: [25, 25]. [15, 30, 10, 10, 10, 10, 10, 15.]
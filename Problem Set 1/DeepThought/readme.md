This problem required that the user provided the answer to the Great Question then display YES if the answer provided was correct or NO if the answer provided was wrong.
I knew the problem required conditinals. I first tried using Match Case conditional but I experienced an error. When the user input was 42, the program output was NO. When I made the input an interger, I still experienced errors so I used If, Elif and Else instead.

I started the code by prompting user for input with "What is the Answer to the Great Question of life? ". In line 2, I made the input value lowercase with .lower() command so that user's input case would not affect the working of the code.

Next I used a conditional to say, If the value stored in question was equal to fourty two or fourty-two then 'Yes' should be displayed. In line 5, if the value stored in 'question' is typecasted to integer and it is equal to '42', 'Yes' is also printed. If none of these conditions are met, 'No' is displayed on the screen.

The program was tested with: 42, Fourty-Two, fourty two.
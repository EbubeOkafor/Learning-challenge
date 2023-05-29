The program required me to implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. it doesn't output anything if it is not time for a mmeal. The user's input will be formatted in 24-hour time as #:## or ## and aech meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

I structured my

 program, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

I started by defining main() function. In the main() fuction, I prompted the user for input. The convert () function was calked on the user input. Then usin a series of conditionals, I checked the conditions and made the program diaplay the required output.

In the convert () function, I passed an argument 'time'. I changed it to a list using .split() command. Then I casted each element of the list to float and performed mathematical operations on the resulting value to change time to the float which would be returned to the main function.

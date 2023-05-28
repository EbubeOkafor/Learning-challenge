This problem required me to create an emoticon to emoji converter.
I decided to use a user defined function convert() to impement the program. This function did the conversion while main() function called it on the input given.

I gave the function an argument 'word'. When the input from line 7 in main() is stored, the string ':)', if present in the input, would be replaced with a happy face using the .replace() command(Line 2). Also if ':(' is present in the input, it ould be replace with a sad face(Line 3).
In line 4, the print() would display the converted string to the sceen. This way, when convert() is called in main(), after conversion of emoticon, the new statement is displayed.
In the main(), the user input is stored in 'faces'. Then 'faces' is used as the agument for convert() in line 8.

The program was tested with: I am happy :), I am sad ;(.
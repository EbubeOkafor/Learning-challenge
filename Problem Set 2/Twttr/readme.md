This program required me to implement program that prompts user for a string and outputs the string with all vowels omitted.
When i saw this pproblem hat came to my mind was that I needed to iterte through the user's input with for loop and replace vowels with .replace() command.

I start the program by creating a list called 'vowel' that contains all vowels in English language. The next line, prompts user for a input. in line 3, I convert the input to lowercase and assign the modified value back to 'text'.

In line 4, I start iterating through user's input using 'for' loop. The program is told that for every character, i, in 'text', if the character is in the list 'vowel'(line 5) then that character should be replaced with '""' which basically means 'nothing', hence tha character is removed.

In line 7, outside the loop, the modified text is outputted to the user.
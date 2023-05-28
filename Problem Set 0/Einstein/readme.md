This problem required that a user inputs mass and the value of Energy will be output using einstein's equation.
This problem was straightfoward for me. First of all, I initiated the value of 'c' since it was a constant(line 1). 
Next, I prompted the user to enter the value of mass to be worked with. Since input() always returned the value of input as string, I used the int() to cast from str to int so that mathemaical operations could be carried out without errors(Line 2).
After that I created a variable 'E' and assigned 'm*c**2' to it(Line 3). This line simply represented einsteins equation, E = mc^2.
Finally, the mathematical operaton was performed and the value of 'E' is displayed on screen as "Energy is: 'value of E".

The program was tested with: 1(kg)
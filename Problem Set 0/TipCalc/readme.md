This program is to program a calculator used to calculate tips for servers in a restaurant.
The program already had the main(), dollars_to_float() and percent_to_float functions defined. Although the main() function had been written and called, I was expected to write the programs under the other two functions that would make the main() function work as expected.

The format of the input for the price of the meal was $#.## and the format for the tip percentage is #% (where # is a digit).

When I saw the problem I knew that what I had to do was to get rid of $ and % and put the resulting values back in the main() function so that mathemathical operation could be carried out on the inputs.

Since my focus in this problem was the programs in the function, I started the code solution by discarding the $ in the value of argument "d" (in dollars_to_float() funtion). The value of "d" will come from the input prompt in line 3. $ was discarded using .replace command(line 9). After discarding $, I proceeded to return the value of "d" (now typecasted to float) back to the main() function.
In percent_to_float() function, I discarded the % in the value of argument "p" also using .replace() command(Line 13). "p" was then typecasted to float and divided by 100 to convert the percent to float. the value gotten was then assigned to "p". The value of "P" was returned to main() function.

The program was tested with: $500, %15.
from pyfiglet import figlet_format
import sys
from random import choice

if len(sys.argv) > 3:
    sys.exit("Greater argument")


if len(sys.argv) == 0:
    result = input("fff: ")
    result = figlet_format(result, font ="slant")
    print(result)


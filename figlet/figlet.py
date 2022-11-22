from pyfiglet import Figlet
import random as r
import sys

figlet = Figlet()

rf = r.choice(figlet.getFonts())


if len(sys.argv) == 1:
    i = input("Input: ")
    figlet.setFont(font=rf)
    print("Output: " + figlet.renderText(i))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in figlet.getFonts()):
    i = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output: " + figlet.renderText(i))
else:
    sys.exit("Invalid usage")


        
import sys
import os
from PIL import Image
from PIL import ImageOps

try:
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        i = os.path.splitext(sys.argv[1])
        o = os.path.splitext(sys.argv[2])
        if not i[1] == ".png" and not i[1] == ".jpg" and not i[1] == ".jpeg":
            sys.exit("Invalid input")
        elif not o[1] == ".png" and not o[1] == ".jpg" and not o[1] == ".jpeg":
            sys.exit("Invalid output")
        elif o[1] != i[1]:
            sys.exit("Input and output have different extensions")
        elif os.path.isfile(sys.argv[1]) is False:
            sys.exit("Input does not exist")
        else:
            person = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            width, height = shirt.size
            p = ImageOps.fit(person, (width, height))
            p.paste(shirt, (0, 0), shirt)
            p.save(
                sys.argv[2]
            )

except FileNotFoundError:
    sys.exit("File does not exist")
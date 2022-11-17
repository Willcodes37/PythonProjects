import csv
import sys
import os

first_last_house = []
if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if os.path.isfile(sys.argv[1]) is False:
        sys.exit("Could not read " + sys.argv[1])
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row['name'].split(",")
                house = row['house']
                first_last_house.append([first.lstrip(), last, house])

        with open(sys.argv[2], "w") as file1:
            writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in first_last_house:
                writer.writerow({"first": row[0], "last": row[1], "house": row[2]})
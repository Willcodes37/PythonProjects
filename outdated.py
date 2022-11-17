while True:
    date = input("Date: ").strip()

    Months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }
    d = "0"
    if date[1] == "/" or date[2] == "/":
        ds = date.split("/")
        dsi = int(ds[0])
        dsi2 = int(ds[1])
        if (len(ds[0]) == 1 or len(ds[0]) == 2) and (len(ds[1]) == 1 or len(ds[1]) == 2) and len(ds[2]) == 4:
            if 1 <= dsi <= 12 and 1 <= dsi2 <= 31:
                if 1 <= dsi <= 9 and 1 <= dsi2 <= 9:
                    dm = d + ds[0]
                    dd = d + ds[1]
                    print(ds[2], dm, dd, sep="-")
                    break
                elif 1 <= dsi <= 9:
                    dm = d + ds[0]
                    print(ds[2], dm, ds[1], sep="-")
                    break
                elif 1 <= dsi2 <= 9:
                    dd = d + ds[1]
                    print(ds[2], ds[0], dd, sep="-")
                    break
                else:
                    print(ds[2], ds[0], ds[1], sep="-")
                    break
            else:
                pass
        else:
            pass
    elif date[-6] == ",":
        ds = date.split(" ")
        ds2 = ds[1].replace(",", "")
        if len(ds2) == 1 or len(ds2) == 2:
            ds2i = int(ds2)
            ds3 = d + ds2
            if (len(ds[1]) == 1 or len(ds[1]) == 2) and len(ds[2]) == 4:
                if 1 <= ds2i <= 31:
                    if ds[0] in Months:
                        M = Months.get(ds[0])
                        print(ds[2], M, ds3, sep="-")
                        break
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
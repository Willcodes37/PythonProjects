import re


def main():
    print(parse(input("HTML: ")))


def parse(s):

    x = re.search(r"(https|http)://(www\.)?(youtube\.com)/embed/(\w+)", s)

    if x:
        if not s.startswith("<iframe") and not s.endswith("></iframe>"):
            return None
        else:
            return f"https://youtu.be/{x.group(4)}"
    else:
        return None


if __name__ == "__main__":
    main()
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")

# matches = re.search(r"^(.+), *(.+)$", name) ? allows space and no space * allows only one

# if matches:

# last, first = matches.groups()
# name = f"{first} {last}"
# last = matches.group(1)
# first = matches.group(2)
# name = f"{first} {last}"

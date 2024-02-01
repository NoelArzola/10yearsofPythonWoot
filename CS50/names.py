names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# name = input("What's your name? ")

# file = open("names.text", "a")

# with open("names.text", "a") as file:
#     file.write(f"{name}\n")

# with open("names.text", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

# for line in lines:
#     print("hello", line)
# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")
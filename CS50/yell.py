def main():
    yell("This", "is", "CS50")

def yell(*words):
    # uppercased = map(str.upper, words) MAP
    uppercased = [word.upper() for word in words] # LIST COMPREHENSION
    print(*uppercased)


if __name__ == "__main__":
    main()
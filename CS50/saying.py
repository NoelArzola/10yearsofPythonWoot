import sys

def main():
    if len(sys.argv) == 2:
        hello(sys.argv[1])
        goodbye(sys.argv[1])
    else: 
        print("Too few arguments, exiting")
        exit()

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()
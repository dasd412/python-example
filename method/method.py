import sys


def greet(*names):
    for name in names:
        print(f"Hello, {name}!")


def main():
    greet("a", "b", "c")


if __name__ == "__main__":
    main()

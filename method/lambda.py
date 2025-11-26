def main():
    add = lambda x, y: x + y
    result = add(3, 5)
    print(result)

    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)

    numbers = [i for i in range(0, 11)]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)


if __name__ == "__main__":
    main()

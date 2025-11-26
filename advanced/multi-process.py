import multiprocessing


def square(x):
    return x * x


def main():
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square, range(10))
    print(results)


if __name__ == "__main__":
    main()

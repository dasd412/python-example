def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result

    return wrapper


@decorator_function
def say_hello(message):
    print(message)


def main():
    say_hello("Hello!")


if __name__ == "__main__":
    main()

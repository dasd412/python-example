import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def large_data_processing():
    def data_generator(size):  # 제너레이터는 모든 값을 한 번에 메모리에 올리지 않고, 필요할 때 값을 생성하여 메모리 사용을 최적화한다.
        for i in range(size):
            yield i
    total = 0
    for value in data_generator(10 ** 6):
        total += value
    return total


def main():
    result = large_data_processing()
    print(result)


if __name__ == "__main__":
    main()

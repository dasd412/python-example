import threading

lock = threading.Lock()
counter = 0


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


def main():
    threads = []

    for _ in range(2):
        t = threading.Thread(target=increment_counter())
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value: {counter}")


if __name__ == "__main__":
    main()

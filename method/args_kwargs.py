import sys


def greet_args(*names): # 위치 인자 가변 매개변수
    for name in names:
        print(f"Hello, {name}!")

def greet_kwargs(**info): # 키워드 인자 가변 매개변수
    for key,value in info.items():
        print(f"{key}: {value}")
def main():
    greet_args("a", "b", "c")
    greet_kwargs(name="Alice",age=30)

if __name__ == "__main__":
    main()

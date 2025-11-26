class Person:
    species = "Homo sapiens"  # 클래스 변수 (모든 인스턴스가 공유하는 변수)

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 (각 객체마다 별도로 유지돠눈 변수)
        self.age = age  # 인스턴스 변수 (각 객체마다 별도로 유지돠눈 변수)

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # 클래스 메소드는 클래스 자체에 속하며, 클래스 변수에 접근할 수 있다.
    @classmethod
    def species_info(cls):
        print(f"Species : {cls.species}")


class MathOperations:
    # 클래스나 인스턴스와 상관없이 동작하는 메서드가 스태틱 메서드
    @staticmethod
    def add(a, b):
        return a + b


def main():
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    person1.greet()
    person2.greet()

    print(person1.species)
    print(person2.species)

    print(person1.name)
    print(person2.name)

    Person.species_info()

    result = MathOperations.add(5, 3)
    print(result)


if __name__ == "__main__":
    main()

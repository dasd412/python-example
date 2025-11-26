class Person:
    def __init__(self, name, age):
        self.__name = name  # private 변수
        self.__age = age  # private 변수

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise ValueError("Invalid age")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id


def main():
    person = Person("Alice", 30)
    print(person.get_name())  # Alice
    print(person.get_age())  # 30

    person.set_name("Bob")
    person.set_age(25)
    print(person.get_name())  # Bob
    print(person.get_age())  # 25

    employee = Employee("July", 35, "E1234")
    print(employee.get_name())
    print(employee.get_age())
    print(employee.get_employee_id())


if __name__ == "__main__":
    main()

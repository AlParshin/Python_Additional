# Создайте класс студента.
# Используя дескрипторы, проверяйте ФИО на первую заглавную букву и наличие только букв.

class IncorrectName(ValueError):
    def __str__(self) -> str:
        return "Валидация данных провалена! Ошибка в формате ФИО!"


class CheckNameDescriptor:
    Z

    def __init__(self):
        self.__fio = 0

    def __get__(self, instance, owner):
        return self.__fio

    def __set__(self, instance, value):
        if not (str.istitle(value[0])) or not (str.isalpha(value)):
            raise IncorrectName
        self.__fio = value


class Student:
    name = CheckNameDescriptor()
    surname = CheckNameDescriptor()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"


st_1 = Student("Анатолий", "Иванов")
st_2 = Student("Дмитрий", "Сидоров")
st_3 = Student("Борис", "Петров")
st_4 = Student("жорик", "Вартанов")
st_5 = Student("Ибрагим", "Гегельшм@н")
st_6 = Student("василий", "васе4кин")
st_7 = Student("Маргарита", "Кюкюкюштова")
print("Ошибка не вызвана, значит все студенты успешно прошли валидацию!")

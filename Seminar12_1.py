# Создайте класс студента.
# Используя дескрипторы, проверяйте ФИО на первую заглавную букву и наличие только букв.

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        if str.istitle(self.name[0]) and str.istitle(self.surname[0]) and str.isalpha(self.name) and str.isalpha(self.surname):
            """Валидация данных пройдена, все прекрасно!"""
            Students.add(self)
        else:
            """Валидация данных провалена, а это не очень хорошо!"""
    
    def __repr__(self):
        return f"{self.name} {self.surname}"

class Students:
    lst = []
    def add(student):
        Students.lst.append(student)
  
st_1 = Student("Анатолий", "Иванов")
st_2 = Student("Дмитрий", "Сидоров")
st_3 = Student("Борис", "Петров")
st_4 = Student("жорик", "Вартанов")
st_5 = Student("Ибрагим", "Гегельшм@н")
st_6 = Student("василий", "васе4кин")
st_7 = Student("Маргарита", "Кюкюкюштова")
print("Нормальные студенты, прошедшие валидацию данных:")
print(Students.lst)
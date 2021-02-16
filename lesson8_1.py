# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Mydate:

    def __init__(self):
        self.mydate = ""

    def setmydate(self, mydate):
        self.mydate = mydate

    @classmethod
    def set_my_date(cls, mydate):
        return cls(mydate)

    @staticmethod
    def my_validation(my_chek_date):
        print (my_chek_date)
        d, m, y = my_chek_date
        if m < 13:
            if m in (1, 3, 5, 7, 8, 10, 12) :
                if d > 31:
                    return f'Не правильно введен "день"{d} имеет место превышение'
                else:
                    return "Все правильно"
            elif m in (4, 6, 9, 11):
                if d > 30:
                    return f'Не правильно введен "день"{d} имеет место превышение'
                else:
                    return "Все правильно"
            elif m == 2:
                if y % 4 == 0:
                    if d > 29:
                        return f'Не правильно введен "день"{d} имеет место превышение'
                    else:
                        return "Все правильно"
                else:
                    if d > 28:
                        return f'Не правильно введен "день"{d} имеет место превышение'
                    else:
                        return "Все правильно"
        else:
            return f'Не правильно введен "месяц" {m} имеет место превышение'

    @classmethod
    def get_dmy(cls, mydate):

        dates = str(mydate).split("-")
        if len(dates) != 3:
            return f"непрвыильный формат данных {mydate}, не соответсвует типу  «день-месяц-год»."
        elif len(dates[0]) != 2:
            return f"непрвыильный формат данных {dates[0]}, не корректно введен «день»"
        elif len(dates[1]) != 2:
            return f"непрвыильный формат данных {dates[1]}, не корректно введен «месяц»"
        elif len(dates[2]) != 4:
            return f"непрвыильный формат данных {dates[2]}, не корректно введен «год»"
        else:
            day = 0
            if dates[0][0] == "0":
                if dates[0][1].isnumeric():
                    day = int(dates[0][1])
                else:
                    return f"введен не числовой формат для значения дня - {dates[0]}"
            else:
                if dates[0].isnumeric():
                    day = int(dates[0])
                elif dates[0].isnumeric():
                    day = int(dates[0])
                else:
                    return f"введен не числовой формат для значения дня - - {dates[0]}"
            month = 0
            if dates[1][0] == "0":
                if dates[1][1].isnumeric():
                    month = int(dates[1][1])
                elif dates[1].isnumeric():
                    month = int(dates[1])
                else:
                    return f"введен не числовой формат для значения месяца - {dates[1]}"
            else:
                if dates[1].isnumeric():
                    month = int(dates[0])
                else:
                    return f"введен не числовой формат для значения месяца - - {dates[1]}"
            year = 0
            if dates[2][0] == "0":
                if dates[2][1].isnumeric():
                    year = int(dates[2][1])
                else:
                    return f"введен не числовой формат для значения год - {dates[2]}"
            else:
                if dates[2].isnumeric():
                    year = int(dates[2])
                else:
                    return f"введен не числовой формат для значения год - - {dates[2]}"

            print(cls.my_validation((day, month, year)))



print(Mydate.get_dmy("30-02-2014"))
#print(Mydate.get1())
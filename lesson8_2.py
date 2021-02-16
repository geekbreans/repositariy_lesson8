# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class MyOwnerErr(Exception):
    def __init__(self, txt):
        self.txt = txt

in_data = input("Enter namber > 0, non 0 :" )
in_data = int(in_data)
m_data =100
i_data = 0
try:

    if in_data == 0:
        raise MyOwnerErr("Не должно быть нулем ")
    i_data = m_data/ in_data

except (ZeroDivisionError, MyOwnerErr) as err:
    print(err)
else:
    print(i_data)
finally:
    print("Ok")







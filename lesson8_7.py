# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class mComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self,other):
        return mComplex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)

    def __add__(self, other):
        return mComplex( self.a + other.a, self.b + other.b)

    def __str__(self):
        return str(self.a) + " + " + "i" + str(self.b)


k1 = mComplex(2, 3)
print(k1)
k2 = mComplex(7, 1)
print(k2)

print(k1 + k2)
print (k1*k2)






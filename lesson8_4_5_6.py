# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


# Склад это ряды стелажей, стелаж имеет полки, на каждой полке имеются места - по сути это ячейки стремя координатам
# объекты хранения располагаются в ячкейках
# подразделение по сути тот же склад
# склад имееет методы добавить в склад объект, удплить из склада объектб количество объектов с определенным типом (именем) на складе


class officEquipmentwarehouse:

    def __init__(self, warehouseparametrs):
        M, H, L = warehouseparametrs
        self.warehouseparametrs = warehouseparametrs
        self.M = M
        self.H = H
        self.L = L
        self.W_cells = []
        self.wellsWithpallet = {}

    def setNewcells(self):

        m = 0
        h = 0
        l = 0

        while m < self.M:
            h = 0
            while h < self.H:
                l = 0
                while l < self.L:
                    if not (m, h, l) in self.W_cells:
                        self.W_cells.append((m, h, l))
                        return m, h, l
                        l = self.L
                        h = self.H
                        m = self.M
                    else:
                        l = l + 1

                h = h + 1
            m = m + 1

    def countValue(self, el_value):

        n = 0
        for k, v in self.wellsWithpallet.items():
            if v == el_value:
                n = n + 1
        return n

    def addObjectinwarehouse(self, m_object):

        mycells = self.setNewcells()
        self.wellsWithpallet[mycells] = m_object.name

    def deldObjectinwarehouse(self, m_namet , n_value):

        m_list = []
        m = 0
        n = 0
        if self.countValue(m_namet) < n_value:
            m = self.countValue(m_namet)
        else:
            m = n_value

        for k, v in self.wellsWithpallet.items():
            if v == m_namet:
                m_list.append(k)
                n = n + 1
                if n == m:
                    break

        for el in m_list:
            self.W_cells.remove(el)
            del self.wellsWithpallet[el]

    def moveObjecttosubdivision(self, m_object, m_division, n_value):

        m = 0
        n = 0
        if self.countValue(m_object.name) < n_value:
            m = self.countValue(m_object.name)
        else:
            m = n_value
        #m = self.countValue(m_object.name)

        while n < m:
            m_division.addObjectinwarehouse(m_object)
            n = n + 1

        n = 0
        self.deldObjectinwarehouse(m_object.name, m)
        # while n < m:
        #     self.deldObjectinwarehouse(m_object.name, )
        #     n = n + 1


class subdivisionBig(officEquipmentwarehouse):

    def __init__(self, warehouseparametrs):
        officEquipmentwarehouse.__init__(self, warehouseparametrs)

    def setname(self, name):
        self.name = name


class officeEquipment():
    # s_value количество объектов которые размещаются на палете
    def __init__(self):
        self.s_value = 0
        self.model = ""
        self.name = ""

    def palletvalue(self, s_value):
        self.s_value = s_value

    def setname(self, name):
        self.name = name

    def setmodel(self, model):
        self.model = model

    def __add__(self, other):
        RetofficeEquipment = officeEquipment()
        RetofficeEquipment.s_value = self.s_value + other.s_value
        return RetofficeEquipment

    def __str__(self):
        return str(self.s_value)


class Printer(officeEquipment):

    def __init__(self):
        officeEquipment.__init__(self)
        self.papirformat = ""

    def __str__(self):
        return str(self.s_value)

    def setpapirformat(self, papirformat):
        self.papirformat = papirformat


class Scanner(officeEquipment):

    def __init__(self):
        officeEquipment.__init__(self)
        self.dpi = 0

    def __str__(self):
        return str(self.s_value)

    def setdpi(self, dpi):
        self.dpi = dpi


class Xerox(officeEquipment):

    def __init__(self):
        officeEquipment.__init__(self)
        self.papirinsec = 0

    def __str__(self):
        return str(self.s_value)

    def setpapirinsec(self, papirinsec):
        self.papirinsec = papirinsec


class subdivision():

    def __init__(self, name):
        self.name = name
        self.s_value = 0
        self.Equipment = []

    def addEquipment(self, m_object):
        self.Equipment.append(m_object)


p = Printer()
p.palletvalue(1)
p.name = "Принтер"
print(p)
s = Scanner()
s.name = "Сканер"
s.palletvalue(10)
print(s)
x = Xerox()
x.name = "Xerox"
x.palletvalue(100)
print(x)

print(p + s + x)

sklad = officEquipmentwarehouse([7, 7, 7])


sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(x)
sklad.addObjectinwarehouse(s)
sklad.addObjectinwarehouse(p)
sklad.addObjectinwarehouse(p)

sklad.deldObjectinwarehouse(p.name, 1)

sklad.addObjectinwarehouse(p)
print("Оборудование на складах до перемещения ----------------------------------")
print(sklad.wellsWithpallet)

# объявляем подразделение
d = subdivisionBig([3, 3, 3])


sklad.moveObjecttosubdivision(p, d, 4)
print("Оборудование в подразделении----------------------------------")
print(d.wellsWithpallet)
print("Оборудование на складах----------------------------------")
print(sklad.wellsWithpallet)

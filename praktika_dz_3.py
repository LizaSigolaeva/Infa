"""ДЗ №3,создание класса"""
class Cake():
    """описание торта"""
    def __init__(self,filling,price):
        self.filling=filling
        self.price=price
    def bake(self):
        """печем торт"""
        print("Торт c начинкой "+self.filling + " стоимостью " + str(self.price)+ " приготовлен.")
        
Cake1=Cake("Вишня",56)
Cake2=Cake("Шоколад",120)
Cake3=Cake("Ваниль",98)
Cake1.bake()

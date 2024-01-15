class Obdelnik:
    def __init__(self, x=0, y=0):
        self.__ob_x = x
        self.__ob_y = y

    def x_plus(self, amount):
        self.__ob_x += amount

    def y_plus(self, amount):
        self.__ob_y += amount

    def x_minus(self, amount):
        self.__ob_x -= amount

    def y_minus(self, amount):
        self.__ob_y -= amount

    def __str__(self):
        return "x: " + str(self.__ob_x) + ", y: " + str(self.__ob_y)
    
    def __add__(self, other):
        return Obdelnik(self.__ob_x + other.__ob_x, self.__ob_y + other.__ob_y)

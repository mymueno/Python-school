from math import sqrt, pow

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    

    @property
    def x(self):
        print("jestem tu")
        return self.__x


    @x.setter
    def x(self, a):
        try:
            self.__x = int(a)
        except:
            self.__x = 0


    @property
    def y(self):
        return self.__y


    @x.setter
    def y(self, a):
        try:
            self.__y = int(a)
        except:
            self.__y = 0   


    def dlugosc(self):
        return sqrt(pow(self.__x, 2) + pow(self.__y, 2))

    
    def normalizuj(self):
        return Vector(self.__x / self.dlugosc(), self.__y / self.dlugosc())

    def wyswietl(self):
        return f"Wektor [{self.__x},{self.__y}] o długości {self.dlugosc()}"


    def __add__(self, w):
        return Vector(self.__x + w.__x, self.__y + w.__y)


    def __sub__(self, w):   
        return Vector(self.__x - w.__x, self.__y + w.__y)
    

    def __iadd__(self, w):
        return Vector(self.__x + w.__x, self.__y + w.__y)
    

    def __isub__(self, w):
        return Vector(self.__x - w.__x, self.__y + w.__y)


    def __str__(self):
        return f"[{self.__x},{self.__y}]"


    def __mul__(self, a):
        return Vector(self.__x * a, self.__y * a)
    

    def __rmul__(self, a):
        return Vector(self.__x * a, self.__y * a)

w1 = Vector('2', '4')
w2 = Vector('1', '0')


print("Wektor w1:", w1, "wektor w2:", w2)
print("Dł. w1 =", w1.dlugosc(), "dł. w2 =", w2.dlugosc())
print("w1+w2 =", w1+w2)
print("w1-w2 =", w1-w2)
print("w1*2 =", w1*2)
print("-3*w2 =", -3*w2)
print("w1*2-w2 =", w1*2-w2)
print("w1 po normalizacji =", w1.normalizuj())
print("w2 po normalizacji =", w2.normalizuj())
w1.wyswietl()
w2.wyswietl()   
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import sys
import math

class Triangle:
	def __init__(self, point1, point2, point3):
    self.x1 = float(point1[0])
		self.y1 = float(point1[1])
		self.x2 = float(point2[0])
		self.y2 = float(point2[1])
		self.x3 = float(point3[0])
		self.y3 = float(point3[1])
    
	def get_area(self):
		area = math.fabs(self.x1*(self.y2-self.y3) + self.x2*(self.y3-self.y1) + self.x3*(self.y1-self.y2)) / 2.0
		return area
	def get_perimeter(self):
    self.a = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
		self.b = math.sqrt((self.x3-self.x1)**2+(self.y3-self.y1)**2)
		self.c = math.sqrt((self.x3-self.x2)**2+(self.y3-self.y2)**2)
		return self.a + self.b + self.c
  def get_heights(self):
		height_a = 2*self.get_area() / self.a
		height_b = 2*self.get_area() / self.b
		height_c = 2*self.get_area() / self.c
		return [height_a, height_b, height_c]

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class trapeze:
  def __init__(self, point1, point2, point3, point4):
		self.x1 = float(point1[0])
		self.y1 = float(point1[1])
		self.x2 = float(point2[0])
		self.y2 = float(point2[1])
		self.x3 = float(point3[0])
		self.y3 = float(point3[1])
		self.x4 = float(point4[0])
		self.y4 = float(point4[1])
    
 def trapeze_equality(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
  	if c == d:
			return 'Трапеция равнобочная'
		else:
			return 'Трапеция не равнобочная'
  def get_sides(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		return [a, b, c, d]
	def get_perimeter(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		perimeter = a+b+c+d
		return perimeter   
	def get_area(self):
		c = math.sqrt(((self.x2-self.x1) ** 2) + ((self.y2-self.y1) ** 2))
		d = math.sqrt(((self.x4-self.x3) ** 2) + ((self.y4-self.y3) ** 2))
		a = math.sqrt(((self.x3-self.x2) ** 2) + ((self.y3-self.y2) ** 2))
		b = math.sqrt(((self.x4-self.x1) ** 2) + ((self.y4-self.y1) ** 2))
		area = ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))
		return area

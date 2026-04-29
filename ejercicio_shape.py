"""In this new code, unlike the previous version, the new superclass `shape`
was added, defining the methods `compute_area` and `compute_perimetre`, and 
using them with polymorphism in the `rectangle` and `square` classes. The new
`triangle` class was created, inheriting the existing triangle types and using 
polymorphism on the area of each triangle. Finally, encapsulation was applied, 
protecting all class attributes to allow the use of getters and setters."""

import numpy as np 
import math

class Point:
    definition: str = (
    "Entidad geometrica abstracta que representa "
    "una ubicacion en un espacio."
)
    def __init__(self, x: float, y: float):
        self._x = x 
        self._y = y

    def get_x(self) -> float:
        return self._x

    def set_x(self, value: float):
        self._x = value

    def get_y(self) -> float:
        return self._y

    def set_y(self, value: float):
        self._y = value

    def move(self, new_x: float, new_y: float):
        self._x = new_x
        self._y = new_y

    def reset(self):
        self._x = 0
        self._y = 0

    def compute_distance(self, point: "Point")-> float:
        return ((self._x - point.get_x())**2+(self._y - point.get_y())**2)**0.5
    

class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length = self.compute_length()
        self._slope = self.compute_slope()

    def get_start(self) -> Point:
        return self._start

    def get_end(self) -> Point:
        return self._end
    
    def compute_length(self) -> str:
        self._length = ((self._start.get_x() - self._end.get_x())**2 + 
                        (self._start.get_y() - self._end.get_y())**2) ** 0.5
        return f"La longitud de la linea es {self._length}"
    
    def compute_slope(self) -> str:
        dx = self._end.get_x() - self._start.get_x()
        dy = self._end.get_y() - self._start.get_y()
        if dx == 0:
            return None
        self._slope = np.arctan(dy/dx) * 180/np.pi
        return f"La pendiente de la linea es {self._slope}"
    
    def compute_horizontal_cross(self) -> str:
        if self._start.get_y() == 0 or self._end.get_y() == 0:
            return "Si hay intersección con el eje x"
        elif self._start.get_y() < 0 and self._end.get_y() > 0:
            return "Si hay intersección con el eje x"
        elif self._end.get_y() < 0 and self._start.get_y() > 0:
            return "Si hay intersección con el eje x"
        else:
            return "No hay intersección en x"
    
    def compute_vertical_cross(self) -> str:
        if self._start.get_x() == 0 or self._end.get_x() == 0:
            return "Si hay intersección con el eje y"
        elif self._start.get_x() < 0 and self._end.get_x() > 0:
            return "Si hay intersección con el eje y"
        elif self._end.get_x() < 0 and self._start.get_x() > 0:
            return "Si hay intersección con el eje y"
        else:
            return "No hay intersección en y"
        

class Shape:
    def __init__(self, is_regular: bool, vertices: list, edges: list, inner_angles: list):
        self._is_regular = is_regular          
        self._vertices = vertices             
        self._edges = edges                   
        self._inner_angles = inner_angles     

    def get_is_regular(self) -> bool:
        return self._is_regular

    def set_is_regular(self, value: bool):
        self._is_regular = value

    def get_vertices(self) -> list:
        return self._vertices

    def set_vertices(self, vertices: list) :
        self._vertices = vertices

    def get_edges(self) -> list:
        return self._edges

    def set_edges(self, edges: list):
        self._edges = edges

    def get_inner_angles(self) -> list:
        return self._inner_angles

    def set_inner_angles(self, angles: list):
        self._inner_angles = angles

    def compute_area(self) -> float:
        raise NotImplementedError

    def compute_perimeter(self) -> float:
        raise NotImplementedError

    def compute_inner_angles(self) -> list:
        raise NotImplementedError
    
    
class Rectangle(Shape):
    def __init__(self, method: int, p1 = None, p2 = None, width = None, 
        height = None, line1 = None, line2 = None, line3 = None, line4 = None
        ):
        self._width = None
        self._height = None
        self._center = None

        if method == 1: 
            self._width = width
            self._height = height
            self._center = Point(p1.get_x() + width/2, p1.get_y() + height/2)
            
        elif method == 2:
            self._width = width 
            self._height = height
            self._center = p1
            
        elif method == 3:
            self._width = abs(p2.get_x() - p1.get_x())
            self._height = abs(p2.get_y() - p1.get_y())
            self._center = Point((p1.get_x()+p2.get_x())/2, (p1.get_y()+p2.get_y())/2)
            
        elif method == 4:
            points = [line1.get_start(), line1.get_end(), line2.get_start(), line2.get_end(), 
                      line3.get_start(), line3.get_end(), line4.get_start(), line4.get_end()]
            x_coords = [p.get_x() for p in points]
            y_coords = [p.get_y() for p in points]
            min_x, max_x = min(x_coords), max(x_coords) 
            min_y, max_y = min(y_coords), max(y_coords)
            self._width = max_x - min_x
            self._height = max_y - min_y
            self._center = Point((min_x + max_x) / 2, (min_y + max_y) / 2)

    def get_width(self) -> float:
        return self._width

    def set_width(self, value: float):
        self._width = value

    def get_height(self) -> float:
        return self._height

    def set_height(self, value: float):
        self._height = value

    def get_center(self) -> Point:
        return self._center

    def compute_area(self) -> str:
        return f"el area es: {self._width * self._height}"

    def compute_perimeter(self) -> str:
        return f"El perimetro es: {(self._width*2)+(self._height*2)}"
            
            
class Square(Rectangle):

    def __init__(self, method, p1, p2, width, height):
        super().__init__(method, p1, p2, width, height)      
        
    def compute_interference_point(self, point: Point) -> bool:
        xmin = self.get_center().get_x() - self.get_width()/2
        xmax = self.get_center().get_x() + self.get_width()/2
        ymin = self.get_center().get_y() - self.get_height()/2
        ymax = self.get_center().get_y() + self.get_height()/2

        if xmin <= point.get_x() <= xmax and ymin <= point.get_y() <= ymax:
            print("El punto está dentro del rectángulo")
            return True
        else:
            print("El punto está fuera del rectángulo")
            return False    
        

class Triangle(Shape):
    def __init__(self, vertices: Point, edges: Line):
        super().__init__(False, vertices, edges, [])

    def get_edges(self) -> list:
        return [edge._length if isinstance(edge._length, float) else 
                float(edge._length.split()[-1]) for edge in self._edges]

    def compute_perimeter(self) -> float:
        return sum(self.get_edges())

    def compute_inner_angles(self) -> list:
        a, b, c = self.get_edges()
        angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
        angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        angle_C = 180 - angle_A - angle_B
        return [angle_A, angle_B, angle_C]

    def compute_area(self) -> float:
        a, b, c = self.get_edges()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Equilateral(Triangle):
    def __init__(self, vertices: Point, edges: Line):
        super().__init__(vertices, edges)
        self.set_is_regular(True)

    def compute_area(self) -> float:
        side = self.get_edges()[0]
        return (math.sqrt(3) / 4) * side**2

    def compute_inner_angles(self) -> list:
        return [60, 60, 60]


class Isosceles(Triangle):
    def __init__(self, vertices: Point, edges: Line):
        super().__init__(vertices, edges)

    def compute_area(self) -> float:
        a, b, c = self.get_edges()
        if a == b:
            equal = a
            base = c
        elif a == c:
            equal = a
            base = b
        else:
            equal = b
            base = a

        height = math.sqrt(equal**2 - (base/2)**2)
        return (base * height) / 2


class Scalene(Triangle):
    def __init__(self, vertices: Point, edges: Line):
        super().__init__(vertices, edges)

    def compute_area(self) -> float:
        return super().compute_area()


class TriRectangle(Triangle):
    def __init__(self, vertices: Point, edges: Line):
        super().__init__(vertices, edges)

    def compute_area(self) -> float:
        a, b, c = self.get_edges()
        sides = sorted([a, b, c])
        base = sides[0]
        height = sides[1]
        return (base * height) / 2
    
    def compute_inner_angles(self) -> list:
        angles = super().compute_inner_angles()
        return [round(a, 2) for a in angles]
    
    
if __name__ == "__main__":            
            
    #Rectangles
    lin1 = Line(Point(0,0),Point(2,0))
    lin2 = Line(Point(2,0),Point(2,4))
    lin3 = Line(Point(2,4),Point(0,4))
    lin4 = Line(Point(0,4),Point(0,0))
    
    rec1 = Rectangle(method = 1, p1 = Point(0,0), width = 2, height = 4)
    rec2 = Rectangle(method = 2, p1 = Point(1,2), width = 2, height = 4)
    rec3 = Rectangle(method = 3, p1 = Point(0,0), p2 = Point(2,4))
    rec4 = Rectangle(method = 4, line1 = lin1, line2 = lin2, line3 = lin3, line4 = lin4)
    
    print(rec1.compute_area())
    print(rec2.compute_area())
    print(rec3.compute_area())
    print(rec4.compute_area())

    print(rec1.compute_perimeter())
    print(rec2.compute_perimeter())
    print(rec3.compute_perimeter())
    print(rec4.compute_perimeter())

    #Lines
    print(lin1.compute_length())
    print(lin2.compute_length())
    print(lin3.compute_length())
    print(lin4.compute_length())

    print(lin1.compute_slope())
    print(lin2.compute_slope())
    print(lin3.compute_slope())
    print(lin4.compute_slope())

    print(lin1.compute_horizontal_cross())
    print(lin2.compute_horizontal_cross())
    print(lin3.compute_horizontal_cross())
    print(lin4.compute_horizontal_cross())

    print(lin1.compute_vertical_cross())
    print(lin2.compute_vertical_cross())
    print(lin3.compute_vertical_cross())
    print(lin4.compute_vertical_cross())

    #Test Square
    sq = Square(method=1, p1=Point(0,0), p2=None, width=4, height=4)
    p_test1 = Point(1,1)
    p_test2 = Point(5,5)
    print(sq.compute_interference_point(p_test1))  # True
    print(sq.compute_interference_point(p_test2))  # False

    # Triangles
    A = Point(0,0)
    B = Point(4,0)
    C = Point(2,3)
    l1 = Line(A,B)
    l2 = Line(B,C)
    l3 = Line(C,A)
    edges = [l1, l2, l3]
    vertices = [A, B, C]

    #Class Triangle
    trian1 = Triangle(vertices, edges)
    print("Triángulo:")
    print("Perímetro:", trian1.compute_perimeter())
    print("Área:", trian1.compute_area())
    print("Ángulos:", trian1.compute_inner_angles())

    # Equilateral
    A2 = Point(0,0)
    B2 = Point(3,0)
    C2 = Point(1.5, (3 * math.sqrt(3))/2)
    l1e = Line(A2,B2)
    l2e = Line(B2,C2)
    l3e = Line(C2,A2)

    equil = Equilateral([A2,B2,C2], [l1e,l2e,l3e])
    print("\nEquilátero:")
    print("Área:", equil.compute_area())
    print("Ángulos:", equil.compute_inner_angles())

    # Isosceles
    iso = Isosceles(vertices, edges)
    print("\nIsósceles:")
    print("Área:", iso.compute_area())

    # Escalene
    scalen = Scalene(vertices, edges)
    print("\nEscaleno:")
    print("Área:", scalen.compute_area())

    # Triangle rectangle
    A3 = Point(0,0)
    B3 = Point(3,0)
    C3 = Point(0,4)
    l1r = Line(A3,B3)
    l2r = Line(B3,C3)
    l3r = Line(C3,A3)
    tri_rect = TriRectangle([A3,B3,C3], [l1r,l2r,l3r])
    print("\nTriángulo Rectángulo:")
    print("Área:", tri_rect.compute_area())
    print("Ángulos:", tri_rect.compute_inner_angles())
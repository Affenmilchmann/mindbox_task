from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    @abstractclassmethod
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def area(self) -> float:
        pass

    @abstractclassmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        """Create a circle with radius = `radius`
        """
        if radius < 0: raise ValueError(f"Radius must be greater than zero. Got {radius}")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius * self.radius
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
class Triangle(Shape):
    def __init__(self, s1, s2, s3) -> None:
        """Create a triengle with side lengths `s1`, `s2` and `s3`.
        If triangle is invalid raises ValueError
        """
        if s1 < 0 or s2 < 0 or s3 < 0:
            raise ValueError(f"Triangle side must be a positive number. Recieved: {s1}, {s2}, {s3}")
        s1_, s2_, s3_ = sorted([s1, s2, s3])
        if s1_ + s2_ <= s3_:
            raise ValueError(f"Longest side ({s3_}) is shorter than (or equeal to) sum of other sides ({s1_} and {s2_})")
        self.a, self.b, self.c = s1, s2, s3

    def area(self) -> float:
        """Calculate area using Heron's formula."""
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def is_rectangular(self) -> bool:
        a, b, c = sorted([self.a, self.b, self.c])
        return c ** 2 == a ** 2 + b ** 2

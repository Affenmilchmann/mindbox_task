import os
import sys
import unittest
import random
import math

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import _shapes as shapes

class ShapeTest(unittest.TestCase):
    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            _ = shapes.Circle(- random.random() * 1000)

    def test_circle_area(self):
        for _ in range(100):
            radius = 1000 * random.random()
            circle = shapes.Circle(radius)
            self.assertEqual(circle.area(), math.pi * radius * radius)

    def test_circle_perimeter(self):
        for _ in range(100):
            radius = 1000 * random.random()
            circle = shapes.Circle(radius)
            self.assertEqual(circle.perimeter(), 2 * math.pi * radius)

    def test_invalid_triangle(self):
        # negative triangle side len
        with self.assertRaises(ValueError):
            _ = shapes.Triangle(- random.random() * 1000, random.random() * 1000, random.random() * 1000)
        with self.assertRaises(ValueError):
            _ = shapes.Triangle(random.random() * 1000, - random.random() * 1000, random.random() * 1000)
        with self.assertRaises(ValueError):
            _ = shapes.Triangle(random.random() * 1000, random.random() * 1000, - random.random() * 1000)
        # one side equals (and greater) to (than) the sum of other two
        def check_value_error(a, b, c):
            with self.assertRaises(ValueError):
                _ = shapes.Triangle(a, b, c)
        # testing C side
        a, b = random.random() * 1000, random.random() * 1000
        c = a + b
        check_value_error(a, b, c)
        c += random.random() * 1000
        check_value_error(a, b, c)
        # testing B side
        a, c = random.random() * 1000, random.random() * 1000
        b = a + c
        check_value_error(a, b, c)
        b += random.random() * 1000
        check_value_error(a, b, c)
        # testing A side
        b, c = random.random() * 1000, random.random() * 1000
        a = b + c
        check_value_error(a, b, c)
        a += random.random() * 1000
        check_value_error(a, b, c)

    def test_trianglee_area(self):
        for _ in range(100):
            a, b, c = (1000 * random.random() for _ in range(3))
            if a + b <= c or a + c <= b or b + c <= a:
                with self.assertRaises(ValueError):
                    _ = shapes.Triangle(a, b, c)
            else:
                tr = shapes.Triangle(a, b, c)
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                self.assertEqual(tr.area(), area, f"{a}, {b}, {c}")

    def test_triangle_perimeter(self):
        for _ in range(100):
            a, b, c = (1000 * random.random() for _ in range(3))
            if a + b <= c or a + c <= b or b + c <= a:
                with self.assertRaises(ValueError):
                    _ = shapes.Triangle(a, b, c)
            else:
                tr = shapes.Triangle(a, b, c)
                self.assertEqual(tr.perimeter(), a + b + c)

def test_triangle_rectangular(self):
        pythagorean_triplets = [
            (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17),
            (9, 40, 41), (11, 60, 61), (12, 35, 37), (13, 84, 85)
        ]
        # is rectangular
        for triplet in pythagorean_triplets:
            sides = list(triplet)
            random.shuffle(sides)
            a, b, c = sides
            tr = shapes.Triangle(a, b, c)
            self.assertTrue(tr.is_rectangular())
        # is not rectangular
        for triplet in pythagorean_triplets:
            sides = list(triplet)
            sides[0] += random.random()
            random.shuffle(sides)
            a, b, c = sides
            tr = shapes.Triangle(a, b, c)
            self.assertFalse(tr.is_rectangular())

if __name__ == "__main__":
    unittest.main()

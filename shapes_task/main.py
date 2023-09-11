from shapes import Triangle, Circle
from random import randint

def main():
    shapes = []
    for _ in range(1000):
        if randint(0, 1):
            shapes.append(Triangle(randint(3, 5), randint(3, 5), randint(3, 5)))
        else:
            shapes.append(Circle(randint(1, 15)))

    total_triangles = total_circles = 0
    total_area = triangle_area_sum = circle_area_sum = 0
    total_perimeter = triangle_perimeter_sum = circle_perimeter_sum = 0
    total_rectangular = 0
    for sh in shapes:
        area = sh.area()
        perimeter = sh.perimeter()
        total_area += area
        total_perimeter += perimeter
        if isinstance(sh, Triangle):
            total_triangles += 1
            triangle_area_sum += area
            triangle_perimeter_sum += perimeter
            if sh.is_rectangular():
                total_rectangular += 1
        elif isinstance(sh, Circle):
            total_circles += 1
            circle_area_sum += area
            circle_perimeter_sum += perimeter

    print(f"""    Total shapes: {len(shapes)}
        Avg area: {total_area / len(shapes):.2f}
        Avg perimeter: {total_perimeter / len(shapes):.2f}
    Total triangles: {total_triangles}
        Avg triangle area: {triangle_area_sum / total_triangles:.2f}
        Avg triangle perimeter: {triangle_perimeter_sum / total_triangles:.2f}
        Total rectangular: {total_rectangular}
    Circles: {total_circles}
        Avg circle area: {circle_area_sum / total_circles:.2f}
        Avg circle perimeter: {circle_perimeter_sum / total_circles:.2f}""")
    
if __name__ == "__main__":
    main()

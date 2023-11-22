def equation_of_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    a = y2 - y1
    b = x1 - x2

    c = a * x1 + b * y1

    # рівняння прямої
    equation = f"{a}x + {b}y = {c}"

    return equation
import math

def area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def area_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height

def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width

def area_square(side):
    if side < 0:
        raise ValueError("Side cannot be negative")
    return side ** 2

if __name__ == "__main__":
    # Test cases with expected results
    test_cases = [
        ("Circle", area_circle(5), 78.54),
        ("Triangle", area_triangle(10, 5), 25.0),
        ("Rectangle", area_rectangle(4, 7), 28.0),
        ("Square", area_square(6), 36.0)
    ]

    for shape, computed, expected in test_cases:
        print(f"{shape} area: {computed:.2f} (Expected: {expected:.2f})")

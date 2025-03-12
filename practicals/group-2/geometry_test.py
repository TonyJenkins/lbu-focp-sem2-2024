 #!/usr/bin/env python3

import geometry_origin 

def main():
    print("Testing geometry_origin module functions:")
    
    print(f"Circle area (radius=5): {geometry_origin.area_circle(5):.2f}")
    print(f"Triangle area (base=10, height=5): {geometry_origin.area_triangle(10, 5):.2f}")
    print(f"Rectangle area (length=4, width=7): {geometry_origin.area_rectangle(4, 7):.2f}")
    print(f"Square area (side=6): {geometry_origin.area_square(6):.2f}")

if __name__ == "__main__":
    main()

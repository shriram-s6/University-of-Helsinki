#!/usr/bin/env python3

# Don't modify the below hack

try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    # Call the functions from here
    
    hyp = triangle.hypothenuse(1, 1)
    tri_area = triangle.area(1, 1)
    print(hyp)
    print(tri_area)


if __name__ == "__main__":
    main()

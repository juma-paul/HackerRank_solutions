import math

def angle_of_triangle(AB: int, BC: int) -> int:
    """
    Calculate the angle of a triangle using the lengths of the adjacent (AB) and opposite (BC) sides.

    Args:
        AB (int): Length of the adjacent side.
        BC (int): Length of the opposite side.

    Returns:
        int: The angle MBC in degrees.
    """

    angle_MBC = math.atan2(AB, BC)
    MBC = round(math.degrees(angle_MBC))

    return MBC

def main():
    """
    Main function to calculate and print the angle of a triangle.
    """

    opp = int(input(f'\nEnter length of opposite side of triangle: '))
    adj = int(input(f'\nEnter length of adjacent side of triangle: '))

    res = angle_of_triangle(opp, adj)
    print(f'\n<MBC = {res}{chr(176)}\n')

if __name__ == '__main__':
    main()

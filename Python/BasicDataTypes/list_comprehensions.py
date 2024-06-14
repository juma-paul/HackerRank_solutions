def possible_cordinates(x, y, z, n):
    """
    A function to print all possible coordinates on a 3D grid

    params:
        x(int) - first cuboid dimension 
        y(int) - second cuboid dimension 
        z(int) - third cuboid dimension 
        n(int) - integer to ensure i + j + k != n
    """
    
    cuboid = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    return cuboid

def main():
    """
    A main method for testing the function possiblecordinates()
    """

    print("\nPlease enter four integers to print dimensions of the cuboid: ")
    x = int(input("x: ")) # x: 1
    y = int(input("y: ")) # y: 1
    z = int(input("z: ")) # z: 1
    n = int(input("n: ")) # n: 2

    res = possible_cordinates(x, y, z, n)
    print(res) # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

if __name__ == '__main__':
    main()
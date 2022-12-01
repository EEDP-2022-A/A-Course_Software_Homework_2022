## Function to get user input for required values

def get_circle_inputs():
    x0 = input("Enter the x-coordinate of the circle: ")
    y0 = input("Enter the y-coordinate of the circle: ")
    R = input("Enter the radius of the circle: ")
    N = input("Enter the number of perimeter points on the circle: ")
    spacing = input("Enter \'1\' for equally spaced points or \'2\' for randomly spaced points: ")
    return x0, y0, R, N, spacing

if __name__ == '__main__':
    get_circle_inputs()

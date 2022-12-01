## Function to get user input for required values

def get_circle_inputs():
    again = True
    while again == True:
        # Obtaining circle inputs
        x0 = float(input("Enter the x-coordinate of the circle: "))
        y0 = float(input("Enter the y-coordinate of the circle: "))
        R = float(input("Enter the radius of the circle: "))
        N = int(input("Enter the number of perimeter points on the circle: "))
        spacing = int(input("Enter \'1\' for equally spaced points or \'2\' for randomly spaced points: "))

        # Printing inputs
        print("\n======USER INPUTS======")
        print("x-coordinate: {}".format(x0))
        print("y-coordinate: {}".format(y0))
        print("radius: {}".format(R))
        print("number of perimeter points: {}".format(N))
        print("spacing selection: {}\n".format(spacing))

        # Chacking statisfaction with inputs
        answer1 = input("Are you satisfied with these values? (y/n): ")
        if answer1.lower() == 'y':
            again = False
        else:
            answer2 = input("Would you like to repeat the inputs? (y/n): ")
            if answer2.lower() == 'n':
                again = False
    return x0, y0, R, N, spacing

if __name__ == '__main__':
    x0, y0, R, N, spacing = get_circle_inputs()

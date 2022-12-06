## Function to get user input for required values

def get_circle_inputs():
    # Obtaining circle inputs
    while True:
        try:
            x0 = float(input("Enter the x-coordinate of the circle: "))
        except ValueError:
            print("USER ERROR: Please enter a number.")
            continue
        break
    
    while True:
        try:
            y0 = float(input("Enter the y-coordinate of the circle: "))
        except ValueError:
            print("USER ERROR: Please enter a number.")
            continue
        break
    
    while True:
        try:
            R = float(input("Enter the radius of the circle: "))
            if R <= 0:
                raise ValueError("USER ERROR: Please enter a positive number.")
        except ValueError:
            print("USER ERROR: Please enter a positive number.")
            continue
        break
    
    while True:
        try:
            N = int(input("Enter the number of perimeter points on the circle (must be greater than 2): "))
            if N < 3:
                raise ValueError("USER ERROR: Please enter an integer greater than 2")
        except ValueError:
            print("USER ERROR: Please enter an integer greater than 2")
            continue
        break

    while True:
        try:
            spacing = int(input("Enter \'1\' for equally spaced points or \'2\' for randomly spaced points: "))
            if spacing != 1 and spacing != 2:
                raise ValueError("USER ERROR: Please enter a value of '1' or '2'.")
        except ValueError:
            print("USER ERROR: Please enter a value of '1' or '2'.")
            continue
        break
    return x0, y0, R, N, spacing

def print_inputs(x0, y0, R, N, choice):
    print("\n======USER INPUTS======")
    print("x-coordinate: {}".format(x0))
    print("y-coordinate: {}".format(y0))
    print("radius: {}".format(R))
    print("number of perimeter points: {}".format(N))
    print("spacing selection: {}\n".format(choice))
    return


def check_satisfaction():
    # Checking statisfaction with inputs
    answer1 = input("Are you satisfied with these values? (y/n): ")
    if answer1.lower() == 'y':
        return True
    else:
        answer2 = input("Would you like to repeat the inputs? (y/n): ")
        if answer2.lower() == 'n':
            return True
    return False

if __name__ == '__main__':
    while True:
        x0, y0, R, N, choice = get_circle_inputs()
        print_inputs(x0, y0, R, N, choice)
        if check_satisfaction():
            break
        continue

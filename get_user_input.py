## Function to get user input for required values

def get_circle_inputs():
    while True:
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
            except ValueError:
                print("USER ERROR: Please enter a number.")
                continue
            break
        
        while True:
            try:
                N = int(input("Enter the number of perimeter points on the circle: "))
            except ValueError:
                print("USER ERROR: Please enter an integer greater than 2")
            break

        while True:
            try:
                spacing = int(input("Enter \'1\' for equally spaced points or \'2\' for randomly spaced points: "))
                if spacing != 1 or spacing != 2:
                    raise Exception("USER ERROR: Please enter a value of '1' or '2'.")
                    
            except ValueError:
                print("USER ERROR: Please enter a value of '1' or '2'.")
                continue
            break

        # Printing inputs
        print("\n======USER INPUTS======")
        print("x-coordinate: {}".format(x0))
        print("y-coordinate: {}".format(y0))
        print("radius: {}".format(R))
        print("number of perimeter points: {}".format(N))
        print("spacing selection: {}\n".format(spacing))

        # Checking statisfaction with inputs
        answer1 = input("Are you satisfied with these values? (y/n): ")
        if answer1.lower() == 'y':
            break
        else:
            answer2 = input("Would you like to repeat the inputs? (y/n): ")
            if answer2.lower() == 'n':
                break
    return x0, y0, R, N, spacing

if __name__ == '__main__':
    x0, y0, R, N, spacing = get_circle_inputs()

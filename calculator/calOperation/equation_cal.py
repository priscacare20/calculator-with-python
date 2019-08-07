import matplotlib.pyplot as plt
import sys
import math
import cmath


class EquOperation:

    """This class requires the user to input the highest degree of the equation they want to calculate
        Then figure out the equation type and then calculate the equation
        It returns the list of values and a graph of y against x
    """

    def __init__(self):
        self.linear = False
        self.quadratic = False
        self.cubic = False
        self.poly = False

    # the call function makes the class callable as it is seen in main file. this function is ran when an instance of the class is called
    # although this is not the best use case, am using this here to practice callable class
    def __call__(self):
        print("in the call function")
        # continue asking for equation degree untill user input integer
        while True:
            try:
                degree = int(input("Enter the Equation degree: "))
            except ValueError:
                print("degree must be integers only")
                continue
            break
        if degree == 1 or degree == 0:
            self.linear = True
        elif degree == 2:
            self.quadratic = True
        elif degree == 3:
            self.cubic = True
        elif degree >=4:
            self.poly = True
        else:
            print("degree must be integer")

    @staticmethod  # this function can only be used by within this class. Notice no self, it is used in this class alone intants do not need to use it
    def _linear_equation():
        """This function calculates linear equation of the form y=mx + b.
            arguments: m, b, and a stream or range of values for x
            It returns a graph of y vs x and a list of y values
        """

        # the single underscore means its a private function
        print("y = mx + b where m != 0")
        y = []
        x = []
        counter = 3
        while counter:
            counter -= 1 # user only attempts to calculate 3 times, if no success it ask if they want to exit from this function
            try:
                m = float(input("enter m: "))  # possibility of value error if user enters characters
                b = float(input("enter b: "))  # possibility of value error if user enters characters
            except ValueError:
                print("enter numbers only")
                continue
            # the user should be able to enter a range of constant values for x or a stream of values
            get_x = input("if x is range of values enter 'r'\n"
                          "if x is a stream of values enter 's'\n")
            if get_x.upper() == 'R':
                try:
                    x_range = list(map(int, (input("enter a range of x values (i,j): ").split(',')))) # possibility of value error if user enters characters
                    for x1 in range(x_range[0],x_range[1]):  # possibility of index error if used inputs a single value
                        y1 = (m*x1) + b
                        y.append(y1)
                        x.append(x1)
                except (ValueError, IndexError):
                    print("invalid range: enter 2 integers separated by comma")
                    continue
            elif get_x.upper() == 'S':
                # continuously receives value for user, appends this to the x: list.
                # x1 is float

                while True:
                    x1 = input("enter a value for x, if this is the last value please enter 'l'")
                    try:
                        x1 = float(x1)
                    except ValueError as e:
                        if x1.lower() == 'l':
                            break
                        else:
                            print("invalid input!")
                            sys.exit()
                    y1 = (m * x1) + b
                    y.append(y1)
                    x.append(x1)
                    continue
            else:
                print("enter 'r' or 's' ")
                continue
            plt.plot(x,y,'r.-')
            plt.xlabel("X AXIS")
            plt.ylabel("Y AXIS")
            plt.title("GRAPH OF Y AGAINST X")
            plt.show()
            return y

    @staticmethod
    def _quadratic_equation():
        print("Ax^2 + Bx + C = 0")
        while True:
            try:
                a = float(input("enter coefficient A"))
                b = float(input("enter coefficient B"))
                c = float(input("enter c"))
            except ValueError:
                print("invalid input")
                continue
            if (b**2) >= (4 * a * c):
                x1 = -b + (math.sqrt(b**2 - (4 * a * c))/(2* a))
                x2 = -b - (math.sqrt(b**2 - (4 * a * c))/(2 * a))
            else:
                z = math.sqrt((b**2 - (4 * a * c)) * -1)
                print('z:{}'.format(z))
                x1 = complex(-b,z)/(2*a)
                x2 = complex(-b,-z)/(2*a)
            return x1, x2

    def cubic_equation(self):
        pass

    def polynomial(self):
        pass

    def execute(self):
        print("in the execute block")
        if self.linear:
            print(self._linear_equation())
        elif self.quadratic:
            return self._quadratic_equation()
        elif self.cubic:
            return self.cubic_equation()
        else:
            return self.polynomial()

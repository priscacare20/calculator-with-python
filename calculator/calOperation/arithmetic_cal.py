import math


class Arithmetic:

    def simple_arithmetic(self):
        """ calculate simple arithmetic operation. e.g 9+6*4. user need not enter the equality sign"""
        print("Accepts basic operation:\n"
              "+ : addition\n"
              "- : subtraction\n"
              "* : multiplication\n"
              "/ : division\n"
              "% : modulus\n"
              "** : power of 2\n")
        request_operand = input()
        while True:
            try:
                return eval(request_operand)  # calculates user inputs
            except TypeError as t:
                print("invalid definition of operand")
                print(t)
                break
            except SyntaxError as e:
                print("invalid argument: use only the available operation")
                print(e)
                print("result = ", end="")  # let the None be on the same line as result
                break

    # TODO def mean(self): continuous input processed after a certain time limit is reach when the user did not give any further input

    def mean(self):
        """calculate the mean of numbers.
        Users must enter numbers only seperated by comma"""
        print("enter numbers separated by comma")
        error = None
        a_inputs = input()
        inputs = a_inputs.split(',')
        # remove empty value when comma is the last value entered in a_inputs
        if inputs[-1] == '':
            inputs.pop()
        sub_mean = 0
        length = 0
        while True:
            # calculate only when user enter some value else exit and trap the zero divison from length=0
            if any(inputs):
                for inp in inputs:
                    if inp != ',':
                        length += 1
                        try:
                            sub_mean += float(inp)
                        except ValueError as e:
                            print("invalid arguments, inputs must be numbers separated by comma")
                            error = e
            else:
                print("No inputs entered")
            # if an error occurs during the code, then the result is not output to user
            if error:
                print("cannot complete this operation")
                raise error  # this raise the valueError but if we don't want this error on the user interface, this line should be erased
            else:
                print("total sum {} : total length {}".format(sub_mean, length))
                try:
                    return sub_mean/length
                except ZeroDivisionError:
                    break

    def mode(self):
        """calculate the mode given a list of numbers.
        Users must enter numbers only separated by comma"""
        print("enter numbers separated by comma")
        a_inputs = input()
        while True:
            # pre processing: ensure that user enters numbers only
            try:
                inputs = list(map(float, a_inputs.split(',')))
            except ValueError:
                print("Check value entered: you have either entered improper values or nothing")
                print("result: ", end="")
                break
            print(inputs)
            # remove empty value when comma is the last value entered in a_inputs
            if inputs[-1] == '':
                inputs.pop()
            # calculate mode only when user enter some value else exit
            if any(inputs):
                max_count = 0
                max_count_value = 0
                for value in set(inputs):
                    counter = inputs.count(value)
                    if counter >= max_count:
                        max_count = counter
                        max_count_value = value
            print("number of times mode occurs : {}".format(max_count))
            print("modal value:", end="")
            return max_count_value

    def median(self):
        """calculate the mean of numbers.
        Users must enter numbers only seperated by comma"""
        print("enter numbers separated by comma")
        a_inputs = input()
        # pre processing
        inputs = a_inputs.split(',')
        print(inputs)
        # remove empty value when comma is the last value entered in a_inputs
        if inputs[-1] == '':
            inputs.pop()
        # calculate median only when user enter some value else exit
        flag = True
        while flag:
            if any(inputs):
                try:
                    sort_inputs = sorted(map(float, inputs))  # converts elements of inputs to int and sort the output
                    print(sort_inputs)
                except ValueError:
                    print("values must be numbers")
                    break
                # if len of inputs is divisible by two, then sum the 2 middle values and divide by 2, else output the middle value
                length = len(sort_inputs)
                if length % 2 == 0:
                    index = int(length/2)
                    print(index)
                    middle_values = sum(sort_inputs[(index-1):(index+1)])
                    result = middle_values/2
                else:
                    index = (length//2) + 1
                    result = sort_inputs[index-1]
            else:
                print("No inputs entered")
                break
            print("median:", end="")
            return result

    def sqroot(self):
        while True:
            try:
                user_input = float(input())
            except ValueError:
                print("Enter Numbers only")
                continue
            return math.sqrt(user_input)

    def execute(self):
        flag = True
        problem = None
        # inside a while loop so that the program can break when the user choose to exit
        while flag:
            # assigning symbols for the needed arithmetic operations
            option = {1: "simple arithmetic", 2: "square root", 3: "median", 4: "mode", 5: "mean", 0: "exit"}
            for code, opt in option.items():
                print(code, ":", opt)
            # get input from user and execute the operation corresponding to users value
            try:
                action = option.get(int(input()), option[0])
            except ValueError:
                print("please choose from the above options")
                # sys.exit(1) this is gonna terminate the program, however we don't want that. i want the user to keep trying
                continue
            if problem:
                raise problem
            print(action)
            if action == 'square root':
                print(self.sqroot())
            elif action == "median":
                print(self.median())
            elif action == "mode":
                print(self.mode())
            elif action == "mean":
                print(self.mean())
            elif action == 'simple arithmetic':
                print(self.simple_arithmetic())
            else:
                break
            #  to repeat the existing option
            repeat = input("Do you want to perform another operation? Y/N: ")
            if repeat.upper() == 'Y':
                continue
            flag = False

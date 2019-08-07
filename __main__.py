# this main is use to make the directory executable. that is you can pass the name of this directory to python on terminal and it will execute
# these code may otherwise be written on the calculator\_init_.py because it initializes the module and is the first file to be executed when there is no main
import sys
print("running from main")
from calculator.calOperation.dataframe_cal import DataOperation
from calculator.calOperation.equation_cal import EquOperation
from calculator.calOperation.matrices_cal import MatricOperation
from calculator.calOperation.arithmetic_cal import Arithmetic

""" the classes were instantiated here and then called in line 23-29.
    without this, the self attribute will have to be passed to the class whenever they are used"""

arith = Arithmetic()
data = DataOperation()
equate = EquOperation()
matrices = MatricOperation()
while True:
    print("what operation do you want to perform?\n"
          "enter 1: for Arithmetic \n"
          "enter 2: for Equation \n"
          "enter 3: for Dataframe \n"
          "enter 4: for Matrices \n"
          "enter 0: to exit\n")
    operation_map = {1:'arithmetic', 2:'equation', 3:'dataframe', 4:'matrices', 0: 'exit'}
    # to ensure the user input a number and avoid value error when a string is entered
    try:
        operation_type = operation_map.get(int(input()),operation_map[0])
    except ValueError:
        print("please enter a number for the corresponding operation")
        continue
    # to call the operations corresponding to the entered value
    if operation_type == 'dataframe':
        data.execute()
    elif operation_type == 'equation':
        equate()  # calling an instance of EquOperation, this is possible because of the call function in the class
        print(equate.execute())
    elif operation_type == 'matrices':
        matrices.execute()
    elif operation_type == 'arithmetic':
        print(arith.execute())
    else:
        break
    # to exit from the mycalculator application
    repeat = input("Do you want to exit? Y/N: ")
    if repeat.upper() == "N":
        continue
    else:
        sys.exit()
        #break




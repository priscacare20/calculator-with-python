# from calculator.calOperation.dataframe_cal import DataOperation
# from calculator.calOperation.equation_cal import EquOperation
# from calculator.calOperation.matrices_cal import MatricOperation
# from calculator.calOperation.arithmetic_cal import Arithmetic
#
#
# class Calculator:
#
#     """ this class takes the operation type the user wants to perform
#     """
#
#     def __init__(self):
#         self.operation = self.operation()
#
#     def operation(self):
#         print("what operation do you want to perform?\n"
#               "enter 1: for Arithmetic \n"
#               "enter 2: for Equation \n"
#               "enter 3: for Dataframe \n"
#               "enter 4: for Matrices \n")
#         operation_map = {1:'arithmetic', 2:'equation', 3:'dataframe', 4:'matrices'}
#         operation_type = operation_map.get(int(input()),operation_map[1])
#         return self.execute(operation_type)
#
#     def execute(self,oper_type):
#         if oper_type == 'dataframe':
#             DataOperation.execute(self)
#         elif oper_type == 'equation':
#             EquOperation.execute(self)
#         elif oper_type == 'matrices':
#             MatricOperation.execute(self)
#         else:
#             print(Arithmetic.execute())
#
#     def add(self, *args):
#         sum = 0
#         for arg in args:
#             sum += arg
#         return sum
#
#     def subtract(self, *args):
#         diff = args[0]
#         for arg in args[1:]:
#             diff -= arg
#         return diff
#
#     def multiply(self, *args):
#         prod = 1
#         for arg in args:
#             prod *= arg
#         return prod
#
#     def divide(self, *args):
#         div = args[0]
#         try:
#             for arg in args[1:]:
#                 div /= arg
#         except ZeroDivisionError:
#             return "cannot divide by zero"
#         return div
#
#
# if __name__ == '__main__':
#     cal = Calculator()
#     #print(cal)

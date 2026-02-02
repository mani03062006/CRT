'''
Debugging in python
Bug is an error
Finding and fixing bugs is called debugging
Types of errors:    
1) Syntax Error-->Missing colon, parenthesis, indentation error
2)Run-Time Error-->Any num is divisble by zero
3)Logical error-->Missing of Logics

Debugging Techniques:
1)print()-->Run the code line by line
2)try-except-->
3)Using pdb

  Python Debugger:
     Main Purpose is:
        1)to Pause the Execution
        2)to run the code step by step
        3)to inspect the variables value
        pdb commands:
            1)n-->exceution in a next line
            2)p variable-->to print the value of variable
            3)l-->list nearby code
            4)c-->To continue execution
            5)s-->start with the function
            6)r-->return from the function
            7)h-->help
            8)q-->Quit the execution

try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid input.")
    '''
import pdb
def add(a,b):
    pdb.set_trace() #setting a breakpoint for debugging
    return a+b
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print(add(a,b))
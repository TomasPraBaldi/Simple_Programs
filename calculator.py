from calc_art import logo 
import os



def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}
def calculator():
    print(logo)
    loop = True
    n1 = float(input("What's the first number?: "))

    while loop:
        #choosing numbers and operation
        for _ in operations:
            print(_)
        operation_symb = input("Pick an operation from above: ")
        n2 = float(input("What's the next number?: "))
        #doing the math
        actual_operation = operations[operation_symb]
        answer = actual_operation(n1 , n2)
        #answer
        print(f"{n1} {operation_symb} {n2} = {answer}")
        n1 = answer
        keep_going = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new one.: ").lower()
        os.system('cls')
        print(logo)
        if keep_going == "n":
            loop = False
            calculator()
calculator()

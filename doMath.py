import numpy as np
import re

## ORIGINAL doMath
#def doMath(text):
#    try:
#        number = float(text)
#        square = np.sqrt(number)
#        rounded = round(square, 3)
#        return str(rounded)
#    except:
#        return 'NAN'

    
# ===============================
# based and built of code my friend Daniel Baldwin wrote
# for another calculator python app we built together awhile back
# that one used tkinter and looked like a calculator

def domath(eq):
    # Input: equation as list of strings
    # Output: solution to equation as a floating point number

    # Exponents
    for i in range(0, len(eq)):
        if eq[i] == '^':
            eq[i + 1] = float(eq[i - 1]) ** float(eq[i + 1])
            eq[i - 1] = ''
            eq[i] = ''
    eq = [x for x in eq if x != '']  # Remove all empty elements from eq

    # Multiplication & division
    for i in range(0, len(eq)):
        if eq[i] == '*':
            eq[i + 1] = float(eq[i - 1]) * float(eq[i + 1])
            eq[i - 1] = ''
            eq[i] = ''
        elif eq[i] == '/':
            eq[i + 1] = float(eq[i - 1]) / float(eq[i + 1])
            eq[i - 1] = ''
            eq[i] = ''
    eq = [x for x in eq if x != '']  # Remove all empty elements from eq

    # Addition and subtraction
    for i in range(0, len(eq)):
        if eq[i] == '+':
            eq[i + 1] = float(eq[i - 1]) + float(eq[i + 1])
            eq[i - 1] = ''
            eq[i] = ''
        elif eq[i] == '-':
            eq[i + 1] = float(eq[i - 1]) - float(eq[i + 1])
            eq[i - 1] = ''
            eq[i] = ''
    eq = [x for x in eq if x != '']  # Remove all empty elements from eq

    return eq[0]  # Output


# main operation of calculator
def calc(input):
    # new input
    eq = ['']

    # Sort characters of input into numbers and operators
    # TO DO: Handle negative number after parenthesis

    j = 0  # Index of list eq

    # Check each character of input string
    for i in range(0, len(input)):

        # # Creating list of alphabet
        # alphabet = []
        # alpha = 'a'
        # for i in range(0, 26):
        #     alphabet.append(alpha)
        #     alpha = chr(ord(alpha) + 1)

            # Handle negative sign
        if input[i] == '-' and i == 0:  # Equation begins with minus sign
            eq[j] += input[i]  # Append to current element of list eq
        elif input[i] == '-' and input[i - 1].replace('.', '', 1).replace('-', '',
                                                                          1).isdigit() == False:  # Minus sign after other symbol
            eq[j] += input[i]  # Append to current element of list eq

        # Numbers
        elif input[i].isdigit() or input[i] == '.':
            eq[j] += input[i]  # Append to current element of list eq

        # Check for symbols
        elif input[i] == '+' or input[i] == '-' or input[i] == '*' or input[i] == '/' or input[i] == '^' or input[
            i] == '(' or input[i] == ')':
            j += 2
            eq.append(input[i])  # Move to a new list element
            eq.append('')  # Put the next character in a new list element




    p = 0  # location of open parenthesis

    # Do parentheses first
    # TO DO: Account for nested parentheses
    for i in range(0, len(eq)):
        if eq[i] == '(':
            p = i + 1
        elif eq[i] == ')':
            eq[p] = domath(eq[p:i])
            eq[p - 1] = ''
            for k in range(p + 1, i + 1):
                eq[k] = ''
    eq = [x for x in eq if x != '']  # Remove all empty elements from eq

    q = 0 # location of trig

    # Check for Trigs
    for l in range(0, len(eq)):
        if input[l] == 's' and input[l + 1] == 'i' and input[l + 2] == 'n':
            eq[l] = math.sin(float(eq[l]))
        elif input[l] == 'c' and input[l + 1] == 'o' and input[l + 2] == 's':
            eq[l] = math.cos(float(eq[l]))
        elif input[l] == 't' and input[l + 1] == 'a' and input[l + 2] == 'n':
            eq[l] = math.tan(float(eq[l]))
        elif input[l] == 'l' and input[l + 1] == 'o' and input[l + 2] == 'g':
            eq[l] = math.log10(float(eq[l]))
        # elif input[l] == 'l' and input[l + 1] == 'n':
        #     eq[l] = math.log(float(eq[l])[math.e])


    eq = domath(eq)  # Do rest of calculations after handling parentheses

    # Printing Solution
    solution = ''.join(str(eq))

    return solution
# ======================================






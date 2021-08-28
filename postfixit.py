# Name:         Sameera Balijepalli

#from typing import List


def main() -> None:
    """
    Iteratively prompt the user for an infix expression and display both the
    postfix equivalent and, on the next line, the result as a float (even if it
    is a whole number) rounded to 3 decimal places. Assume the infix expression
    is properly formatted.
    """
    while True:
        try:
            infix = input(">>> ")
            # insert all code for main below this line
            infix_convert = postfix(infix)
            print(infix_convert)
            print(evaluate(infix_convert))

        except EOFError:  # loop breaks with CTRL+d
            break
    print()  # empty line prints before program ends
    # end of main (no return statement is equivalent to |return None|)


# insert additional function definitions below this line
def operand(item: str) -> bool:
    """Checks if string contains an operator (typically a variable).
    Returns True if yes, False otherwise
    """
    for char in item:
        if char == ".":
            return item.replace(char, '', 1).isdigit()
        elif char == "-":
            return item.strip(char).isdigit()
    return item.isdigit()


def pemdas(item: str) -> int:
    """Assigns precedence to operators"""
    if item == "+":
        return 0
    elif item == "-":
        return 0
    elif item == "/":
        return 1
    elif item == "*":
        return 1
    elif item == "^":
        return 2
    return -1


def postfix(infix: str) -> str:
    """Converts infix expression to postfix expression"""
    stack = [] #empty stack
    postfix_out = " " #empty output
    convert = infix.split()
    for item in convert:
        if operand(item):
            postfix_out += item + " "
        elif item == "(" or item == "^":
            stack.append(item)
        elif item == ")":
            if len(stack) > 0:
                while stack[-1] != "(":
                    postfix_out += stack.pop() + " "
            if len(stack) > 0:
                stack.pop()
        else:
            while len(stack) > 0 and stack[-1] != "(" and \
            pemdas(item) <= pemdas(stack[-1]):
                if len(stack) > 0:
                    postfix_out += stack.pop() + " "
            stack.append(item)
    while len(stack) > 0:
        postfix_out += stack.pop() + " "
    return "".join(postfix_out.strip())


def calculate(right_pop: float, left_pop: float, item: str) -> float:
    """Function performs caculators between operators."""
    result = 0
    if item == "/":
        if right_pop != 0:
            result = left_pop / right_pop
    elif item == "*":
        result = left_pop * right_pop
    elif item == "+":
        result = left_pop + right_pop
    elif item == "-":
        result = left_pop - right_pop
    elif item == "^":
        result = left_pop ** right_pop
    return result


def evaluate(postfix: str) -> str:
    """Evaluates postfix expression"""
    stack = []
    evaluate = postfix.split()
    for item in evaluate:
        if operand(item):
            stack.append(float(item))
        else:
            if len(stack) > 0:
                right_pop = stack.pop()
                left_pop = stack.pop()
                result = calculate(right_pop, left_pop, item)
                stack.append(float(result))
    final = 0
    if len(stack) > 0:
        final = stack.pop()
    return format(final, '.3f')


# do not add code below this line
if __name__ == "__main__":  # runs main with command |python3 postfixit.py|
    main()

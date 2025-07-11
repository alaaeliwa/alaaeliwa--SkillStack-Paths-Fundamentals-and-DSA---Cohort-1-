def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []  # operator stack
    output = []  # output list for postfix expression

    tokens = expr.split()

    for token in tokens:
        if token.isdigit():  # Operand
            output.append(token)
        elif token == '(':  # Left 
            stack.append(token)
        elif token == ')':  # Right 
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' from the stack
        else:  # Operator
            while (stack and stack[-1] != '(' and
                  precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    # Pop  operators from the stack
    while stack:
        output.append(stack.pop())

    return ' '.join(output)



expr1 = "5 + ( 6 - 2 ) * 9"
print(infix_to_postfix(expr1))  

expr2 = "( 1 + 2 ) * ( 3 + 4 )"
print(infix_to_postfix(expr2))

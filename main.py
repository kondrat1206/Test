result = 0
operand = 0
operator = '+'
wait_for_number = True

while True:
    if wait_for_number == True:
        in_operand = input("Enter number: ")
        if in_operand.replace('.', '').replace(',', '').isdigit():
            operand = float(in_operand)
            expression = f"{result} {operator} {operand}"
            try:
                result = eval(expression)
            except ZeroDivisionError:
                print("Zero Division Error. Try again")
                continue
            else:
                wait_for_number = False
        else:
            print(f"{in_operand} is not a number. Try again.")
            continue
    else:
        in_operator = input("Enter operator(+,-,*,/,=): ")
        if in_operator in ['=']:
            print(f'Result: {result}')
            break
        elif in_operator in ['+','-','*','/']:
            operator = in_operator
            wait_for_number = True
        else:
            print(f"{in_operator} is not operator(+,-,*,/,=). Try again.")
            continue
            
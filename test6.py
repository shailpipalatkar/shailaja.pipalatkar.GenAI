def parse_and_solve_equation(equation):
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return f"Error: {str(e)}"


equation = input("Enter a mathematical equation (e.g., 3 * x + 2): ")

x_value = float(input("Enter the value for x: "))
equation = equation.replace('x', str(x_value))

result = parse_and_solve_equation(equation)
print(f"The result of the equation is: {result}")
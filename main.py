
def cross_product():
    print("CROSS PRODUCT CALCULATOR")
    print("Enter components as:")
    print("a, b, c for first vector")
    print("d, e, f for second vector")
    print()

    # Get vector components as strings
    a = input("a = ")
    b = input("b = ")
    c = input("c = ")
    print("Vector 1 = [" + a + ", " + b + ", " + c + "]")
    print()

    d = input("d = ")
    e = input("e = ")
    f = input("f = ")
    print("Vector 2 = [" + d + ", " + e + ", " + f + "]")
    print()

    # Calculate symbolic cross product components
    # i-component: b*f - c*e
    i_num = symbolic_subtract(
        symbolic_multiply(b, f),
        symbolic_multiply(c, e)
    )

    # j-component: -(a*f - c*d) = c*d - a*f
    j_num = symbolic_subtract(
        symbolic_multiply(c, d),
        symbolic_multiply(a, f)
    )

    # k-component: a*e - b*d
    k_num = symbolic_subtract(
        symbolic_multiply(a, e),
        symbolic_multiply(b, d)
    )

    # Display the result
    print("Cross Product:")
    print("-------------")
    print("i: " + i_num)
    print("j: " + j_num)
    print("k: " + k_num)
    print()
    print("Result: [" + i_num + ", " + j_num + ", " + k_num + "]")

    # Pause before exiting
    input("Press ENTER to continue...")

def symbolic_multiply(x, y):
  
    # Check for zeros
    if x == "0" or y == "0":
        return "0"

    # Check if either is 1 or -1
    if x == "1":
        return y
    if x == "-1":
        if y.startswith('-'):
            return y[1:]  # -1 * -y = y
        else:
            return "-" + y  # -1 * y = -y

    if y == "1":
        return x
    if y == "-1":
        if x.startswith('-'):
            return x[1:]  # -x * -1 = x
        else:
            return "-" + x  # x * -1 = -x

    # Cases with negatives
    if x.startswith('-') and y.startswith('-'):
        # (-x)*(-y) = x*y
        return x[1:] + "*" + y[1:]
    elif x.startswith('-'):
        # (-x)*y = -(x*y)
        return "-" + x[1:] + "*" + y
    elif y.startswith('-'):
        # x*(-y) = -(x*y)
        return "-" + x + "*" + y[1:]
    else:
        # x*y = x*y
        return x + "*" + y

def symbolic_subtract(expr1, expr2):
    # If both are zero
    if expr1 == "0" and expr2 == "0":
        return "0"

    # If second expression is negative, it becomes addition
    if expr2.startswith('-'):
        # expr1 - (-expr2) = expr1 + expr2
        expr2_pos = expr2[1:]  # Remove the negative
        return symbolic_add(expr1, expr2_pos)

    # If first expression is zero
    if expr1 == "0":
        return "-" + expr2

    # If second expression is zero
    if expr2 == "0":
        return expr1

    # Check if expressions are the same
    if expr1 == expr2:
        return "0"

    # Regular subtraction
    return expr1 + " - " + expr2

def symbolic_add(expr1, expr2):

    # Handle empty expressions or zeros
    if expr1 == "" or expr1 == "0":
        return expr2
    if expr2 == "" or expr2 == "0":
        return expr1

    # Check if both are negative
    if expr1.startswith('-') and expr2.startswith('-'):
        return "-(" + expr1[1:] + " + " + expr2[1:] + ")"

    # Check if second is negative (becomes subtraction)
    if expr2.startswith('-'):
        return symbolic_subtract(expr1, expr2[1:])

    # Check if first is negative
    if expr1.startswith('-'):
        # -x + y = y - x
        return symbolic_subtract(expr2, expr1[1:])

    # Regular addition
    return expr1 + " + " + expr2

def simplify_expression(expr):
    # Remove double negatives
    while "--" in expr:
        expr = expr.replace("--", "")

    # Remove +- and -+
    expr = expr.replace("+-", "-")
    expr = expr.replace("-+", "-")

    # Remove unnecessary *1
    expr = expr.replace("*1", "")
    expr = expr.replace("1*", "")

    # Simplify -1* to just -
    expr = expr.replace("-1*", "-")

    # Remove leading + if present
    if expr.startswith("+"):
        expr = expr[1:]

    return expr

cross_product()

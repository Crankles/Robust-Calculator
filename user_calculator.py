print("""Hello! I'm a calculator with two modes:

    standard - enter two numbers and an operator

    file - enter a text file name to read in and calculate equations

Please enter your selection below:
      """)

# By defining the following dictionary, we can convert the string operators to
# a corresponding function. At first I wasn't sure if a lambda function could
# be used as a dictionary value but turns out you can.
operator_dict = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
    "**": (lambda x, y: x ** y)
    }

calc_type = input("Desired mode: ")

# Look for valid user input.
while calc_type not in ["standard", "file"]:
    print("Please enter 'standard' or 'file'.\n")
    calc_type = input("Desired mode: ")

# Standard calculator mode:
if calc_type == "standard":

    print("\nThe equation entered will be saved to a calc_answers.txt file.\n")

    # Look for valid user input. Float to enable float inputs.
    while True:
        try:
            operand_1 = float(input("First operand: "))
            operand_2 = float(input("Second operand: "))
        except ValueError:
            print("Please enter only numbers.\n")
        else:
            break

    print("You have entered: {} _ {}".format(operand_1, operand_2))

    operator = input("\nNow enter an operator: ")
    # Having operator_dict means there is no need for repeated if statements.
    while operator not in operator_dict.keys():
        print("Please enter one of {}.".format(operator_dict.keys()))
        operator = input("Please enter an operator: ")

    print("\nThe equation you have entered is: {} {} {}".format(operand_1,
                                                                operator,
                                                                operand_2))
    # Check for division by zero.
    if (operand_2 == 0) and (operator == "/"):
        print("\nDivision by zero is undefined!")
    else:
        print("\n{} {} {} = {}".format(
            operand_1,
            operator,
            operand_2,
            operator_dict[operator](operand_1, operand_2)))
    # Write or append equation to file based on file existence.
    with open("calc_answers.txt", "a") as answer_file:
        # Protection for division by zero case.
        if (operand_2 == 0) and (operator == "/"):
            answer_file.write("{} {} {}".format(operand_1, operator, operand_2)
                              + " is not defined\n")
        else:
            answer_file.write("{} {} {} = {}\n".format(
                operand_1,
                operator,
                operand_2,
                operator_dict[operator](operand_1, operand_2)))

# File reading mode:
else:
    # Show user proper formatting to read the file properly:
    print("""\nPlease ensure that the file to read is formatted as follows:

    (a) Each equation is written on a single line
    (b) Each equation is written like 'x operator y'
    (c) Each operand is a number
    (d) The given operator is one of '+', '-', '*', '/', '**'

Any equation that does not satisfy these conditions will result in error.
""")
    # Look for user entered filename.
    while True:
        try:
            file_name = input("\nEnter the name of the file to read: ")
            equation_file = open(file_name, "r")
        except FileNotFoundError:
            print("\nI couldn't find a file named {}!".format(file_name))
        else:
            break
    # Save the file contents immediately so the file can be closed quickly.
    equations = [equation.strip("\n") for equation in equation_file]
    equation_file.close()

    for equation in equations:
        current_eq = equation.split(" ")
        # Check the equation has exactly two operands and one operator.
        if (len(current_eq) == 1) or (len(current_eq) > 3):
            print("\nError (b), invalid equation format: {}".format(equation))

        else:
            # Check the operands are numbers.
            try:
                operand_1 = float(current_eq[0])
                operand_2 = float(current_eq[2])
            except ValueError:
                print("\nError (c), non-number operands: {}".format(equation))
            else:
                operator = current_eq[1]
                # Check if operator is valid.
                if operator not in operator_dict.keys():
                    print("\nError (d),"
                          " unrecognised operator: {}".format(operator))
                # Check for division by zero
                elif (operator == "/") and (operand_2 == 0):
                    print("\n" + equation,
                          "- Division by zero is undefined!")
                # If no errors, print equation and answer.
                else:
                    print("\n" + equation + " =",
                          operator_dict[operator](operand_1, operand_2))

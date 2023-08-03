# Robust-Calculator
A two-mode robust calculator made using Python

---

A calculator that accepts any binary equation. When running the file, prompts the user to select a mode:

### Mode 1: Standard

Like a conventional calculator, first prompts the user for the operands and then an operator. Operands can be any `float` and operators can be any simple binary operator:
| Operator | |
| --- | --- |
| `+` | Addition, x + y |
| `-` | Subtraction, x - y |
| `*` | Multiplication, x * y |
| `/` | Division, x / y |
| `**` | Exponentiation, x ^ y |

The program will then print the solution to the equation and append the whole equation to a `calc_answers.txt` file, creating such a file if necessary.

### Mode 2: File

When this mode is selected, the user is prompted for the name of a `.txt` file where each line is an unanswered equation. If a line in the file satifies all of:
| Condition | |
| --- | --- |
| (a) | Each equation is written on a single line |
| (b) | Each equation is written like 'x operator y'|
| (c) | Each operand is a number|
| (d) | The given operator is one of +, -, *, /, **|

Then the equation on the line is entered and answered by the calculator. If a line does not satisfy any of the conditions then the calculator will raise and error and continue to the next line.

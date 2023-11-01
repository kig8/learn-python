exp = input("Expression: ")
x, y, z = exp.split(" ")
x = float(x)
z = float(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        if z != 0:
            result = x / z

if z == 0 and y == "/":
    result = "0-val nem lehet osztani"
else:
    result = f"{result:.1f}"


print(result)

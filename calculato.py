def recur():
    try:
         a = float(input("Enter first number: "))
         op = input("Enter operator (+, -, *, /): ")
         b = float(input("Enter second number: "))

         if op == "+":
            print("Result:", a + b)
         elif op == "-":
            print("Result:", a - b)
         elif op == "*":
            print("Result:", a * b)
         elif op == "/":
            print("Result:", a / b)
         else:
            print("Invalid operator!")

    except ValueError:
        print("Try only numericals.")
        recur()
    except ZeroDivisionError:
        print("Zero can't be a denominator Try another number.")
        recur()
recur()
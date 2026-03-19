# Simple Python Calculator

print("Hello! Let's do some math.")

# Taking user inputs
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing calculations
    sum_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2

    # Handling division by zero
    if num2 != 0:
        div_result = num1 / num2
    else:
        div_result = "Undefined (cannot divide by zero)"

    # Displaying results
    print("\n--- Results ---")
    print(f"Sum:        {sum_result}")
    print(f"Difference: {sub_result}")
    print(f"Product:    {mul_result}")
    print(f"Division:   {div_result}")

except ValueError:
    print("Oops! Please enter valid numbers next time.")

# JENNIE ROSE PAITAN
# PHMAN19

# Function to calculate the sum of two numbers
def add(x, y):
    return x + y

# Function to calculate the difference of two numbers
def subtract(x, y):
    return x - y

# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Function to calculate the quotient of two numbers
def divide(x, y):
    return x / y

# Displaying a menu of available operations for the user to select
print("Select an operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division \n")

while True:
    # Get an input from the user among options
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num_1 = float(input("Please enter first number: "))
            num_2 = float(input("Please enter second number: "))
        except ValueError:
            print("Invalid Input. Please enter a Number.")
            continue

        if choice == '1':
            print(num_1, "+", num_2, "=", add(num_1, num_2))

        elif choice == '2':
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))

        elif choice == '3':
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))

        elif choice == '4':
            print(num_1, "/", num_2, "=", divide(num_1, num_2))
        
        # Check if user wants another calculation
        new_calc = input("Do you want to perform calculations again? (Yes/No): ")
        if new_calc == "No":
          break
    else:
        print("Invalid Input. Please answer with Yes/No")

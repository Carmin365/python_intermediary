try:
    num = int(input("Enter a number"))
    if num <= 0:
        raise ValueError("The number must be positive")
    print(f"the square of the number is: {num ** 2}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

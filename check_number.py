def check_number(prompt, minimum, maximum):
    while True:
        try:
            value = int(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a number between {minimum} and {maximum}.")

        except ValueError:
            print("Please enter a number.")
def main():
    # Prompt the user for camel case input
    name = input("camelCase: ")
    # Display the user input as snake case using nake_case function
    print(f"snake_case: {snake_case(name)}")


def snake_case(name):
    # Loop through every characters in the input name
    for char in name:
        # Check if the character is upper case
        if char.isupper():
            # Replace the upper case character with "_" + lower case character
            name = name.replace(char, f"_{char.lower()}")
    return name


if __name__ == "__main__":
    main()

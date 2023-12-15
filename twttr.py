def main():
    # Prompt the user for input text
    user_input = input("Input: ")
    # Print out the user input with vowels removed
    print(remove_vowels_from(user_input))


def remove_vowels_from(prompt):
    vowels = ["a", "e", "i", "o", "u"]
    # Create a list containing all characters except vowels from the user input
    omit_vowels = [char for char in prompt if char.lower() not in vowels]
    # Convert the list back to a string and return it
    return "".join(omit_vowels)


if __name__ == "__main__":
    main()

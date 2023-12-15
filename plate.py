from string import punctuation


def main():
    # Prompt the user for a vanity plate input
    plate = input("Plate: ")

    # Check whether the user input passes the requirements
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Vanity plates can contain a maximum of 6 characters and a minimum of 2 characters
    if 2 <= len(s) <= 6:
        # Must start with at least two letters
        if s[:2].isalpha():
            for char in s:
                # The first number used cannot be '0'
                if char.isnumeric() and char != "0":
                    alpha, num = s[: s.index(char)], s[s.index(char) :]

                    # Numbers cannot be used in the middle of a plate; they must come at the end
                    if num.isnumeric():
                        # No periods, spaces, or punctuation marks are allowed
                        if sum(char.isalnum() for char in s) == len(s):
                            return True
                break  # Break after the first numeric character is found
    return False


if __name__ == "__main__":
    main()

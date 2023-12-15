def main():
    coke()


def coke():
    price = 50
    while price > 0:
        # Print out the amount user still dues
        print(f"Amount due: {price}")
        # Prompt user input for coin
        coin = int(input("Insert Coin: "))
        # Check wheather the user input was accepted
        if coin == 25 or coin == 10 or coin == 5:
            price -= coin
    # Print out how many cents in change the user is owed
    print(f"Change Owed: {-price}")


if __name__ == "__main__":
    main()

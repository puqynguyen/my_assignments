fruits = {
    "Apple": 130,
    "Avocado California": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Watermelon": 80,
}


def main():
    # Prompt the user for case-insensitive input for a fruit name
    item = input("Item: ").lower()
    # Print out the number of calories in one portion of that fruit
    calories_in(item)


def calories_in(item):
    # Create a lower case dictionary to find item case-insensitively
    lower_fruits = {fruit.lower(): nutrition for fruit, nutrition in fruits.items()}
    # Print out the calories if the item is in the lower case dictionary
    if item in lower_fruits:
        print(f"Calories: {lower_fruits[item]}")

if __name__ == "__main__":
    main()

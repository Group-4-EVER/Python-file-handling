# Shopping List Manager
# Combined functionality for adding and reading shopping items

def read_shopping_list(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()

            if not items:
                print("Shopping list is empty.")
                return

            print("🛒 Shopping List:")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")

            print(f"\nTotal items: {len(items)}")

    except FileNotFoundError:
        print("Shopping list file not found.")

def create_shopping_file(filename):
    try:
        f = open(filename, "x")
        f.write("SHOPPING LIST\n")
        f.close()
        print("File created successfully.")
        return True
    except FileExistsError:
        print("File already exists.")
        return False

def add_initial_item(filename):
    item = input("Enter shopping item: ")
    f = open(filename, "w")
    f.write("Shopping Item: " + item + "\n")
    f.close()
    print("Item saved successfully.")

def main():
    filename = "shopping.txt"

    # Create file if it doesn't exist
    file_created = create_shopping_file(filename)

    if file_created:
        # If file was just created, add initial item
        add_initial_item(filename)

    print("\n--- Shopping List Manager ---")

    while True:
        print("\n1. Add New Item")
        print("2. View Shopping List")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter shopping item: ")

            with open(filename, "a") as file:
                file.write("Shopping Item: " + item + "\n")

            print(f"Successfully added {item} to the list.")

        elif choice == "2":
            read_shopping_list(filename)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
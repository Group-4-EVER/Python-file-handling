# Shopping List Manager
# Student A - x and w mode

try:
    f = open("shopping.txt", "x")
    f.write("SHOPPING LIST\n")
    f.close()

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

item = input("Enter shopping item: ")

f = open("shopping.txt", "w")
f.write("Shopping Item: " + item)

f.close()

print("Item saved successfully.")

 #Student C - read mode
def read_shopping_list(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()

            if not items:
                print("Shopping list is empty.")
                return

            print("\nShopping List:")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")

            print(f"\nTotal items: {len(items)}")

    except FileNotFoundError:
        print("Shopping list file not found.")

#Student D - Update Functionality
def update_item():
    old_item = input("Enter item to update: ")
    new_item = input("Enter new item: ")

    try:
        with open("shopping.txt", "r") as file:
            items = file.readlines()

        with open("shopping.txt", "w") as file:
            for item in items:
                if old_item.strip() in item:
                    file.write(item.replace(old_item, new_item))
                else:
                    file.write(item)

        print("Item updated successfully.")

    except FileNotFoundError:
        print("Shopping list file not found.")
        
# Student B - append(a) mode

print("\n--- Shopping List Manager ---")

while True:
    print("\n1. Add New Item")
    print("2. Read Items")
    print("3. Update Item")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Append mode
    if choice == "1":
        item = input("Enter shopping item: ")

        with open("shopping.txt", "a") as file:
            file.write("Shopping Item: " + item + "\n")

        print(f"Successfully added {item} to the list.")

    elif choice == "2":
        read_shopping_list("shopping.txt")

    elif choice == "3":
        update_item()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid input. Please try again.")  
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

# Student B - append(a) mode

print("\n--- Shopping List Manager (Append Mode) ---")

while True:
    print("\n1. Add New Item")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter shopping item: ")

        with open("shopping.txt", "a") as file:
            file.write("Shopping Item: " + item + "\n")

        print(f"Successfully added {item} to the list.")

    elif choice == "2":
        print("Exiting program...")
        break

    else:
        print("Invalid input. Please try again.")   

 
  def read_shopping_list(filename):
    try:
        with open(filename, 'r') as file:
            items = file.readlines()

            if not items:
                print("Shopping list is empty.")
                return

            print("Shopping List:")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")

            print(f"\nTotal items: {len(items)}")

    except FileNotFoundError:
        print("Shopping list file not found.")

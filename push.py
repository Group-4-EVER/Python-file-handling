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
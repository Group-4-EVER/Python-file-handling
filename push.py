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
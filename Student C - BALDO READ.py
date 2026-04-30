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
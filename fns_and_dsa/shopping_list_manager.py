def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                if choice == 1:
                    # Add item
                    item = input("Enter the item to add: ")
                    shopping_list.append(item)
                    print(f"{item} added to the list!")
                elif choice == 2:
                    # Remove item
                    item = input("Enter the item name to remove: ")
                    if item in shopping_list:
                        shopping_list.remove(item)
                        print(f"{item} removed from the list.")
                    else:
                        print(f"Item '{item}' not found in the list.")
                elif choice == 3:
                    # View list
                    if shopping_list:
                        print("Shopping List:")
                        for i, item in enumerate(shopping_list, start=1):
                            print(f"{i}. {item}")
                    else:
                        print("The shopping list is empty.")
                else:
                    print("Goodbye!")
                    break
            else:
                print("Invalid choice (enter a number between 1 and 4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

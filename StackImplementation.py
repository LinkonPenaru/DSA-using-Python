#Now I will create a organized way to insert the data and pop the data using the user command

stack = []

while True:
    x = input("Enter a number (or type 'esc' to stop): ")

    if x.lower() == "esc":
        print("Exiting the loop...")
        break

    try:
        x = int(x)
        stack.append(x)
        print("Current Stack:", stack)
    except ValueError:
        print("Invalid input! Please enter a number or type 'esc'.")

if stack:

    print("\nN.B. Deleting from stack removes values from the end (LIFO).")

    while stack:
        x = input("Press 1 to delete from stack / 0 to exit: ")

        try:
            x = int(x)

            if x == 1:
                removed = stack.pop()
                print("Removed:", removed)
                print("Current Stack:", stack)

            elif x == 0:
                print("Exiting the loop...")
                break

            else:
                print("Wrong input!")

        except ValueError:
            print("Invalid input! Use 0 to exit and 1 to delete.")


else:
    print("Nothing to be deleted..")




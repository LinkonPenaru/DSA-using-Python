"""
Queue Implementation in Python
Author: Rithik Linkon Penaru

Description:
    - Enqueue elements into queue
    - Dequeue elements from queue
    - Demonstrates FIFO principle

Time Complexity:
    Enqueue: O(1)
    Dequeue: O(1)
"""

from collections import deque

queue = deque()

while True:
    x = input("Enter a number (or type 'esc' to stop): ")

    if x.lower() == "esc":
        print("Exiting the loop...")
        break

    try:
        x = int(x)
        queue.append(x)
        print("Current queue:", queue)
    except ValueError:
        print("Invalid input! Please enter a number or type 'esc'.")

if queue:

    print("\nN.B. Deleting from queue removes values from the top (FIFO).")

    while queue:
        x = input("Press 1 to delete from queue / 0 to exit: ")

        try:
            x = int(x)

            if x == 1:
                removed = queue.popleft()
                print("Removed:", removed)
                print("Current queue:", queue)

            elif x == 0:
                print("Exiting the loop...")
                break

            else:
                print("Wrong input!")

        except ValueError:
            print("Invalid input! Use 0 to exit and 1 to delete.")


else:
    print("Nothing to be deleted..")




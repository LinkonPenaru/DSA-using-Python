# Stack uses LIFO(Last In First Out), meaning the latest data inserted in the list is to be removed at first. In my example I will be using list to create a basic stack structure.

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop() # pop removes the last value
stack.pop()

print(stack)
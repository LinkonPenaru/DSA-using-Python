# Queue uses FIFO meaning First In First Out.
# Queue using List

queue = []

#Enqueue(this means insert in the queue)
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# Dequeue(this means removing data from the front)
remove = queue.pop(0) # just pop() would've removed the last element instead of first data
print("Removed element: ",remove)
print("using pop(0) will cause the whole queue to shift at first which causes O(n) time this is not the best way to do this\n"
      "rather use collection deque for O(1) time :)")
print(queue)
remove = queue.pop(0)
print("Removed element: ",remove)
print(queue)



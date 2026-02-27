from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# popleft will cause O(1) time
remove = queue.popleft()
print("Removed Item using popleft(): ",remove)
print(queue)
remove = queue.popleft()
print(remove)
print(queue)

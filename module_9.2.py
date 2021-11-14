from collections import deque
dq = deque([6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9])
dq_one = dq.popleft()
print(dq_one)
print(dq)
dq.rotate(-5)

print(dq)
dq_two = dq.pop()
print(dq_two)
print(dq.count(dq_two))




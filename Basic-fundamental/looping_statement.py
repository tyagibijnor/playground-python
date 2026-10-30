# Looping Statement Examples in Python

# 1. For Loop - iterate over a sequence
print("=== For Loop ===")
for i in range(5):
    print(f"Iteration {i}")

# 2. For Loop with List
print("\n=== For Loop with List ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. While Loop - execute while condition is true
print("\n=== While Loop ===")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# 4. For Loop with range and step
print("\n=== For Loop with Step ===")
for i in range(0, 10, 2):
    print(i)

# 5. Nested Loop
print("\n=== Nested Loop ===")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 6. Loop with break statement
print("\n=== Break Statement ===")
for i in range(5):
    if i == 3:
        break
    print(i)

# 7. Loop with continue statement
print("\n=== Continue Statement ===")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 8. For-else loop (else executes when loop completes normally)
print("\n=== For-Else Loop ===")
for i in range(3):
    print(i)
else:
    print("Loop completed successfully!")

## range with loop
for i in range(5, 10, 2):
    print(f"Range value: {i}") 

for i in range(10, 0, -1):
    print(f"Countdown: {i}")    

for i in range(6):
    print(f"Square of {i}: {i**2}")
          

q=0
while q < 5:
    print(f"While Loop Count: {q}")
    q += 1 

    

# Ask how many numbers to sort
n = int(input("Enter number of inputs: "))

numbers = []
for i in range(n):
    num = int(input(f"Input {i+1}: "))
    numbers.append(num)

sorted_list = []
tree = []

for num in numbers:
    if not tree:
        tree.append([num, [], []])
    else:
        current = tree[0]
        while True:
            if num < current[0]:
                if current[1]:
                    current = current[1]
                else:
                    current[1] = [num, [], []]
                    break
            else:
                if current[2]:
                    current = current[2]
                else:
                    current[2] = [num, [], []]
                    break

# Get sorted numbers (in-order traversal)
result = []
stack = []
current = tree[0] if tree else None

while stack or current:
    while current:
        stack.append(current)
        current = current[1]
    current = stack.pop()
    result.append(current[0])
    current = current[2]

print("Sorted numbers:", result)

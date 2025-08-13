numbers = []
print("Enter numbers one by one. Type 'done' to finish.")

bst = []

while True:
    user_input = input("Enter a number (or 'done' to exit): ")

    if user_input.lower() == 'done':
        break
    
    number = int(user_input)
    numbers.append(number)

    if not bst:
        bst.append([number, [], []])  # Create a new tree node
    else:
        current = bst[0]  # Start with the root node
        while True:
            if number < current[0]:  # Go to the left
                if current[1]:  # Check if left subtree exists
                    current = current[1]  # Move to the left subtree
                else:
                    current[1] = [number, [], []]  # Insert the number
                    break
            else:  # Go to the right
                if current[2]:  # Check if right subtree exists
                    current = current[2]  # Move to the right subtree
                else:
                    current[2] = [number, [], []]  # Insert the number
                    break

    sorted_list = []
    stack = []
    current = bst[0] 

    while stack or current:
        while current:
            stack.append(current)
            current = current[1]  # Move to the left child
        current = stack.pop()
        sorted_list.append(current[0])  # Append the node value
        current = current[2]  # Move to the right child

    print("Current sorted list (Tree Sorted):", sorted_list)

print("Final sorted list (Tree Sorted):", sorted_list)

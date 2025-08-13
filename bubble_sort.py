numbers = []
print("Enter numbers one by one. Type 'done' to finish.")

while True:
    user_input = input("Enter a number (or 'done' to exit): ")

    if user_input.lower() == 'done':
        break
    
    numbers.append(int(user_input))
    
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    print("Current sorted list (Bubble Sorted):", numbers)

print("Final sorted list (Bubble Sorted):", numbers)

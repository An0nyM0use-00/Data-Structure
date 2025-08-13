numbers = []
print("Enter how many numbers you want to input:")
count = int(input("Number of inputs : "))

print("Enter numbers one by one.")
for _ in range(count):
    user_input = input("Enter a number : ")
    numbers.append(int(user_input))

n=len(numbers)
for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j]> numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+ 1], numbers[j]

display_choice = input("How would you like to display the final sorted list? (type 'asc' for ascending or 'desc' for descending):")
if display_choice.lower() == 'desc':
    numbers.reverse()
print("Final sorted list :", numbers)
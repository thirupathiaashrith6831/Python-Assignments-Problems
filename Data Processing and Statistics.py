# assignment_for_loops.py

def analyze_numbers(numbers):
    total_sum = 0
    largest_num = numbers[0] if numbers else 0
    even_count = 0

    for num in numbers:
        # Task 1: Summation
        total_sum += num
        
        # Task 2: Finding the maximum
        if num > largest_num:
            largest_num = num
            
        # Task 3: Counting evens
        if num % 2 == 0:
            even_count += 1
            
    return total_sum, largest_num, even_count

# Test Data
data = [12, 45, 7, 23, 56, 89, 2, 10]
s, m, e = analyze_numbers(data)

print(f"List: {data}")
print(f"Total Sum: {s}")
print(f"Max Value: {m}")
print(f"Even Count: {e}")
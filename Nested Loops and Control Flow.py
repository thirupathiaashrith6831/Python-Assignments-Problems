# assignment_prime_finder.py

def get_prime_numbers():
    print("--- Prime Number Range Finder ---")
    
    # Task 1: Use while loop for input validation
    is_valid = False
    while not is_valid:
        try:
            limit = int(input("Enter the upper limit to search for primes (e.g., 50): "))
            if limit > 1:
                is_valid = True
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    primes = []

    # Task 2: Use for loop to check each number in the range
    for num in range(2, limit + 1):
        is_prime = True
        
        # Task 3: Nested for loop to check for factors
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # Stop checking if a factor is found
        
        if is_prime:
            primes.append(num)

    # Task 4: Output the results
    print(f"\nPrime numbers between 2 and {limit}:")
    print(primes)
    print(f"Total count: {len(primes)}")

if __name__ == "__main__":
    get_prime_numbers()
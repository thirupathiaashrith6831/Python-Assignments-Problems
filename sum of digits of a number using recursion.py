def sum_of_digits(n):
    if n == 0:          # base case
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print("Sum of digits:", sum_of_digits(1234))

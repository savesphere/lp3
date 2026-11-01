# Fibonacci using Iterative and Recursive Methods

# Iterative Method
def fibonacci_iterative(n):
    a, b = 0, 1
    step_count = 0

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        step_count += 1

    print("\nStep Count (Iterative):", step_count)


# Recursive Method
step_count = 0

def fibonacci_recursive(n):
    global step_count
    step_count += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive integer")
else:
    print("\nFibonacci using Iterative Method:")
    fibonacci_iterative(n)

    print("\nFibonacci using Recursive Method:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\nStep Count (Recursive):", step_count)

    print("\nTime and Space Complexity:")
    print("Iterative: Time O(n), Space O(1)")
    print("Recursive: Time O(2^n), Space O(n)")
def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = []
    while n > 0:
        sequence.append(a)
        a, b = b, a + b
        n -= 1
    return sequence

def fibonacci_recursive(n, sequence=[0, 1]):
    if n <= len(sequence):
        return sequence[:n]
    else:
        sequence.append(sequence[-1] + sequence[-2])
        return fibonacci_recursive(n, sequence)

if __name__ == "__main__":
    num = 10
    print("Fibonacci Iterative:", fibonacci_iterative(num))
    print("Fibonacci Recursive:", fibonacci_recursive(num))

# fibonacci sequence 

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = fibonacci_recursive(n - 1)
    next_value = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_value)
    
    return fib_sequence

def main():
    num = int(input())
    fib_seq = fibonacci_recursive(num)
    print(fib_seq)

if __name__ == "__main__":
    main()
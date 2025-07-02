from time import perf_counter as t
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
    start_time = t()
    fib_seq = fibonacci(num)
    end_time = t()
    print(fib_seq)
    print(f"Time taken (iterative): {end_time - start_time:.6f} seconds\n")

    start_time = t()
    fib_seq_recursive = fibonacci_recursive(num)
    end_time = t()
    print(fib_seq_recursive)
    print(f"Time taken (recursive): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
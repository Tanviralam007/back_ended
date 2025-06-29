# factorial number

# without recursion: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

# with recursion: 5! = 5 * 4!
def factorial_recursive(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    num = int(input())
    fact = factorial(num)
    print(fact)

if __name__ == "__main__":
    main()
# Extract Digits from A Given Number
import math

def extract_number(n):
    ans = []
    while n > 0:
        last_digit = n % 10
        ans.append(last_digit)
        n = n // 10
    ans.reverse()
    return ans

def main():
    N = int(input())
    digits = extract_number(N)
    print(digits)

if __name__ == "__main__":
    main()
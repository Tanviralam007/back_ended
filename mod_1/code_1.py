# Extract Digits from A Given Number
import math

def extract_number(N):
    ans = []
    while N > 0:
        last_digit = N % 10
        ans.append(last_digit)
        N = math.floor(N / 10)
    ans.reverse()
    return ans

def main():
    N = int(input())
    digits = extract_number(N)
    print(digits)

if __name__ == "__main__":
    main()
# Counts the number of digits in a given integer N
def count_digits(N):
    count = 0
    while N > 0:
        N = N // 10 # Integer division to remove the last digit
        count += 1
    return count

def main():
    N = int(input())
    digit_count = count_digits(N)
    print(digit_count)

if __name__ == "__main__":
    main()
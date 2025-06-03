# reverses a given integer, handling both positive and negative numbers
def reverse_num(n):
    is_negative = n < 0 # Check if the number is negative
    n = abs(n)
    reverse_num = 0
    while n > 0:
        last_digit = n % 10 # Get the last digit
        reverse_num = reverse_num * 10 + last_digit # Append it to the reversed number
        n = n // 10 # Remove the last digit from n
    
    if is_negative:
        return -reverse_num
    else:
        return reverse_num

def main():
    n = int(input())
    reverse = reverse_num(n)
    print(reverse)

if __name__ == "__main__":
    main()
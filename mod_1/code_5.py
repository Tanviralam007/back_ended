# check if the number is an amstrong number
def is_armstrong(n):
    original = n
    total = 0
    num_digits = len(str(n))
    
    while n > 0:
        last_digit = n % 10 # get the last digit
        total = total + (last_digit ** num_digits) # calculate the power of the digit
        n = n // 10 # remove the last digit from n
    
    return original == total

def main():
    n = int(input())
    if is_armstrong(n):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
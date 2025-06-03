# check if a string is a palindrome (convert integer to string)
def palindrome(s):
    return s == s[::-1]

def main():
    s = input()
    if palindrome(s):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()

# without converting to string
def is_palindrome(n):
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num

def main():
    n = int(input())
    if is_palindrome(n):
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
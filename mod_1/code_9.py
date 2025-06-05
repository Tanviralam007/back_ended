# Find the GCD of two numbers with recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a = int(input())
    b = int(input())
    print(gcd(a, b))

if __name__ == "__main__":
    main()

'''
sample input:
12
15
sample output:
3

explaination:
The function gcd takes two integers a and b as input. Let's say a = 12 and b = 15.

1. It checks if b is equal to 0, which it is not.
Then it calls itself with the arguments b and a % b, which are 15 and 12 % 15 (which is 12).

2. In the next call, it checks if b is equal to 0, which it is not.
Then it calls itself with the arguments b and a % b, which are 12 and 15 % 12 (which is 3).

3. In the next call, it checks if b is equal to 0, which it is not.
Then it calls itself with the arguments b and a % b, which are 3 and 12 % 3 (which is 0).

4. In the next call, it checks if b is equal to 0, which it is.
So it returns a, which is 3.
'''
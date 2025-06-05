# Find the GCD of two numbers without recursion
# using the Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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
It enters a while loop that continues until b is not equal to 0.
In the first iteration, it sets a = 15 and b = 12 % 15, which is 12.
In the second iteration, it sets a = 12 and b = 15 % 12, which is 3.
In the third iteration, it sets a = 3 and b = 12 % 3, which is 0.
Since b is now 0, the loop ends and the function returns a, which is 3.
'''
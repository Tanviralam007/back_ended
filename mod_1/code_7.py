# prime number checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()

'''
sample input:
10
sample output:
Not prime

explaination:
when you input n = 10, the function is_prime will get called with n = 10.
the function checks if 10 is less than or equal to 1, which it is not.
then it enters a loop from 2 to the int(10**0.5) + 1 (square root check), which is 4.
it checks if 10 is divisible by 2, which it is, so it returns False.
if the function returns False, the main function prints "Not prime".

sample input:
5
sample output:
Prime

explaination:
when you input n = 5, the function is_prime will get called with n = 5.
the function checks if 5 is less than or equal to 1, which it is not.
then it enters a loop from 2 to the int(5**0.5) + 1, which is 3.
it checks if 5 is divisible by 2, which it is not.
then it checks if 5 is divisible by 3, which it is not.
finally, it returns True.
the main function then prints "Prime".
'''
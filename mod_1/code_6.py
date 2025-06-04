# print all the divisors of a number
def print_divisors(n):
    divisors = []
    for i in range(1, n + 1): # loop from 1 to n
        if n % i == 0: # check if i is a divisor of n
            divisors.append(i) # add i to the list of divisors
    return divisors

def main():
    n = int(input())
    divisors = print_divisors(n)
    print(divisors)

    # calculate the sum of divisors
    sum_of_divisors = sum(divisors) 
    print(sum_of_divisors)

if __name__ == "__main__":
    main()
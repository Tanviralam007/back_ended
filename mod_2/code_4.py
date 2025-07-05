'''
Given an array nums of length n, return an array output such that:
output[i] = product of all elements in nums except nums[i]
'''

def product_except_self(arr: list[int]):
    n = len(arr)
    out = [1] * n

    # left pass
    left_product = 1
    for i in range(n):
        out[i] = left_product
        left_product = left_product * arr[i]
    
    # right pass
    right_product = 1
    for i in range(n - 1, -1, -1):
        out[i] = out[i] * right_product
        right_product = right_product * arr[i]

    return out

def main():
    arr = list(map(int, input().split()))
    print(product_except_self(arr))

if __name__ == "__main__":
    main()

'''
input: [1, 2, 3, 4]
output: [24, 12, 8, 6]
'''
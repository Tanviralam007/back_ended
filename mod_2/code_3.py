# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return its sum.

# Print all the sub-arrays
def subarrays(arr):
    n = len(arr)
    subset = []
    for i in range(n):
        for j in range(i, n):
            subset.append(arr[i:j+1])
    return subset

def max_subarray_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    # Kadanes' Algorithm
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    return max_sum

def main():
    arr = list(map(int, input().split()))
    # print(subarrays(arr))
    # print(max_subarray_sum(arr))

if __name__ == "__main__":
    main()
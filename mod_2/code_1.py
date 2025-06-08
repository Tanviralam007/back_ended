'''
Problem Statement: Given an array of integers arr[] and an integer target.
1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
'''

def has_pair_with_sum(arr, target, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return "YES"
    return "NO"

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    print(has_pair_with_sum(arr, target, n))

if __name__ == "__main__":
    main()

'''
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.
'''

def find_indices_with_sum(arr, target, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    result = find_indices_with_sum(arr, target, n)
    print(result)

if __name__ == "__main__":
    main()
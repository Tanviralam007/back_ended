# best time to buy and sell stock

# brute force
def max_profit(prices : list[int]):
    max_profit = float('-inf') # Initialize to negative infinity

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    
    if max_profit < 0:
        return 0
    return max_profit

# optimized solution using two pointers
def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = float('-inf')

    for price in prices:
        if price < min_price:
            min_price = price
        
        profit = price - min_price
        if profit > max_profit:
            max_profit = price - min_price

    return [min_price, max_profit]

def main():
    prices = list(map(int, input().split()))
    # print(max_profit(prices))
    print(maxProfit(prices))

if __name__ == "__main__":
    main()
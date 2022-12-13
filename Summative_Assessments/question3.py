def maximum_toys(prices, budget):
    prices.sort()
    max_toys = 0
    spent = 0
    for price in prices:
        if spent + price > budget:
            return max_toys
        max_toys += 1
        spent += price
    return max_toys

# Example
prices = [1, 2, 3, 4]
budget = 7
num_toys = maximum_toys(prices, budget)
print(num_toys)  # 3

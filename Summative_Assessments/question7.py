def change_combinations(sum, coins):
    # Step 1
    dp = [0] * (sum + 1)
    
    # Step 2
    for c in coins:
        # Step 2a
        dp[0] = 1
        
        # Step 2b
        for i in range(1, sum+1):
            if i - c >= 0:
                dp[i] = dp[i] + dp[i - c]
    
    # Step 3
    return dp[sum]

# Example
sum = 10
coins = [2, 5, 3, 6]
print(change_combinations(sum, coins))  # Expected result is 5

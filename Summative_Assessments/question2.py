def staircase(n):
    num_spaces = n - 1
    for i in range(n):
        print(' ' * num_spaces + '#' * (n - num_spaces))
        num_spaces -= 1

# Example
staircase(6)

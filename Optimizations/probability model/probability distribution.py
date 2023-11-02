import random

# Number of coin flips
num_flips = 1000

# Simulate coin flips (0 represents Tails, 1 represents Heads)
coin_flips = [random.randint(0, 1) for _ in range(num_flips)]

# Calculate the probability of getting Heads
num_heads = coin_flips.count(1)
probability_heads = num_heads / num_flips

print(f"Number of Heads: {num_heads}")
print(f"Number of Tails: {num_flips - num_heads}")
print(f"Probability of getting Heads: {probability_heads:.2f}")
print(f"Probability of getting Tails: {1 - probability_heads:.2f}")

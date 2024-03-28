import random

# Define the transition matrix
transition_matrix = [[0 for _ in range(70)] for _ in range(70)]

# Hypothetical lottery data (replace with real data if available)
lottery_data = [
    [6,23,25,34,51],  # Sample data
    [13,22,27,54,66],
    [10,17,20,39,44],
    [12,23,44,57,61],
    [21,29,54,59,62],
    [1,3,7,16,66]# Sample data
    # Add more sample data here...
]

# Build the transition matrix from sample data
for sequence in lottery_data:
    for i in range(len(sequence) - 1):
        transition_matrix[sequence[i]][sequence[i + 1]] += 1

# Normalize each row of the matrix (get probabilities)
for row in transition_matrix:
    total = sum(row)
    if total > 0:
        for i in range(len(row)):
            row[i] /= total
    else:
        # Handle cases where a number never appeared after another (assign equal probability)
        for i in range(len(row)):
            row[i] = 1 / 70

# Generate a starting number (randomly select from entire range)
current_state = random.randint(1, 69)

# Generate 5 numbers using the Markov chain
generated_numbers = [current_state]
for _ in range(4):
    next_state = random.choices(range(70), weights=transition_matrix[current_state])[0]
    generated_numbers.append(next_state)
    current_state = next_state

print("Generated numbers:", generated_numbers)
past = [37,46,57,60,66]
while(generated_numbers == past):
    print("Match", generated_numbers)
else:
    print("no Match")
# Disclaimer
print("\nDisclaimer: This is a simulated example. Lottery drawings are designed to be random, and past results do not influence future outcomes. This approach should not be used for real lotteries.")

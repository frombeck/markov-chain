from random import randint, choices

# Sample lottery data placeholder (replace with real data)
data = [
    [6,23,25,34,51],  # Sample data
    [13,22,27,54,66],
    [10,17,20,39,44],
    [12,23,44,57,61],
    [21,29,54,59,62],
    [1,3,7,16,66]
    
    ]  # Empty list to handle potential missing data

try:
  # Assuming you have lottery data stored in a list (replace with actual data source)
  with open("lottery_data.txt", "r") as file:  # Open data file for reading
    data = [list(map(int, line.strip().split())) for line in file]  # Parse data lines
except FileNotFoundError:
  print("WARNING: Lottery data file not found. Using empty data.")

# Build transition matrix with dictionary comprehension
transition_matrix = {i: {j: 0 for j in range(70)} for i in range(70)}
for seq in data:
    for i in range(len(seq) - 1):
        transition_matrix[seq[i]][seq[i + 1]] += 1

# Normalize rows using map and lambda
for row in transition_matrix.values():
    s = sum(row.values())
    row.update({k: v / s if s else 1/70 for k, v in row.items()})

# Generate sequence
start = randint(1, 69)
sequence = [start]
for _ in range(4):
    next_state = choices(population=range(70), weights=transition_matrix[start])[0]
    sequence.append(next_state)
    start = next_state

print("Generated numbers:", sequence)
print("\nDisclaimer: Educational purposes only. Lotteries are random.")

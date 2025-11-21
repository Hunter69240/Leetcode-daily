a = [2, 1, 1, 5]           # Initial scores of players

d = {}                     # Dictionary to count occurrences of each score

# Build the count dictionary
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

change_index = 2           # The index (0-based) of the player to update (3rd player)
new_score = 3              # The new score to set for that player

unique_scores = set(a)     # Set of unique scores currently present

old_score = a[change_index]    # The old score at the given index

# Decrease count of the old score
d[old_score] -= 1
if d[old_score] == 0:
    del d[old_score]           # Remove old score from dictionary if it's no longer present
    unique_scores.remove(old_score) # Remove old score from unique_scores if gone

# Increase/add count for the new score
if new_score in d:
    d[new_score] += 1
else:
    d[new_score] = 1
    unique_scores.add(new_score)

a[change_index] = new_score    # Update the score in the array

print(len(unique_scores) + 1)  # Print the number of unique scores + 1 (the number of possible distinct ranks for the new player)

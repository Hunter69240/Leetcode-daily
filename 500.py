rows = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}

words = ["Hello", "Alaska", "Dad", "Peace"]

result = []

# Check each word in the list
for word in words:
    # Check each row to see if the word can be typed using letters from this row only
    for i in rows:
        # Convert word to lowercase and check all characters belong to the current row
        if all(char.lower() in rows[i] for char in word):
            result.append(word)  # If yes, add word to result list
            break  # No need to check other rows for the current word

print(result)

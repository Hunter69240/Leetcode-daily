class TimeMap:
    def __init__(self):
        # Initialize a dictionary to store key -> list of [value, timestamp] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary, initialize it with an empty list
        if key not in self.store:
            self.store[key] = []
        # Append the value along with its timestamp to the list corresponding to the key
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Default result is an empty string if no matching timestamp is found
        res = ""
        # Get the list of [value, timestamp] pairs for the key, or an empty list if key doesn't exist
        values = self.store.get(key, [])

        # Binary search to find the value with the largest timestamp <= given timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # If current timestamp is less than or equal to the given timestamp,
            # it's a potential result; store it and continue to search to the right
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                # If current timestamp is greater than the given one, search to the left
                r = m - 1
        return res


# Example usage:
# obj = TimeMap()
# obj.set(key, value, timestamp)  # Store the value at the given timestamp for the key
# param_2 = obj.get(key, timestamp)  # Retrieve the value with the largest timestamp <= given timestamp

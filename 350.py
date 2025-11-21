nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

# Create dictionaries to store frequency (count) of each element in nums1 and nums2
d1 = {}
d2 = {}

# Count frequency of elements in nums1 and store in d1
for i in nums1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1

# Count frequency of elements in nums2 and store in d2
for i in nums2:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1

# Initialize result list to store common elements (including duplicates)
result = []

# Loop through each key in d1
for i in d1:
    # If the element exists in both dictionaries
    if i in d2:
        # Add the element to result min(number of times it appears in both lists)
        for j in range(min(d1[i], d2[i])):
            result.append(i)

# Print the final list containing the intersection (including duplicates)
print(result)

# nums1 = [4, 9, 5, 8]
# nums2 = [9, 4, 9, 8, 4, 5]

# # Create dictionaries to store frequency of each element in nums1 and nums2
# d1 = {}
# d2 = {}

# # Count frequency of elements in nums1
# for i in nums1:
#     if i in d1:
#         d1[i] += 1
#     else:
#         d1[i] = 1

# # Count frequency of elements in nums2
# for i in nums2:
#     if i in d2:
#         d2[i] += 1
#     else:
#         d2[i] = 1

# # Initialize result list to store common elements
# result = []

# # Loop through keys in first dictionary
# for i in d1:
#     # If the key exists in both dictionaries and is not already added to result
#     if i in d2 and i not in result:
#         result.append(i)  # Add to result list

# # Print the final list of common elements (intersection)
# print(result)


#or


# # Using set intersection to find common elements in two lists
# nums1 = [4, 9, 5, 8]
# nums2 = [9, 4, 9, 8, 4, 5]
# result = list(set(nums1) & set(nums2))
# print(result)
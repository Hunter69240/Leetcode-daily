nums = [1,2,1,0,4,2,6]
k = 3

#Not that efficient but works
# res=[]
# i=0
# j=i+k
# while j <= len(nums):
#     res.append(max(nums[i:j]))
#     i += 1
#     j += 1
# print(res)

import collections

output = []         # List to store the maximum of each window
l = r = 0           # Left and right pointers to track the current window
q = collections.deque()  # Deque to store indices of elements in decreasing order

# Loop until the right pointer reaches the end of the list
while r < len(nums):
    
    # Maintain a decreasing deque:
    # Remove elements from the back if they are smaller than current element
    while q and nums[q[-1]] < nums[r]:
        q.pop()

    # Append the index of the current element to the deque
    q.append(r)

    # Remove the index at the front if it’s outside the current window
    if l > q[0]:
        q.popleft()

    # Once we’ve hit a full window of size k
    if (r + 1) >= k:
        # The front of the deque is the index of the max in current window
        output.append(nums[q[0]])
        # Slide the window to the right by incrementing left pointer
        l += 1

    # Always move the right pointer
    r += 1

# Print the list of maximums for each window
print(output)

    
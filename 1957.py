# s = "leeetcode"  # Step 1: Input string. We need to remove extra consecutive characters (no more than 2 same letters in a row)

# res = ""         # Step 2: Initialize empty result string that will store the cleaned-up version of 's'

# for i in s:      # Step 3: Loop over each character in the input string
#     # Step 4: Check if the last two characters in 'res' are equal to the current character 'i'
#     # If so, skip adding 'i' to avoid having 3 same letters in a row
#     if len(res) >= 2 and res[-1] == res[-2] == i:
#         continue
#     # Step 5: Safe to add character, append it to result
#     res += i

# print(res)       # Step 6: Print the final "fancy" string


#sliding window
s = "leeetcode"

res=[]
count=0
prev=""
for i in s:
    if(i==prev):
        count+=1
    else:
        count=1
    if(count<3):
        res.append(i)
    prev=i
print("".join(res))  


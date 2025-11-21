# Set the time: 1 hour and 0 minutes
hh = 1
mm = 0

# Convert time to total minutes from 12:00
t = (hh*60) + mm  # t = 60 minutes

# Cross multiplication logic:
# In 720 minutes (12 hours) → hands meet 11 times
# In t minutes → hands meet (t×11)/720 times
# Add 1 for the initial meeting at 12:00
count = (t*11)/720 + 1

# Print how many complete meetings have occurred by this time
print(int(count))  # Output: 1 (meaning 1 meeting has happened - at 12:00)

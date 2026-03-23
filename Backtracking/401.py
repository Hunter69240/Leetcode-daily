# Problem: Binary Watch — given k LEDs turned on, return all valid times
# Approach: Backtracking over 10 LEDs (indices 0–9), binary choice at each
#   — turn ON → adds its bit value to hours or minutes
#   — turn OFF → moves to next LED unchanged
# State: (idx, rem, hours, minutes)
# Base case: rem==0 → all required LEDs placed, record time if valid
# Pruning: hours>=12 or minutes>=60 → invalid, stop early
#          idx==10 → no LEDs left, rem still >0, dead end

# DRY RUN for turnedOn=1:
# backtrack(0, 1, 0, 0)
#   hours<12, mins<60 → ok | rem!=0 | idx!=10
#   CHOICE ON:  idx<4 → backtrack(1, 0, 0+8, 0)  → hours=8, rem=0 → "8:00" added
#   CHOICE OFF:         backtrack(1, 1, 0,   0)
#     CHOICE ON:  idx<4 → backtrack(2, 0, 0+4, 0) → hours=4, rem=0 → "4:00" added
#     CHOICE OFF:        backtrack(2, 1, 0,   0)
#       ... continues until all 10 LEDs tried ...
#       idx=4 (minute LEDs now):
#       CHOICE ON: idx>=4 → backtrack(5, 0, 0, 0+32) → minutes=32 → "0:32" added
#       ... and so on until "0:01" at idx=9
# Final result: ['8:00','4:00','2:00','1:00','0:32','0:16','0:08','0:04','0:02','0:01']

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        # hour LEDs:   index 0→bit8, 1→bit4, 2→bit2, 3→bit1
        # minute LEDs: index 4→bit32, 5→bit16, 6→bit8, 7→bit4, 8→bit2, 9→bit1
        hour_bits   = [8, 4, 2, 1]
        minute_bits = [32, 16, 8, 4, 2, 1]

        def backtrack(idx, rem, hours, minutes):

            # PRUNING 1: time already invalid, no point going deeper
            if hours >= 12 or minutes >= 60:
                return

            # BASE CASE: used up exactly rem LEDs, time is valid → record it
            # must come before idx==10 check — both can be true simultaneously
            if rem == 0:
                result.append(f"{hours}:{minutes:02d}")  # :02d → leading zero for minutes
                return

            # PRUNING 2: exhausted all 10 LEDs but rem still > 0 → dead end
            if idx == 10:
                return

            # CHOICE 1: turn LED idx ON → add its bit value to hours or minutes
            if idx < 4:  # indices 0–3 are hour LEDs
                backtrack(idx + 1, rem - 1, hours + hour_bits[idx], minutes)
            else:        # indices 4–9 are minute LEDs, offset by 4
                backtrack(idx + 1, rem - 1, hours, minutes + minute_bits[idx - 4])

            # CHOICE 2: leave LED idx OFF → move forward, nothing changes
            backtrack(idx + 1, rem, hours, minutes)

        backtrack(0, turnedOn, 0, 0)  # start at LED 0, rem=turnedOn, hours=0, minutes=0
        return result
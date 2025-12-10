# Goal: find the extra character in t compared to s.
# We will use XOR, which cancels out matching characters.

s = "abcd"
t = "abcde"

res = 0
# We start with 0 because XOR with 0 returns the number itself.
# (0 ^ x = x)

for c in s + t:
    # XOR the ASCII value of each character into res.
    # Matching characters cancel out because x ^ x = 0.
    # After all cancellations, only the extra character remains.
    res ^= ord(c)

# Convert final ASCII value back to a character.
print(chr(res))


"""
============================
WHY THIS WORKS (EXPLANATION)
============================

1) Each letter is stored as a number using ASCII.
   Example:
       'a' -> 97
       'b' -> 98
       'c' -> 99
       'd' -> 100
       'e' -> 101

2) XOR properties make this trick possible:
   - x ^ x = 0       (a value cancels itself)
   - x ^ 0 = x       (XOR with 0 keeps the value)
   - Order does NOT matter: a ^ b = b ^ a

3) s and t contain all the same characters EXCEPT one extra in t.
   All matching characters appear *twice* → they cancel out.
   The extra character appears once → it stays.

This is why XOR solves the problem.


============================
DRY RUN (STEP BY STEP)
============================

s + t = "abcdabcde"

Start:
    res = 0

Step 1: c = 'a' (97)
    res = 0 ^ 97 = 97

Step 2: c = 'b' (98)
    res = 97 ^ 98 = 3

Step 3: c = 'c' (99)
    res = 3 ^ 99 = 96

Step 4: c = 'd' (100)
    res = 96 ^ 100 = 4

Step 5: c = 'a' (97)
    res = 4 ^ 97 = 101

Step 6: c = 'b' (98)
    res = 101 ^ 98 = 7

Step 7: c = 'c' (99)
    res = 7 ^ 99 = 100

Step 8: c = 'd' (100)
    res = 100 ^ 100 = 0   <-- both 'd's cancel out

Step 9: c = 'e' (101)
    res = 0 ^ 101 = 101   <-- only 'e' remains


Final:
    chr(101) → 'e'


============================
SUMMARY
============================

- XOR cancels matching characters.
- All characters in s appear twice (once in s, once in t) → they vanish.
- Only the extra character from t remains.
- This works regardless of the character’s *position*.

"""

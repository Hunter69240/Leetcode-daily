# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """

#         # Define 32-bit integer limits (for overflow handling)
#         max_value = 2147483647
#         min_value = -2147483648

#         # Track sign; start with False (positive)
#         sign = False

#         # The result quotient (starts from 0)
#         quotient = 0

#         # Normalize divisor to positive and register sign if negative
#         if divisor < 0:
#             divisor = -divisor
#             sign = True

#         # Normalize dividend to positive and adjust sign flag if dividend is negative
#         if dividend < 0:
#             dividend = -dividend
#             sign = not sign

#         # Main division loop: repeatedly find the largest shifted divisor
#         while dividend >= divisor:
#             # Start search for maximum shift
#             i = 1
#             # Increase shift until (divisor << i) exceeds dividend
#             while (divisor << i) <= dividend:
#                 i += 1
#             # Subtract the largest found shifted divisor from dividend
#             dividend = dividend - (divisor << (i-1))
#             # Add corresponding multiplier (power of two) to quotient
#             quotient += (1 << (i-1))

#         # Adjust sign of result if needed
#         if sign:
#             quotient = -quotient

#         # Clamp result within 32-bit integer range
#         if quotient > max_value:
#             quotient = max_value
#         elif quotient < min_value:
#             quotient = min_value

#         # Return the computed quotient
#         return quotient



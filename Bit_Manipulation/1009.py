class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        # Edge case:
        # If n = 0 → binary = "0"
        # Complement → "1"
        # So answer = 1
        if n == 0:
            return 1
        
        # n.bit_length() gives number of bits required to represent n in binary
        # Example:
        # n = 5 → binary = 101 → bit_length = 3
        
        # (1 << n.bit_length()) shifts 1 left by bit_length
        # Example:
        # 1 << 3 → 1000 (8 in decimal)
        
        # Subtract 1 to get mask of all 1s of same length
        # 1000 - 1 → 111
        mask = (1 << n.bit_length()) - 1
        
        # XOR with mask flips the bits
        # Example:
        # n     = 101
        # mask  = 111
        # XOR   = 010 → 2
        return n ^ mask
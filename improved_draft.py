# Function to find repeated 10-letter DNA sequences
def findRepeatedDnaSequences(s):
    # Set to store sequences we have seen so far
    seen = set()
    
    # Set to store sequences that repeat
    repeated = set()
    
    # Loop through the string with a sliding window of length 10
    for i in range(len(s) - 9):  # -9 ensures the last window has 10 letters
        sequence = s[i:i+10]      # Extract substring of length 10
        
        if sequence in seen:
            # If we have seen this sequence before, it's repeated
            repeated.add(sequence)
        else:
            # If we see it for the first time, add to seen
            seen.add(sequence)
    
    # Convert the set of repeated sequences to a list and return
    return list(repeated)

# -------------------------------
# Example Test Cases
# -------------------------------

# Example 1
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print("Input:", s1)
print("Repeated sequences:", findRepeatedDnaSequences(s1))
print()

# Example 2
s2 = "AAAAAAAAAAAAA"
print("Input:", s2)
print("Repeated sequences:", findRepeatedDnaSequences(s2))

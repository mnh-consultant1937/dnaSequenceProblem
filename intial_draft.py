# def findRepeatedDnaSequences(s):
#   seen = set()
#   repeated = set()

#   for i in range(len(s) - 9):
#     sequence = s[i:i+10]
#     if sequence in seen:
#       repeated.add(sequence)
#     else:
#       seen.add(sequence)

#   return list(repeated)

# print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))


# Task 1.1: Loop through the string
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# for i in range(len(s) - 9):  # len(s)-9 ensures the last substring has 10 letters
#     substring = s[i:i+10]
#     print(substring)


# Step 2: Identify Repeated Substrings (Naive Way)
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# repeated = []

# for i in range(len(s) - 9):
#     substring = s[i:i+10]
#     if s.count(substring) > 1 and substring not in repeated:
#         repeated.append(substring)

# print(repeated)



# Step 3: Efficient Solution Using Sets
# Instead of counting every substring repeatedly, 
# we use sets to track seen substrings.

# Step 3.1: Initialize sets
seen = set()      # sequences we have seen
repeated = set()  # sequences that repeat

# Step 3.2: Sliding window
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

for i in range(len(s) - 9):
    sequence = s[i:i+10]
    if sequence in seen:
        repeated.add(sequence)  # add to repeated if seen before
    else:
        seen.add(sequence)      # first time seeing

# Step 3.3: Convert result to list
print(list(repeated))























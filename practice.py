# # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# for i in range(len(s) - 9):  # -9 ensures last window has 10 letters
#     substring = s[i:i+10]
#     print(substring)


# # s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# # seen = set()
# # repeated = set()

# # for i in range(len(s) - 9):
# #     sequence = s[i:i+10]
# #     if sequence in seen:
# #         repeated.add(sequence)  # it's repeated
# #     else:
# #         seen.add(sequence)      # first time seeing it

# # print(list(repeated))



# s = "ABCDEFG"
# for i in range(len(s) - 2):  # we want substrings of length 3
#     print(s[i:i+3])


# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# print(len(s))
# for i in range(len(s) - 9):
#     substring = s[i:i+10]
#     print(substring)

# How many times a short DNA pattern appears inside a 
# long DNA strand?

# dna = "AGCTCGGTA"
# pattern = "CG"
# count = 0

# for i in range(len(dna) - len(pattern) + 1):
#     match = True

#     for j in range(len(pattern)):
#         if dna[i + j] != pattern[j]:
#             match = False
#             break

#     if match:
#         count += 1

# print(f"Pattern '{pattern}' found {count} times")


# Using sliding window approach:

dna = "AGCTCGGTA"
pattern = "CG"
count = 0

window_size = len(pattern)

for i in range(len(dna) - window_size + 1):
    window = dna[i:i + window_size]   # sliding window
    
    if window == pattern:
        count += 1

print(f"Pattern '{pattern}' found {count} times")


















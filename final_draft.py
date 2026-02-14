 def get_all_sequences(s, length=10):
    """Return all possible substrings of given length."""
    sequences = []
    for i in range(len(s) - length + 1):
        sequences.append(s[i:i+length])
    return sequences


def find_repeated_sequences(s, length=10):
    """Return all repeated substrings of given length."""
    seen = set()
    repeated = set()

    for seq in get_all_sequences(s, length):
        if seq in seen:
            repeated.add(seq)
        else:
            seen.add(seq)

    return list(repeated)


def print_dna_analysis(s):
    print("Input:", s)
    print("Length of the string is:", len(s))
    print()

    all_sequences = get_all_sequences(s)
    print("All possible sequences:")
    for seq in all_sequences:
        print(seq)

    print()
    repeated = find_repeated_sequences(s)
    print("Repeated sequences:", repeated)
    print("-" * 40)




# Example 1
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print_dna_analysis(s1)

# Example 2
s2 = "AAAAAAAAAAAAA"
print_dna_analysis(s2)


# 🔹 visualize sliding window step-by-step

# 🔹 optimize with rolling hash (advanced)

# 🔹 convert this into a LeetCode-style solution

# 🔹 write unit tests





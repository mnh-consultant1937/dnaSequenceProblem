# ==========================================
# Matching Strings – Sliding Window Version
# ==========================================


# ------------------------------------------------
# Problem 1: Count substring matches (iterative)
# ------------------------------------------------
def countSubStringMatch(target, key):
    window_size = len(key)
    count = 0

    for start in range(len(target) - window_size + 1):
        if target[start:start + window_size] == key:
            count += 1

    return count


# ------------------------------------------------
# Problem 1: Count substring matches (recursive)
# ------------------------------------------------
def countSubStringMatchRecursive(target, key):
    if len(target) < len(key):
        return 0

    if target[:len(key)] == key:
        return 1 + countSubStringMatchRecursive(target[1:], key)
    else:
        return countSubStringMatchRecursive(target[1:], key)


# ------------------------------------------------
# Problem 2: Exact substring match positions
# ------------------------------------------------
def subStringMatchExact(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if target[start:start + window_size] == key:
            matches.append(start)

    return tuple(matches)


# ------------------------------------------------
# Helper: Match with ≤ 1 substitution
# ------------------------------------------------
def match_with_one_substitution(target, key, start):
    mismatches = 0

    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False

    return True


# ------------------------------------------------
# Problem 3: Substring match with ≤ 1 substitution
# ------------------------------------------------
def subStringMatchOneSub(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if match_with_one_substitution(target, key, start):
            matches.append(start)

    return tuple(matches)


# ------------------------------------------------
# Helper: Match with exactly 1 substitution
# ------------------------------------------------
def match_exactly_one_sub(target, key, start):
    mismatches = 0

    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False

    return mismatches == 1


# ------------------------------------------------
# Problem 4: Substring match with exactly 1 substitution
# ------------------------------------------------
def subStringMatchExactlyOneSub(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if match_exactly_one_sub(target, key, start):
            matches.append(start)

    return tuple(matches)


# ------------------------------------------------
# Optional Test Block
# ------------------------------------------------
if __name__ == "__main__":

    target1 = "atgacatgcacaagtatgcat"
    target2 = "atgaatgcatggatgtaaatgcag"

    key10 = "a"
    key11 = "atg"
    key12 = "atgc"
    key13 = "atgca"

    print("Problem 1 (Count - Iterative):")
    print(countSubStringMatch(target1, key12))

    print("\nProblem 1 (Count - Recursive):")
    print(countSubStringMatchRecursive(target1, key12))

    print("\nProblem 2 (Exact Matches):")
    print(subStringMatchExact(target1, key12))

    print("\nProblem 3 (≤ 1 Substitution):")
    print(subStringMatchOneSub(target1, key12))

    print("\nProblem 4 (Exactly 1 Substitution):")
    print(subStringMatchExactlyOneSub(target1, key12))

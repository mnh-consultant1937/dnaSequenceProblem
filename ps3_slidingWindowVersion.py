# ================================
# Helper: Count mismatched characters
# ================================
def mismatchCount(s1, s2):
    mismatches = 0
    for a, b in zip(s1, s2):
        if a != b:
            mismatches += 1
    return mismatches


# ------------------------------------------------
# Problem 1: Count substring matches (sliding window)
# ------------------------------------------------
def countSubStringMatch(target, key):
    count = 0
    k = len(key)

    for i in range(len(target) - k + 1):
        if target[i:i + k] == key:
            count += 1

    return count


# ------------------------------------------------
# Problem 1 (Recursive version – unchanged)
# ------------------------------------------------
def countSubStringMatchRecursive(target, key):
    index = target.find(key)

    if index == -1:
        return 0
    else:
        return 1 + countSubStringMatchRecursive(
            target[index + 1:], key
        )


# ------------------------------------------------
# Problem 2: Exact substring match positions
# ------------------------------------------------
def subStringMatchExact(target, key):
    result = ()
    k = len(key)

    for i in range(len(target) - k + 1):
        if target[i:i + k] == key:
            result += (i,)

    return result


# ------------------------------------------------
# Problem 3: ≤ 1 substitution allowed
# ------------------------------------------------
def subStringMatchOneSub(target, key):
    result = ()
    k = len(key)

    for i in range(len(target) - k + 1):
        window = target[i:i + k]
        if mismatchCount(window, key) <= 1:
            result += (i,)

    return result


# ------------------------------------------------
# Problem 4: Exactly 1 substitution (no exact matches)
# ------------------------------------------------
def subStringMatchExactlyOneSub(target, key):
    result = ()
    k = len(key)

    for i in range(len(target) - k + 1):
        window = target[i:i + k]
        if mismatchCount(window, key) == 1:
            result += (i,)

    return result


# ------------------------------------------------
# Optional test block
# ------------------------------------------------
if __name__ == "__main__":
    target1 = "atgacatgcacaagtatgcat"
    target2 = "atgaatgcatggatgtaaatgcag"

    key10 = "a"
    key11 = "atg"
    key12 = "atgc"
    key13 = "atgca"

    print("Problem 1:")
    print(countSubStringMatch(target1, key12))
    print(countSubStringMatchRecursive(target1, key12))

    print("\nProblem 2:")
    print(subStringMatchExact(target1, key12))

    print("\nProblem 3 (≤1 substitution):")
    print(subStringMatchOneSub(target1, key12))

    print("\nProblem 4 (exactly 1 substitution):")
    print(subStringMatchExactlyOneSub(target1, key12))

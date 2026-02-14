# ================================
# Matching Strings – All Problems
# ================================

from string import *


# ------------------------------------------------
# Problem 1: Count substring matches (iterative)
# ------------------------------------------------
def countSubStringMatch(target, key):
    count = 0
    start = 0

    while True:
        index = target.find(key, start)
        if index == -1:
            break
        count += 1
        start = index + 1  # allow overlapping matches

    return count


# ------------------------------------------------
# Problem 1: Count substring matches (recursive)
# ------------------------------------------------
def countSubStringMatchRecursive(target, key):
    index = target.find(key)

    if index == -1:
        return 0
    else:
        # search the rest of the string after the first match
        return 1 + countSubStringMatchRecursive(
            target[index + 1:], key
        )

def countSubStringMatch_loop(target, key):
    count = 0
    for start in range(len(target) - len(key) + 1):
        if is_match_at(target, key, start):
            count += 1
    return count


# ------------------------------------------------
# Problem 2: Exact substring match positions
# ------------------------------------------------
def subStringMatchExact(target, key):
    result = ()
    start = 0

    while True:
        index = target.find(key, start)
        if index == -1:
            break
        result += (index,)
        start = index + 1

    return result

def subStringMatchExact_loop(target, key):
    result = ()
    for start in range(len(target) - len(key) + 1):
        if is_match_at(target, key, start):
            result += (start,)
    return result


# ------------------------------------------------
# Problem 3: Constrained match pair (one substitution)
# ------------------------------------------------
def constrainedMatchPair(firstMatch, secondMatch, length):
    result = ()

    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                result += (n,)

    return result


# ------------------------------------------------
# Helper function provided in the assignment logic
# (uses constrainedMatchPair)
# ------------------------------------------------
def subStringMatchOneSub(target, key):
    allMatches = ()

    for miss in range(len(key)):
        key1 = key[:miss]
        key2 = key[miss + 1:]

        matches1 = subStringMatchExact(target, key1)
        matches2 = subStringMatchExact(target, key2)

        filtered = constrainedMatchPair(matches1, matches2, len(key1))
        allMatches += filtered

    # remove duplicates
    return tuple(set(allMatches))

def one_substitution_match(target, key, start):
    mismatches = 0
    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False
    return mismatches == 1


# ------------------------------------------------
# Problem 4: Exactly one substitution (no exact matches)
# ------------------------------------------------
def subStringMatchExactlyOneSub(target, key):
    oneSubMatches = subStringMatchOneSub(target, key)
    exactMatches = subStringMatchExact(target, key)

    result = ()
    for match in oneSubMatches:
        if match not in exactMatches:
            result += (match,)

    return result

def subStringMatchExactlyOneSub_loop(target, key):
    result = ()
    for start in range(len(target) - len(key) + 1):
        if one_substitution_match(target, key, start):
            result += (start,)
    return result

# ------------------------------------------------
# Optional test block (safe to remove for submission)
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




# 🚀 Optimize or refactor







 # ==========================================
# 🧬 Mini DNA Scanner Tool
# ==========================================


# ------------------------------------------------
# Validation Function
# ------------------------------------------------
def is_valid_dna(sequence):
    allowed = {"A", "T", "G", "C"}
    
    for char in sequence:
        if char not in allowed:
            return False
    
    return True



# ------------------------------------------------
# Exact Match Counter
# ------------------------------------------------
def countSubStringMatch(target, key):
    window_size = len(key)
    count = 0

    for start in range(len(target) - window_size + 1):
        if target[start:start + window_size] == key:
            count += 1

    return count


# ------------------------------------------------
# Exact Match Positions
# ------------------------------------------------
def subStringMatchExact(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if target[start:start + window_size] == key:
            matches.append(start)

    return matches


# ------------------------------------------------
# Match with ≤ 1 substitution
# ------------------------------------------------
def match_with_one_substitution(target, key, start):
    mismatches = 0

    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False

    return True
# target = "AACCTGACATCTT"
# key = "ACAT"
# start = 6
# print(match_with_one_substitution(target, key, start))

def subStringMatchOneSub(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if match_with_one_substitution(target, key, start):
            matches.append(start)

    return matches


# ------------------------------------------------
# Match with exactly 1 substitution
# ------------------------------------------------
def match_exactly_one_sub(target, key, start):
    mismatches = 0

    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False

    return mismatches == 1


def subStringMatchExactlyOneSub(target, key):
    window_size = len(key)
    matches = []

    for start in range(len(target) - window_size + 1):
        if match_exactly_one_sub(target, key, start):
            matches.append(start)

    return matches


# ------------------------------------------------
# 🧬 CLI Interface
# ------------------------------------------------
def show_menu():
    print("1 - Count Exact Matches")
    print("2 - Show Exact Match Positions")
    print("3 - Allow ≤ 1 Mutation")
    print("4 - Exactly 1 Mutation")

def dna_scanner():
    print("===================================")
    print("🧬 Welcome to the Mini DNA Scanner")
    print("===================================\n")

    while True:
        target = input("Enter DNA sequence: ").upper()
        key = input("Enter DNA pattern to search: ").upper()
    
        # Validate input
        if not is_valid_dna(target) or not is_valid_dna(key):
            print("\n❌ Error: DNA must contain only A, T, G, C.")
            return

        print("\nChoose scan type: 1-4")
        show_menu()
    
        choice = input("Enter option (1-4): ")
    
        print("\n🔍 Scanning...\n")
    
        if choice == "1":
            count = countSubStringMatch(target, key)
            print(f"Exact matches found: {count}")
        elif choice == "2":
            matches = subStringMatchExact(target, key)
            print(f"Exact match positions: {matches}")
    
        elif choice == "3":
            matches = subStringMatchOneSub(target, key)
            print(f"Matches with ≤ 1 mutation: {matches}")
    
        elif choice == "4":
            matches = subStringMatchExactlyOneSub(target, key)
            print(f"Matches with exactly 1 mutation: {matches}")
    
        else:
            print("❌ Invalid option selected.")
    
        print("--------------------------------------------------\n")

# ------------------------------------------------
# Run Scanner
# ------------------------------------------------
if __name__ == "__main__":
    dna_scanner()



# sample1 = "atgacatgcacaagtatgcat"
# sample2 = "atgaatgcatggatgtaaatgcag"
# pattern1 = "atg"
# pattern2 = "atgc"
# pattern3 = "atgca"

# 1️⃣ Add FASTA file reading support
# 2️⃣ Add performance timer
# 3️⃣ Add support for k mutations
# 4️⃣ Turn it into a GUI (Tkinter)***
# 5️⃣ Turn it into a web app (FastAPI + React)***
# 6️⃣ Dockerize it***










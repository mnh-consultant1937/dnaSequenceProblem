# ==========================================
# 🧬 DNA Mutation Analyzer Tool
# ==========================================

# Validation Function
def is_valid_dna(sequence):
    allowed = {"A", "T", "G", "C"}
    return all(char in allowed for char in sequence)


# -------------------------
# Sliding window functions
# -------------------------

def count_exact_matches(target, key):
    count = 0
    for i in range(len(target) - len(key) + 1):
        if target[i:i+len(key)] == key:
            count += 1
    return count

def exact_match_positions(target, key):
    matches = []
    for i in range(len(target) - len(key) + 1):
        if target[i:i+len(key)] == key:
            matches.append(i)
    return matches

def match_with_one_substitution(target, key, start):
    mismatches = 0
    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False
    return True

def matches_up_to_one_mutation(target, key):
    matches = []
    for i in range(len(target) - len(key) + 1):
        if match_with_one_substitution(target, key, i):
            matches.append(i)
    return matches

def match_exactly_one_mutation(target, key, start):
    mismatches = 0
    for i in range(len(key)):
        if target[start + i] != key[i]:
            mismatches += 1
            if mismatches > 1:
                return False
    return mismatches == 1

def matches_exactly_one_mutation(target, key):
    matches = []
    for i in range(len(target) - len(key) + 1):
        if match_exactly_one_mutation(target, key, i):
            matches.append(i)
    return matches

# -------------------------
# DNA Mutation Analyzer CLI
# -------------------------

def dna_mutation_analyzer():
    print("==============================================")
    print("🧬 Welcome to the DNA Mutation Analyzer Tool")
    print("==============================================\n")

    while True:
        # Input DNA sequence
        dna_sequence = input("Enter DNA sequence (or 'quit' to exit): ").upper()
        if dna_sequence.lower() == "quit":
            print("Exiting DNA Mutation Analyzer. Goodbye! 👋")
            break

        if not is_valid_dna(dna_sequence):
            print("❌ Error: DNA must contain only A, T, G, C.\n")
            continue

        # Inner loop for pattern scanning
        while True:
            dna_pattern = input("\nEnter DNA pattern to scan (or 'back' for new sequence, 'quit' to exit): ").upper()
            if dna_pattern.lower() == "quit":
                print("Exiting DNA Mutation Analyzer. Goodbye! 👋")
                return
            if dna_pattern.lower() == "back":
                print("\n🔄 Switching to new DNA sequence...\n")
                break
            if not is_valid_dna(dna_pattern):
                print("❌ Error: DNA pattern must contain only A, T, G, C.")
                continue

            # Scan options
            print("\nChoose analysis type:")
            print("1 - Count Exact Matches")
            print("2 - Show Exact Match Positions")
            print("3 - Show Matches with ≤ 1 Mutation")
            print("4 - Show Matches with Exactly 1 Mutation")
            print("5 - Show Full Mutation Report")
            print("6 - Enter new DNA sequence")
            print("7 - Quit")

            choice = input("Enter option (1-7): ").strip()

            if choice == "1":
                count = count_exact_matches(dna_sequence, dna_pattern)
                print(f"\nExact matches found: {count}")

            elif choice == "2":
                positions = exact_match_positions(dna_sequence, dna_pattern)
                print(f"\nExact match positions: {positions}")

            elif choice == "3":
                positions = matches_up_to_one_mutation(dna_sequence, dna_pattern)
                print(f"\nMatches with ≤1 mutation: {positions}")

            elif choice == "4":
                positions = matches_exactly_one_mutation(dna_sequence, dna_pattern)
                print(f"\nMatches with exactly 1 mutation: {positions}")

            elif choice == "5":
                exact = exact_match_positions(dna_sequence, dna_pattern)
                up_to_one = matches_up_to_one_mutation(dna_sequence, dna_pattern)
                exactly_one = matches_exactly_one_mutation(dna_sequence, dna_pattern)

                print("\n📊 DNA Mutation Analysis Report")
                print(f"DNA Sequence Length: {len(dna_sequence)}")
                print(f"Pattern: {dna_pattern}")
                print(f"Exact Matches ({len(exact)}): {exact}")
                print(f"Matches with ≤1 Mutation ({len(up_to_one)}): {up_to_one}")
                print(f"Matches with Exactly 1 Mutation ({len(exactly_one)}): {exactly_one}")

            elif choice == "6":
                print("\n🔄 Switching to new DNA sequence...\n")
                break

            elif choice == "7":
                print("Exiting DNA Mutation Analyzer. Goodbye! 👋")
                return

            else:
                print("❌ Invalid option selected.")

            print("--------------------------------------------------")

# -------------------------
# Run the Analyzer
# -------------------------
if __name__ == "__main__":
    dna_mutation_analyzer()

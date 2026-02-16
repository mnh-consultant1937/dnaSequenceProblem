# ==========================================
# 🧬 Mini DNA Scanner Tool - GUI Version
# ==========================================
import customtkinter as ctk
from tkinter import messagebox

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
# GUI Callback
# ------------------------------------------------
def scan_dna():
    target = entry_target.get().upper()
    key = entry_key.get().upper()
    choice = scan_type.get()

    # Validate input
    if not is_valid_dna(target) or not is_valid_dna(key):
        messagebox.showerror("Invalid Input", "DNA must contain only A, T, G, C")
        return

    # Perform scan
    if choice == "1":
        count = countSubStringMatch(target, key)
        result_text.set(f"Exact matches found: {count}")
    elif choice == "2":
        matches = subStringMatchExact(target, key)
        result_text.set(f"Exact match positions: {matches}")
    elif choice == "3":
        matches = subStringMatchOneSub(target, key)
        result_text.set(f"Matches with ≤ 1 mutation: {matches}")
    elif choice == "4":
        matches = subStringMatchExactlyOneSub(target, key)
        result_text.set(f"Matches with exactly 1 mutation: {matches}")
    else:
        result_text.set("❌ Invalid option selected.")

# ------------------------------------------------
# GUI Setup
# ------------------------------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Mini DNA Scanner")
app.geometry("500x400")

# Title
label_title = ctk.CTkLabel(app, text="🧬 Mini DNA Scanner", font=ctk.CTkFont(size=20, weight="bold"))
label_title.pack(pady=20)

# DNA Sequence Entry
label_target = ctk.CTkLabel(app, text="Enter DNA Sequence:")
label_target.pack(pady=(10, 0))
entry_target = ctk.CTkEntry(app, width=300)
entry_target.pack(pady=5)

# DNA Pattern Entry
label_key = ctk.CTkLabel(app, text="Enter DNA Pattern to Search:")
label_key.pack(pady=(10, 0))
entry_key = ctk.CTkEntry(app, width=300)
entry_key.pack(pady=5)

# Scan Type Radio Buttons
scan_type = ctk.StringVar(value="1")
frame_options = ctk.CTkFrame(app)
frame_options.pack(pady=20)

ctk.CTkLabel(frame_options, text="Select Scan Type:").pack(pady=(0,5))
ctk.CTkRadioButton(frame_options, text="1 - Count Exact Matches", variable=scan_type, value="1").pack(anchor="w", padx=20)
ctk.CTkRadioButton(frame_options, text="2 - Show Exact Match Positions", variable=scan_type, value="2").pack(anchor="w", padx=20)
ctk.CTkRadioButton(frame_options, text="3 - Allow ≤ 1 Mutation", variable=scan_type, value="3").pack(anchor="w", padx=20)
ctk.CTkRadioButton(frame_options, text="4 - Exactly 1 Mutation", variable=scan_type, value="4").pack(anchor="w", padx=20)

# Scan Button
btn_scan = ctk.CTkButton(app, text="🔍 Scan DNA", command=scan_dna)
btn_scan.pack(pady=20)

# Result Display
result_text = ctk.StringVar()
label_result = ctk.CTkLabel(app, textvariable=result_text, font=ctk.CTkFont(size=14))
label_result.pack(pady=10)

# Run App
app.mainloop()

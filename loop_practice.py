# fruits = ["apple", "banana", "mango"]

# for fruit in fruits:
#   print(fruit)



# dna = 'ACGT'
# for nucleotide in dna:
#   print(nucleotide)


# dna = 'AAGTCATA'
# count = 0
# for nucleotide in dna:
#   if nucleotide == 'A':
#     count += 1
# print(f'Total count of A: {count}')


# dna = 'AGCTCGGTA'
# for i in range(len(dna)):
#   print(i, dna[i])


# for i in range(1, 19):
#   print(i)



# fruits = ["apple", "banana", "mango"]
# for i in range(len(fruits)):
#   print(i, fruits[i])

# for index, fruit in enumerate(fruits, start=1):
#   print(index, fruit)



# dna = 'ACGTAC'

# for index, nucleotide in enumerate(dna):
#   print('Position', index, '→', nucleotide)



# greet = 'HELLO'
# for ch in greet:
#   print(ch)

# for i in range(3):
#   for j in range(2):
#     print(i, j)


# for row in range(3):
#   for col in range(4):
#     print('*', end=' ')
#   print()


# colors = ["red", "blue"]
# shapes = ["circle", "square"]
# for color in colors:
#   for shape in shapes:
#     print(color, shape)


# dna = 'ACG'
# for i in dna:
#   for j in dna:
#     print(i, j)

# dna = "ACGT"
# for i, n1 in enumerate(dna):
#     for j, n2 in enumerate(dna):
#         print(i, n1, "vs", j, n2)



# target = "GATAT"
# key = "AT"
# count = 0
# for i in range(len(target)):
#     match = True

#     for j in range(len(key)):
#         if i + j >= len(target) or target[i + j] != key[j]:         
#             match = False
#             break

#     if match:
#         print("Match at index", i)
#           count += 1
# print(f"Pattern '{pattern}' found {count} times")


# 09/02/2026

# dna = "AGCTCGGTA"
# count = 0
# for nucletide in dna:
#   if nucletide == 'G' or nucletide == 'C':
#     count += 1
# print(f'Total GC count: {count}')


# dna = "AGCTCGGTA"
# count = 0
# for i in range(len(dna) - 1):
#     if dna[i] == 'G' and dna[i + 1] == 'C':
#         count += 1
# print("GC pairs:", count)


# dna = "AGCTCGGTA"
# count = 0
# for i in range(len(dna) - 1):
#     pair = dna[i:i+2]
#     if pair == "GC":
#         count += 1
# print("GC pairs:", count)

# dna = "AGCTCGGTA"
# print("GC pairs:", dna.count("GC"))


# dna = "AGCTCGGTA"
# for i in range(len(dna)):
#     print(i, dna[i])


# We want to count how many times a short DNA pattern 
# appears inside a long DNA strand.
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


# dna = "AGCTCGGTA"
# pattern = "CG"
# count = 0
# for i in range(len(dna) - len(pattern) + 1):
#     if dna[i:i+len(pattern)] == pattern:
#         count += 1
# print(f"Pattern '{pattern}' found {count} times")


# dna = "AGCTCGGTA"
# pattern = "CG"
# count = dna.count(pattern)
# print(f"Pattern '{pattern}' found {count} times")


# def count_pattern(dna, pattern):
#     count = 0
#     for i in range(len(dna) - len(pattern) + 1):
#         if dna[i:i+len(pattern)] == pattern:
#             count += 1
#     return count
# dna = "AGCTCGGTA"
# pattern = "CG"
# print(f"Pattern '{pattern}' found {count_pattern(dna, pattern)} times")      



# ⚡ Optimize this algorithm (time complexity)

# 🧪 DNA GC-content & mutation detection

# 🧠 Interview-style string problems

# 🔁 Rewrite everything using while loops only

# 🧩 Turn this into a mini Python project

# time complexity analysis


string = 'DNA'
for index, ch in enumerate(string):
  print(index, ch)































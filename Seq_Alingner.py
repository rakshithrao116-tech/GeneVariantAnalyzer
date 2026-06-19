seq1 = input("Enter the first DNA sequence: ").upper().strip()
seq2 = input("Enter the second DNA sequence: ").upper().strip()

alignment = ""
matches = 0
mismatches = 0
score = 0

mutation = []
coserved_regions = []

current_coserved = ""

min_length = min(len(seq1), len(seq2))


transition = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

for i in range(min_length):
    if seq1[i] == seq2[i]:
        alignment += "|"
        matches += 1
        score += 1

        current_coserved += seq1[i]

    else:
        alignment +=""
        mismatches += 1
        score -= 1

        if len(current_coserved) >= 2:
            coserved_regions.append(current_coserved)

        current_coserved = ""

        old = seq1[i]
        new = seq2[i]

        if (old,new) in transition:
            mutation_type = "Transition"
        else:
            mutation_type = "Transversion"


        mutation.append(
            (i+1,old,new,mutation_type)

        )

    
if len (current_coserved) >= 2:
    coserved_regions.append(current_coserved)


print("\n -----Alignment-----")

print(seq1)
print(alignment)    
print(seq2)


print("\n -----Statistics-----")

print(f"Matches : {matches}")
print(f"Mismatches : {mismatches}")


similarity = (matches / min_length) * 100

print(f"Similarity : {similarity:.2f}%")
print(f"Alignment Score : {score}")


print("\n -----Mutations Analysis-----")


if len(mutation) == 0:
    print("No mutations found.")
else:
    for pos, old, new, mutation_type in mutation:
        print(f"Position {pos}: {old} -> {new} ({mutation_type})")


print("\n -----Conserved Regions-----")

if coserved_regions:
    for region in coserved_regions:
        print(region)
else:
    print("No conserved regions found.")



print("\n ----- Hotspot Analysis-----")

mutation_counts = (
    len(mutation)/min_length
)* 100

print(f"Total Mutations : {len(mutation)}")
print(f"Mutation Density : {mutation_counts:.2f}%")


if mutation_counts > 30:
    print("High Mutation Region Detected")
elif mutation_counts > 10:
    print("Moderate Mutation Region Detected")
else:
    print("Low Mutation Region Detected")
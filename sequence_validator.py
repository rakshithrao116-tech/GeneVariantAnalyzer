def validate_dna(sequence):
    sequence = sequence.upper().strip()

    valid_nucleotides = {"A", "T", "C", "G"}
    invalid_nucleotides = []

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            invalid_nucleotides.append(nucleotide)
    return len(invalid_nucleotides) == 0, invalid_nucleotides

dna_sequence = input("Enter a DNA sequence: ")

valid, invalid_nucleotides = validate_dna(dna_sequence)
if len(invalid_nucleotides) == 0:
    print("The DNA sequence is valid.")
else:
    print(f"The DNA sequence is invalid.")
    print(f"Invalid character:",",".join(sorted(set(invalid_nucleotides ))))

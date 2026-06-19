genetic_code = {
    "TTT":"Phe","TTC":"Phe",
    "TTA":"Leu","TTG":"Leu","CTT":"Leu","CTC":"Leu","CTA":"Leu","CTG":"Leu",
    "ATT":"Ile","ATC":"Ile","ATA":"Ile",
    "ATG":"Met",
    "GTT":"Val","GTC":"Val","GTA":"Val","GTG":"Val",
    "TCT":"Ser","TCC":"Ser","TCA":"Ser","TCG":"Ser","AGT":"Ser","AGC":"Ser",
    "CCT":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro",
    "ACT":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr",
    "GCT":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala",
    "TAT":"Tyr","TAC":"Tyr",
    "CAT":"His","CAC":"His",
    "CAA":"Gln","CAG":"Gln",
    "AAT":"Asn","AAC":"Asn",
    "AAA":"Lys","AAG":"Lys",
    "GAT":"Asp","GAC":"Asp",
    "GAA":"Glu","GAG":"Glu",
    "TGT":"Cys","TGC":"Cys",
    "TGG":"Trp",
    "CGT":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg","AGA":"Arg","AGG":"Arg",
    "GGT":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly",
    "TAA":"STOP","TAG":"STOP","TGA":"STOP"
}

dna = input("Enter a DNA sequence: ").upper().strip()
motif = input("Enter a motif to search for: ").upper().strip()


print("\n -----ORF Finder----- ")

orf_count = 0
for i in range(len(dna) - 2):
    codon = dna[i:i+3]
    if codon == "ATG":
        protein = []
        for j in range(i,len(dna)-2,3):
            current_codon = dna[j:j+3]
            if current_codon not in genetic_code:
                break
            amino_acid = genetic_code[current_codon]
            if amino_acid == "STOP":

                orf_count += 1
                print(f"\nORF{orf_count}")
                print("Start Position:", i+1)
                print(f"Stop Position:{j+3}")
                print("Protein:", "".join(protein))

                break

            protein.append(amino_acid)


if orf_count == 0:
    print("No ORFs found.")

print("\n -----Motif Finder----- ")

positions = []

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i+len(motif)] == motif:
        positions.append(i + 1)


if positions:
    print(f"Motif'{motif}'Found")

    for pos in positions:
        print(f"Position: {pos}")
else:
    print("Motif not found.")
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

amino_acid_weight = {
    "Ala":89.09,"Arg":174.20,"Asn":132.12,"Asp":133.10,
    "Cys":121.15,"Gln":146.15,"Glu":147.13,"Gly":75.07,
    "His":155.16,"Ile":131.17,"Leu":131.17,"Lys":146.19,
    "Met":149.21,"Phe":165.19,"Pro":115.13,"Ser":105.09,
    "Thr":119.12,"Trp":204.23,"Tyr":181.19,"Val":117.15
}

dna = input("Enter a DNA sequence: ").upper().strip()

start = dna.find("ATG")

if start == -1:
    print("No start codon found.")
else:
    print(f"Start codon found at position: {start+1}")


print("\n -----Reading Frames -----" )

for frame in range(3):
    print(f"Frame{frame+1}:", end=" ")


    for i in range(frame, len(dna)-2, 3):
        print(dna[i:i+3], end=" ")

    print()


print("\n -----Protein Translation -----")

protein =[]

for i in range(start,len(dna)-2,3):

    codon = dna [i:i+3]

    if codon in genetic_code:
        amino_acid = genetic_code[codon]

        print(f"{codon} -> {amino_acid}")

        if amino_acid == "STOP":
            print("Stop codon reached. Translation terminated.")
            break

        protein.append(amino_acid)

protein_sequence = "-".join(protein)

print("\nProtein Sequence:")
print(protein_sequence)


print("\n -----Amino Acid Composition -----")

composition = {}

for amino_acid in protein:
    composition[amino_acid] = composition.get(amino_acid, 0) + 1

for amino_acid, count in composition.items():
    print(f"{amino_acid}: {count}")



print(f"\nProtein Length: {len(protein)} amino acids")



mw = 0

for amino_acid in protein:
    mw += amino_acid_weight.get(amino_acid, 0)

print(f"Protein Molecular Weight: {mw:.2f} Da")
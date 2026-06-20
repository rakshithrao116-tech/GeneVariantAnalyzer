dna = input("Enter the DNA sequence: ").upper().strip()

primer_length = int(input("Enter the desired primer length(20-30 recommended): "))


forward_primer = dna[:primer_length]

def reverse_complement(seq):

    complement ={
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    

    rev_comp = ""

    for base in reversed(seq):
        rev_comp += complement[base]

    return rev_comp




reverse_primer = reverse_complement(
    dna[-primer_length:])


def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100



def melting_temp(seq):

    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")

    return 2 * (a + t) + 4 * (g + c)



restriction_sites = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "XhoI": "CTCGAG",
    "NotI": "GCGGCCGC"
}



def primer_score(seq):
    score = 100

    gc = gc_content(seq)
    if gc< 40 or gc > 60:
        score -= 20
    melting_temp_value = melting_temp(seq)
    if melting_temp_value < 50 or melting_temp_value > 65:
        score -= 20
    
    if seq[-1] in ["G", "C"]:
        score -= 10

        return score
    


print("\n -----Primer Design Report-----")

print("\nForward Primer:")
print(forward_primer)

print("\nReverse Primer:")
print(reverse_primer)


print("\n-----Forward Primer Stats-----:")

print(f"Length: {len(forward_primer)}")
print(f"GC Content: {gc_content(forward_primer):.2f}%")
print(f"Melting Temperature: {melting_temp(forward_primer)}°C")
print(f"Quality Score: {primer_score(forward_primer)}")

print("\n-----Reverse Primer Stats-----:")

print(f"Length: {len(reverse_primer)}")
print(f"GC Content: {gc_content(reverse_primer):.2f}%")
print(f"Melting Temperature: {melting_temp(reverse_primer)}°C")
print(f"Quality Score: {primer_score(reverse_primer)}")


print("\n-----Restriction Sites Analysis-----:")

found = False

for enzyme, site in restriction_sites.items():
    if site in dna:
        print(f"{enzyme} Site Found")
        print(f"Recognition Sequence: {site}")
        print(f"Position: {dna.find(site)+1}\n")

        found = True

if not found:
    print("No Restriction Sites Found")
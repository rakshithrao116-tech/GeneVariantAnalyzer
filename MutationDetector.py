from Bio import SeqIO

reference_file = input("Enter your reference FASTA file name: ")
sample_file = input("Enter your sample FASTA file name: ")

ref_record = SeqIO.read(reference_file, "fasta")
sample_record = SeqIO.read(sample_file, "fasta")

reference = str(ref_record.seq)
sample = str(sample_record.seq)

mutations = []

for i in range(min(len(reference),len(sample))):
    if reference[i] != sample[i]:
        mutations.append({
            "position": i + 1,
            "reference": reference[i],
            "sample": sample[i]
        })

if len(mutations) == 0:
    print("\nNo mutations found.")
else:
    print("\nMutations detected:")
    for mutation in mutations:
        print(f"Position : {mutation['position']}")
        print(f"Reference : {mutation['reference']}")
        print(f"Sample : {mutation['sample']}")
        print("-" * 20)
print(f"\nTotal mutations detected: {len(mutations)}")
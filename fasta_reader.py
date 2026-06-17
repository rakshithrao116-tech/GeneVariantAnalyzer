def read_fasta(file_path):
    header = ""
    sequence = ""

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                header = line.strip()
            else:
                sequence += line.strip()
    
    return header, sequence

file_name = input("Enter the name of the FASTA file: ")

try:
    header, sequence = read_fasta(file_name)
    print(f"\nHeader: {header}")
    print(f"Sequence: {sequence}")
except FileNotFoundError:
    print("File not found.")
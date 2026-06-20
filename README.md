# 🧬 BioSeqToolkit

An integrated bioinformatics toolkit for DNA sequence analysis, mutation detection, protein translation, ORF discovery, sequence alignment, and PCR primer design.


## About

BioSeqToolkit grew out of a simple mutation-detection script into a small collection of bioinformatics utilities covering the most common early-stage DNA analysis tasks: reading FASTA files, validating sequences, comparing them for mutations, finding genes (ORFs), translating DNA to protein, and designing PCR primers.

Each tool is intentionally simple and dependency-light, making it easy to read, learn from, and extend.

## Features

| Tool | Description |
|---|---|
| 🧪 **Mutation Detector** | Compares a reference and sample FASTA file, reports every nucleotide mismatch by position |
| 🔗 **Sequence Aligner** | Aligns two raw sequences; reports % similarity, transition/transversion calls, conserved regions, and mutation hotspots |
| 🔍 **ORF & Motif Finder** | Detects open reading frames (ATG → stop codon) and locates a search motif within a sequence |
| 🧫 **Protein Translator** | Translates DNA into protein starting at the first ATG; reports amino acid composition and molecular weight |
| 🧷 **Primer Designer** | Generates forward/reverse PCR primers with GC%, melting temperature, a quality score, and restriction site detection |
| 📄 **FASTA Reader** | Parses single- or multi-record FASTA files into headers and sequences |
| ✅ **Sequence Validator** | Confirms a sequence contains only valid A/T/C/G nucleotides |

## Tech Stack

- **Language:** Python 3.8+
- **Dependency:** [Biopython](https://biopython.org/) (used only by `MutationDetector.py`)
- Everything else relies solely on the Python standard library — nothing else to install.

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/rakshithrao116-tech/BioSeqToolkit.git

# 2. Move into the project folder
cd BioSeqToolkit

# 3. Install the one external dependency
pip install biopython
```

That's it — no virtual environment or build step required.

## Usage

Run any script directly with Python. Each one prompts you for input interactively, so there are no flags to memorize.

```bash
python MutationDetector.py
python Sequence_Alingner.py
python ORF_And_Motif_Finder.py
python protein_translator.py
python PrimerDesigner.py
python fasta_reader.py
python sequence_validator.py
```

## Example Run

```bash
$ python protein_translator.py
Enter a DNA sequence: ATGAAATAG
Start codon found at position: 1

 -----Reading Frames -----
Frame1: ATG AAA TAG
Frame2: TGA AAT
Frame3: GAA ATA

 -----Protein Translation -----
ATG -> Met
AAA -> Lys
TAG -> STOP
Stop codon reached. Translation terminated.

Protein Sequence:
Met-Lys

 -----Amino Acid Composition -----
Met: 1
Lys: 1

Protein Length: 2 amino acids
Protein Molecular Weight: 295.40 Da
```

## Project Structure

```
BioSeqToolkit/
├── MutationDetector.py        # Reference vs. sample mutation detection
├── Sequence_Alingner.py       # Two-sequence alignment + mutation analysis
├── ORF_And_Motif_Finder.py    # ORF detection + motif search
├── protein_translator.py      # DNA -> protein translation
├── PrimerDesigner.py          # PCR primer design
├── fasta_reader.py            # FASTA file parser
├── sequence_validator.py      # Nucleotide validation
└── README.md
```

## Known Limitations

Being upfront about what this toolkit doesn't do yet:

- **No gap-aware alignment.** Sequences are compared position-by-position, so substitutions are caught reliably, but insertions/deletions that shift the reading frame are not (a true aligner like Needleman–Wunsch would be needed for that).
- **Forward strand only.** `ORF_And_Motif_Finder.py` does not scan the reverse complement.
- **No CLI flags yet.** Every script is interactive (`input()`-driven) rather than scriptable via arguments.
- **Light input validation.** Outside of `sequence_validator.py`, scripts generally expect clean uppercase A/T/C/G input.

## Roadmap

- [ ] Add a real alignment algorithm for accurate indel detection
- [ ] Add `argparse` support for non-interactive / scriptable use
- [ ] Add reverse-complement scanning to the ORF finder
- [ ] Add unit tests with `pytest`
- [ ] Merge the scripts into a single importable package with a unified CLI

## Contributing

Contributions are welcome, even as a learning project! To contribute:

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit (`git commit -m "Add: your feature"`)
5. Push to your fork and open a Pull Request

If you find a bug, opening an issue with a minimal example (the sequence/input that triggers it) is the fastest way to get it fixed.


## Author

**rakshithrao116-tech**
[GitHub Profile](https://github.com/rakshithrao116-tech)

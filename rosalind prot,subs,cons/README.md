# Day 20 – Rosalind Problems: PROT, SUBS, and CONS

## Objective
Solve three classic Rosalind problems that represent fundamental bioinformatics tasks:

- PROT – Protein Translation
- SUBS – Motif Finding
- CONS – Consensus Sequence

---

## 1. PROT – Protein Translation

### Goal
Convert an RNA sequence into a protein sequence using the genetic code.

### Biological Concept
RNA is read in groups of three nucleotides (codons), and each codon specifies an amino acid.

Example:

RNA:
```
AUGGCCUUU
```

Codons:
```
AUG GCC UUU
```

Protein:
```
MAF
```

### Applications
- Gene annotation
- Protein prediction
- Genome analysis

---

## 2. SUBS – Motif Finding

### Goal
Find all occurrences of a motif within a DNA sequence.

Example:

DNA:
```
GATATATGCATATACTT
```

Motif:
```
ATAT
```

Positions:
```
2 4 10
```

### Applications
- Identifying regulatory elements
- Detecting conserved regions
- Finding transcription factor binding sites

---

## 3. CONS – Consensus Sequence

### Goal
Determine the most common nucleotide at each position among multiple aligned sequences.

Example:

```
ATCCA
ATGCA
ATGGA
ATGCA
```

Consensus sequence:

```
ATGCA
```

### Applications
- Multiple sequence alignment
- Evolutionary studies
- Conserved region analysis

---

## Tools Used

- Python
- Biopython
- Collections.Counter

---

## Key Concepts Learned

✔ Protein translation from RNA sequences

✔ Pattern matching and motif identification

✔ Consensus sequence generation

✔ Sequence conservation analysis

---

## Bioinformatics Workflow

```
RNA Sequence
      ↓
PROT
Protein Sequence

DNA Sequence
      ↓
SUBS
Motif Positions

Multiple Sequences
      ↓
CONS
Consensus Sequence
```

---

## Files

- `prot.py` – Protein translation
- `subs.py` – Motif finding
- `cons.py` – Consensus sequence generation

---

## Outcome

Completed three Rosalind problems corresponding to real-world bioinformatics tasks involving translation, motif discovery, and sequence conservation.
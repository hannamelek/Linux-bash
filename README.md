# Week 3: Linux, Bash Basics & Sequence Analysis and Rosalind Challenges

## Topics Covered

## Day 15 — Bash Basics

- Linux Terminal
- Navigating directories (`pwd`, `cd`)
- Listing files (`ls`)
- Creating directories (`mkdir`)
- Creating files (`touch`)
- Viewing file contents (`cat`)
- Copying files (`cp`)
- Renaming/moving files (`mv`)
- Viewing file beginnings and endings (`head`, `tail`)

### Exercise
Practiced file and directory operations entirely from the terminal.

### Key Takeaway
Learned how to navigate and manage files using basic Linux commands.

---

## Day 16 — Text Processing in Linux

- Searching text with `grep`
- Counting with `wc`
- Sorting data with `sort`
- Removing duplicates with `uniq`
- Using pipes (`|`) to combine commands

### Exercise
Counted the number of sequences in a FASTA file:

```bash
grep ">" sample.fasta | wc -l
```

### Key Takeaway
Learned to filter, count, and process biological sequence data directly from the command line.

---

## Day 17 — Bash Scripting

- What Bash scripts are
- Variables in Bash
- Automating repetitive tasks
- Making scripts executable (`chmod +x`)
- Running scripts (`./script.sh`)

### Exercise
Created a script that:
- Counts sequences in a FASTA file
- Calculates GC percentage

### Key Takeaway
Learned how to automate sequence analysis tasks using Bash scripts.

---

## Day 18 – Introduction to BLAST

- What BLAST (Basic Local Alignment Search Tool) does
- Types of BLAST searches
- Running BLAST using the NCBI web interface
- Understanding BLAST output

### Activities
- Performed a BLASTp search using a sample protein sequence
- Interpreted key output metrics:
  - Max Score
  - Query Coverage
  - Percent Identity
  - E-value
- Identified the top matching protein sequence

### Key Concepts Learned
- Sequence similarity searching
- Homology detection
- Significance of E-values
- Interpreting biological matches

---

## Day 19 – BLAST with Biopython

### Topics Covered
- Automating BLAST searches using Biopython
- Using the NCBIWWW module
- Parsing BLAST XML results

### Activities
- Submitted a protein sequence programmatically
- Saved BLAST output as XML
- Parsed results using NCBIXML
- Extracted the top 5 hits and their E-values

### Key Concepts Learned
- Programmatic access to NCBI services
- Working with XML output
- Parsing biological data
- Automating sequence analysis workflows

### Tools Used
- Biopython
- NCBIWWW
- NCBIXML

---

## Day 20 – Rosalind Problems: PROT, SUBS, CONS

### PROT – Protein Translation
Converted RNA sequences into protein sequences using the genetic code.

**Concepts:**
- Codons
- Translation
- Amino acids
- Stop codons

### SUBS – Motif Finding
Identified all occurrences of a motif within a DNA sequence.

**Concepts:**
- Pattern matching
- Sequence searching
- Biological motifs

### CONS – Consensus Sequence
Generated a consensus sequence from multiple aligned DNA sequences.

**Concepts:**
- Sequence conservation
- Profile matrices
- Consensus sequences

### Key Concepts Learned
- Translation of RNA to protein
- Motif discovery
- Sequence conservation analysis
- Basic bioinformatics problem-solving
  
---

## Skills Developed

- Linux command-line navigation
- File management
- Text processing
- FASTA file handling
- Bash scripting fundamentals
- Basic bioinformatics automation
- Running and interpreting BLAST searches
- Automating analyses with Biopython
- Parsing biological datasets
- Protein translation
- Motif identification
- Consensus sequence generation
- Applying Python to real bioinformatics tasks

---

## Repository Contents

```text
|-- Day 15,16 -> Bash basics-> navigate directories, ls, cp, mv, cat, head, tail, grep, wc, sort, uniq)
|-- Day 17 -> Bash script -> simple file processing 
|-- Day18 -> ncbi blastp -> what it does, how to run it on NCBI web interface, read output
|-- Day19 -> Biopython NCBIWWW -> Ran BLAST programmatically using Biopython's NCBIWWW module
|-- Day20 -> Rosalind -> attempted PROT (protein translation), SUBS (motif finding), CONS (consensus)
```
---

## Goal

Learn the fundamentals of Linux and Bash for bioinformatics, including file navigation, text processing, and basic task automation through scripting.

---

## Purpose

- Understand how biological sequences are analyzed and compared.
- Gain hands-on experience with BLAST through both web-based and programmatic approaches.
- Apply Python and Biopython to solve common bioinformatics problems.
- Develop problem-solving skills using Rosalind challenges that mirror real-world biological analyses.

---

## Outcome

By the end of Days 18–20, I was able to:

- Run and interpret BLAST searches using the NCBI web interface.
- Perform BLAST searches programmatically using Biopython.
- Extract and analyze significant sequence matches and E-values.
- Translate RNA sequences into proteins.
- Identify motifs within DNA and protein sequences.
- Generate consensus sequences from multiple aligned sequences.
- Strengthen Python programming skills through practical bioinformatics applications.

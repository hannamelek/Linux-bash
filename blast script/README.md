# Day 17 - Bash Scripting Basics

## What is a Bash Script?

A Bash script is a text file containing Linux commands that can be executed automatically.

Instead of typing the same commands repeatedly, we can save them in a file and run them whenever needed.

---

## Commands Used

### echo
Print text to the terminal.

```bash
echo "Hello World"
```

### grep
Search for patterns in a file.

```bash
grep ">" sample.fasta
```

### wc
Count lines, words, or characters.

```bash
wc -l
```

### tr
Translate or delete characters.

```bash
tr -d '\n'
```

### chmod
Make a file executable.

```bash
chmod +x fasta_stats.sh
```

---

## Exercise

Write a Bash script that:

1. Counts the number of sequences in a FASTA file.
2. Calculates GC percentage.

---

## Sample FASTA File

sample.fasta

```text
>seq1
ATGC
>seq2
GGCC
>seq3
ATAT
```

---

## Bash Script

fasta_stats.sh

```bash
#!/bin/bash

echo "FASTA Statistics"

seq_count=$(grep ">" sample.fasta | wc -l)

echo "Number of sequences: $seq_count"

bases=$(grep -v ">" sample.fasta | tr -d '\n')

total=$(echo "$bases" | wc -c)

gc=$(echo "$bases" | grep -o "[GC]" | wc -l)

gc_percent=$((gc * 100 / total))

echo "GC Percentage: $gc_percent%"
```

---

## Run the Script

Make it executable:

```bash
chmod +x fasta_stats.sh
```

Execute:

```bash
./fasta_stats.sh
```

---

## Output

```text
FASTA Statistics
Number of sequences: 3
GC Percentage: 50%
```

---

## Concepts Learned

- What a Bash script is.
- Variables (`seq_count`, `gc`, `total`).
- Using `grep` and `wc` together.
- Using pipes (`|`).
- Making scripts executable with `chmod +x`.
- Running scripts using `./script_name`.

---

## Why is this useful?

Bioinformatics datasets often contain thousands or millions of sequences. Bash scripts allow repetitive analyses to be automated, making sequence processing faster and more reproducible.
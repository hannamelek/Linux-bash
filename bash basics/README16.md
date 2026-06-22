# Day 16 - Text Processing in Linux

## Commands Learned

### grep
Search for text patterns.

```bash
grep ">" sample.fasta
```

### wc
Count lines, words, or characters.

```bash
wc -l sample.fasta
```

### sort
Sort lines alphabetically.

```bash
sort genes.txt
```

### uniq
Remove duplicate lines.

```bash
uniq genes.txt
```

## Exercise: Count sequences in a FASTA file

Contents of sample.fasta:

```text
>seq1
ATGC
>seq2
GGAA
>seq3
TTCC
```

Count sequences:

```bash
grep ">" sample.fasta | wc -l
```

Output:

```text
3
```

There are 3 sequences in the FASTA file.
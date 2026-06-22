# Day 19 - BLAST using Biopython

## Objective
Run BLAST programmatically using Biopython's NCBIWWW module and parse results.

## Modules Used
- Bio.Blast.NCBIWWW
- Bio.Blast.NCBIXML

## Workflow
Sequence → qblast() → XML output → Parse XML → Top 5 hits

## Output
Printed the top 5 protein matches along with their E-values.
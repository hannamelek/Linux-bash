#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[5]:

#PROT+SUBS
rna = Seq("AUGGCCAUGGCCUAA")
protein = rna.translate()
print(protein)


# In[6]:


protein = "MAMA"
motif = "MA"

for i in range(len(protein)-len(motif)+1):
    if protein[i:i+len(motif)] == motif:
        print(i+1)


# In[7]:

#CONS+SUBS
from Bio.Seq import Seq


# In[8]:


seqs = [
"ATCCA",
"ATGCA",
"ATGGA",
"ATGCA"
]


# In[9]:


from collections import Counter

consensus = ""

for i in range(len(seqs[0])):
    column = [seq[i] for seq in seqs]
    counts = Counter(column)

    consensus += counts.most_common(1)[0][0]

print(consensus)


# In[10]:


dna = "ATGCA"
motif = "ATG"


# In[11]:


for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)] == motif:
        print(i+1)


# In[ ]:





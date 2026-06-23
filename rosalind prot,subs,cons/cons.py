#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[2]:


seqs = [
"ATCCA",
"ATGCA",
"ATGGA",
"ATGCA"
]


# In[3]:


from collections import Counter

consensus = ""

for i in range(len(seqs[0])):
    column = [seq[i] for seq in seqs]
    counts = Counter(column)

    consensus += counts.most_common(1)[0][0]

print(consensus)


# In[7]:


seqs = [
"GCTA",
"GCAA",
"GCCA",
"GCTA" 
]


# In[8]:


from collections import Counter

consensus = ""

for i in range(len(seqs[0])):
    column = [seq[i] for seq in seqs]
    counts = Counter(column)

    consensus += counts.most_common(1)[0][0]

print(consensus)


# In[ ]:





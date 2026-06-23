#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[2]:


dna = "GATATATGCATATACTT"
motif = "ATAT"


# In[3]:


for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)] == motif:
        print(i+1)


# In[4]:


dna = "ACGTACGTACGT"
motif = "ACG"


# In[6]:


for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)] == motif:
        print(i+1)


# In[7]:


dna = "ATATATAT"
motif = "ATA"


# In[8]:


for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)] == motif:
        print(i+1)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio.Seq import Seq


# In[2]:

#Protein translation from RNA sequence

rna = Seq("AUGGCCUUU")
protein = rna.translate()


# In[3]:


print(protein)


# In[12]:

#PROT EXAMPLE 2
rna = Seq("AUGGCCAAA")
protein = rna.translate()


# In[14]:


print(protein)


# In[15]:

#PROT EXAMPLE 3
rna = Seq("AUGGCUUAAUGG")
protein = rna.translate()


# In[16]:


print(protein)


# In[ ]:





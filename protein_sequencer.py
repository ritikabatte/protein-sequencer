import matplotlib
import Bio

# Getting the structure of human hemoglobin
from Bio import SeqIO
for hemoglobin_seq in SeqIO.parse("hemoglobin.fasta", "fasta"): 
    print(str(hemoglobin_seq))    

# Counting the amino acids in the sequence 
amino_acid_count = {}
for amino_acid in hemoglobin_seq: 
    if amino_acid in amino_acid_count: 
        amino_acid_count[amino_acid] += 1
    else: 
        amino_acid_count[amino_acid] = 1
print("Amino Acid Composition of Human Hemoglobin: ")
for amino_acid, count in amino_acid_count.items(): 
    print(f"{amino_acid}: {count}")

# Visualize 

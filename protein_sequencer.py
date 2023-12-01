import matplotlib.pyplot as plt
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
amino_acids = list(amino_acid_count.keys())
frequencies = list(amino_acid_count.values())
plt.bar(amino_acids, frequencies, width = 0.5, color = 'navy')
plt.title("Amino Acid Composition of Human Hemoglobin")
plt.xlabel("Amino Acids")
plt.ylabel("Freqeuncy")
plt.show()
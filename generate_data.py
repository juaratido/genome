import random

def generate_dna(lenght=100):
    return ''.join(random.choices(['A', 'C', 'D', 'T'], k=lenght))

#1. create a sample of fasta file
with open("sample.fasta", "w") as f:
    for i in range (1,6):
        f.write(f">sequence_{i} description_test_{i}\n")
        f. write(f"{generate_dna(random.randint(80,150))}\n")

#2. create a sample of fastq file
with open("sample.fastq", "w") as f:
    for i in range(1,6):
        seq = generate_dna(100)
        qual = ''. join(chr(random.randint(33,73)) for _ in range (100)) #phred scores as ASCII
        f.write(f"@read_{i}\n{seq}\n+\n{qual}\n")

print("created 'sample.fasta' and 'sample.fastq' successfully")
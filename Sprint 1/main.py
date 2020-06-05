AMINO_ACIDS = { 
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'} 
       
def translate(dna):    
    if len(dna) > 2 and len(dna) % 3 is not 0:
        dna = dna[0: (len(dna) // 3) * 3] #Discard extra letters from the DNA sequence
    elif len(dna) < 3:
        return
    
    return ''.join([AMINO_ACIDS[codon] if codon in AMINO_ACIDS.keys() else 'X' for codon in [dna[i:i+3] for i in range(0, len(dna), 3)]])

        
def mutate(filename = 'dna.txt'):
    normalDNA = ''
    mutatedDNA = ''
    with open(filename, 'r') as f:
        for c in ''.join(f.read().split()):
            normalDNA += c if c != 'a' else 'A'
            mutatedDNA += c if c != 'a' else 'T'
            
    with open('normalDNA.txt', 'w') as f:
        f.write(normalDNA)
        
    with open('mutatedDNA.txt', 'w') as f:
        f.write(mutatedDNA)
        
def txtTranslate():
    with open('normalDNA.txt', 'r') as f:
        print('>>> normalDNA.txt')
        print(translate(''.join(f.read().split())) + "\n\n")
        
    with open('mutatedDNA.txt', 'r') as f:
        print('>>> mutatedDNA.txt')
        print(translate(''.join(f.read().split())) + "\n\n")
  
mutate()
txttxtTranslate()

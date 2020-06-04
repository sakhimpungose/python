AMINO_ACIDS = {'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'TTA': 'L', 'TTG': 'L',
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
'TTT': 'F', 'TTC': 'F',
'ATG': 'M'}
       
def translate(dna):    
    if len(dna) > 2 and len(dna) % 3 != 0:
        dna = dna[0: (len(dna) // 3) * 3] #Discard extra letters from the DNA sequence
    elif len(dna) < 2:
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
        print(translate(''.join(f.read().split())))
        
    with open('mutatedDNA.txt', 'r') as f:
        print(translate(''.join(f.read().split())))
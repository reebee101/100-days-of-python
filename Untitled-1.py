def is_valid_sequence (dna):
    ''' (str)-> boole

    return true if and only if the dna sequence is valid
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('LTPROCKS')
    False
    '''
    for char in dna: 
     if char in ('A' ,'G' ,'T' ,'C'):
        return True
     elif char in (' ') : 
        return True
     else :
        return False
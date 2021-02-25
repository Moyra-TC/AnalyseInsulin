'''
Moyra Chikomo
Exercise 1: Retrieve the Protein Sequence of Human Preproinsulin
Exercise 2: Obtain the Protein Sequence of Human Insulin
Clean- up can also be done using:
                                import re
Feb 2021 v1.0
'''

import os

Path="C:/Users/moyra/PycharmProjects/AWS_reStartLabs"
Filename=Path+'/preproinsulin_seq.txt'
print("Filename is:" +Filename)
ainsulin=Path+'/ainsulin_seq.txt'
binsulin=Path+'/binsulin_seq.txt'
cinsulin=Path+'/cinsulin_seq.txt'
lsinsulin=Path+'/lsinsulin_seq.txt'

with open(Filename, 'r') as myfile:
    data = myfile.read()
    pps_char=sum(len(x) for x in data)
    print(data)
    print("the number of characters in the file is %s" %pps_char)
    '''
    1. Programmatically delete “ORIGIN”, “1”, “61”, “//”, and the spaces and return carriages.
    2. Copy your results in the file preproinsulin_seq_clean.txt.
    3. Verify that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin
    '''
    preproinsulin_seq_clean=data.translate({ord(i): None for i in ('\n ORIGIN161 //')}) #this will remove any character in the string specified
    print(preproinsulin_seq_clean)
    ppsc_char = sum(len(x) for x in preproinsulin_seq_clean)
    print("the number of characters in the preproinsulin_seq_clean file is %s" %ppsc_char)

    '''
    Save amino acids 1-24 as lsinsulin_seq_clean.txt. 
    Verify that your file has 24 characters.
    '''
    ls_isc=preproinsulin_seq_clean[0:24]
    len_ls_isc=sum(len(x) for x in ls_isc)
    print("the number of characters in the lsinsulin_seq_clean file is %s" %len_ls_isc)

    '''
    Save amino acids 25-54 as binsulin_seq_clean.txt. 
    Verify that your file has 30 characters.
    '''
    b_isc=preproinsulin_seq_clean[24:54]
    len_b_isc=sum(len(x) for x in b_isc)
    print("the number of characters in the binsulin_seq_clean file is %s" %len_b_isc)

    '''
    Save amino acids 55-89 as cinsulin_seq_clean.txt. 
    Verify that your file has 35 characters.
    '''
    c_isc=preproinsulin_seq_clean[54:89]
    len_c_isc=sum(len(x) for x in c_isc)
    print("the number of characters in the cinsulin_seq_clean file is %s" %len_c_isc)

    '''
    Save amino acids 90-110 as ainsulin_seq_clean.txt. 
    Verify that your file has 21 characters.
    '''
    a_isc = preproinsulin_seq_clean[89:110]
    len_a_isc = sum(len(x) for x in a_isc)
    print("the number of characters in the ainsulin_seq_clean file is %s" % len_a_isc)

#writing o/p to text files
with open(ainsulin, 'w') as writer:
    writer.write(a_isc)
with open(binsulin, 'w') as writer:
    writer.write(b_isc)
with open(cinsulin, 'w') as writer:
    writer.write(c_isc)
with open(lsinsulin, 'w') as writer:
    writer.write(ls_isc)

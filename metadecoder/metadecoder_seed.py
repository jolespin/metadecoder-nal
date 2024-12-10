import os
import shutil
from datetime import datetime
from math import inf
from collections import defaultdict

import metadecoder

from .fasta_utility import read_fasta_file
from .make_file import make_file
from .run_subprocess import run_pyrodigal, run_pyhmmsearch

def parse_sequence_id(protein_fasta):
    protein_to_contig  = dict()
    with open(protein_fasta, 'r') as open_file:
        for line in open_file:
            line = line.strip()
            if line.startswith('>'):
                id_protein = line[1:].split(" ", maxsplit=1)[0]
                id_contig = id_protein.rsplit("_", maxsplit=1)[0]
                protein_to_contig[id_protein] = id_contig
    return protein_to_contig

# def parse_sequence_id(proteins, contig_to_):
#     '''
#     fraggenescan: >id_start_end_strand
#     '''
#     gene = 1
#     output = os.path.basename(file) + '.proteins'
#     open_file = open(output, 'w')
#     for sequence_id, sequence in read_fasta_file(file):
#         open_file.write('>' + str(gene) + '_' + sequence_id.rsplit('_', maxsplit = 3)[0] + '\n')
#         open_file.write(sequence + '\n')
#         gene += 1
#     open_file.close()
#     return output
# def read_hmm_file(input_hmm):
#     model2tc = dict()
#     open_file = open(input_hmm, 'r')
#     for line in open_file:
#         if line.startswith('NAME'):
#             model = line.rstrip('\n').split()[1]
#         elif line.startswith('TC'):
#             score1, score2 = line.rstrip(';\n').split()[1 : ]
#             model2tc[model] = (float(score1), float(score2))
#     open_file.close()
#     return model2tc


def get_seeds(file, output, protein_to_contig):
    model2sequences = defaultdict(list)
    open_file = open(file, 'r', encoding = 'utf-8')
    next(open_file)
    for line in open_file:
        line = line.strip()
        if line:
            if not line.startswith('#'):
                id_protein, id_hmm, *tmp = line.split()
                id_contig = protein_to_contig[id_protein]
                model2sequences[id_hmm].append(id_contig)
                
    open_file.close()
    open_file = open(output, 'w')
    for model, contigs in model2sequences.items():
        print(model, *contigs, sep = '\t', file = open_file)
    open_file.close()


def main(parameters):
    
    # protein_output = make_file()
    protein_output = parameters.output + ".faa"
    remove_protein_file = False
    if parameters.proteins:
        protein_output = parameters.proteins
        if parameters.proteins_to_contigs:
            protein_to_contig = dict()
            with open(parameters.proteins_to_contigs, 'r') as open_file:
                for line in open_file:
                    if not line.startswith('#'):
                        line = line.strip()
                        id_protein, id_contig = line.split()
                        protein_to_contig[id_protein] = id_contig
        else:
            protein_to_contig  = parse_sequence_id(protein_output)

    else: 
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', 'Identifying protein sequences.', flush = True)
        run_pyrodigal(
            shutil.which("pyrodigal"),
            parameters.fasta, 
            protein_output, 
            parameters,
        )
        protein_to_contig  = parse_sequence_id(protein_output)
        remove_protein_file = True
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', 'Done.', flush = True)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', 'Mapping marker genes to protein sequences.', flush = True)
    pyhmmsearch_output =  parameters.output + ".pyhmmsearch.tsv"
    run_pyhmmsearch(
            shutil.which("pyhmmsearch"),
            protein_output, 
            pyhmmsearch_output, 
            parameters
    )
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', 'Done.', flush = True)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', f'Writing to file: {parameters.output}', flush = True)
    if remove_protein_file:
        if parameters.remove_intermediate_files:
            os.remove(protein_output)
    # model2tc = read_hmm_file(os.path.join(os.path.dirname(metadecoder.__file__), 'markers.hmm'))
    get_seeds(pyhmmsearch_output,parameters.output, protein_to_contig)
    if parameters.remove_intermediate_files:
        os.remove(pyhmmsearch_output)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '->', 'Finished.', flush = True)

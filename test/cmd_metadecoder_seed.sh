ASSEMBLY="S1_scaffolds.fasta"
OUTPUT_DIRECTORY="seed_no_proteins"
mkdir -p ${OUTPUT_DIRECTORY}
metadecoder seed -f ${ASSEMBLY} --threads 12 -o ${OUTPUT_DIRECTORY}/output.seed

OUTPUT_DIRECTORY="seed_with_proteins"
mkdir -p ${OUTPUT_DIRECTORY}
metadecoder seed -f ${ASSEMBLY} --threads 12 -o ${OUTPUT_DIRECTORY}/output.seed -a S1_scaffolds.faa

OUTPUT_DIRECTORY="seed_with_proteins_and_mapping"
mkdir -p ${OUTPUT_DIRECTORY}
metadecoder seed -f ${ASSEMBLY} --threads 12 -o ${OUTPUT_DIRECTORY}/output.seed -a S1_scaffolds.faa --proteins_to_contigs S1_scaffolds.proteins_to_contigs.tsv


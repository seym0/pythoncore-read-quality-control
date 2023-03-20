import gzip

def unpack_gz(path_to_archive):
    with gzip.open(path_to_archive, mode='rt', encoding='utf-8') as f:
        lst = f.read().split('\n')
    return lst


# lines = unpack_gz(input())
lines = unpack_gz(r'C:\Users\Liliana\Desktop\data1.gz')

all_sequences = []
lens_of_seqs = []
for i in lines[1::4]:
    all_sequences.append(i)
    lens_of_seqs.append(len(i))
print('Reads in the file =', len(all_sequences))
print('Reads sequence average length =', round(sum(lens_of_seqs) / len(lens_of_seqs), 2))

# repeats
repeats = len(all_sequences) - len(set(all_sequences))
print(f'Repeats = {repeats}')

# percentage of the undefined nucleotides ( N ) per sequence
ns_per_seq = []
for read in all_sequences:
    if read.count('N') != 0:
        ns_per_seq.append(read.count('N') / len(read.rstrip()) * 100)
print('Reads with Ns =', len(ns_per_seq))
print(f'Ns per read sequence = {round(sum(ns_per_seq) / len(all_sequences), 2)}%')

# gc content
gc_cont_av = []
for i in all_sequences:
    gc_cont_av.append(round((i.count('G') + i.count('C')) / len(i) * 100, 2))
print(f'GC content average = {round(sum(gc_cont_av) / len(all_sequences), 2)}%')

# write your code here
import gzip

# path_to_archive1 = r'C:\Users\Liliana\PycharmProjects\Read Quality Control2\Read Quality Control\task\test\data1.gz'
# path_to_archive2 = r'C:\Users\Liliana\PycharmProjects\Read Quality Control2\Read Quality Control\task\test\data2.gz'
# path_to_archive3 = r'C:\Users\Liliana\PycharmProjects\Read Quality Control2\Read Quality Control\task\test\data3.gz'

path_to_archive1 = input()
path_to_archive2 = input()
path_to_archive3 = input()

with gzip.open(path_to_archive1, mode='rt', encoding='utf-8') as f:
    lines_1 = f.read().split('\n')
with gzip.open(path_to_archive2, mode='rt', encoding='utf-8') as f:
    lines_2 = f.read().split('\n')
with gzip.open(path_to_archive3, mode='rt', encoding='utf-8') as f:
    lines_3 = f.read().split('\n')
# with gzip.open(path_to_archive1, 'rt', encoding='utf-8') as f:
# lines_1 = f.read().split('\n')
# with gzip.open(path_to_archive2, 'rt', encoding='utf-8') as f:
# lines_2 = f.read().split('\n')
# with gzip.open(path_to_archive3, 'rt', encoding='utf-8') as f:
# lines_3 = f.read().split('\n')

# d is dict where len: freq of reads
# d = {}

all_sequences_1 = []
lens_1 = []
for i in lines_1[1::4]:
    all_sequences_1.append(i)
    lens_1.append(len(i))
all_sequences_2 = []
lens_2 = []
for i in lines_2[1::4]:
    all_sequences_2.append(i)
    lens_2.append(len(i))
all_sequences_3 = []
lens_3 = []
for i in lines_3[1::4]:
    all_sequences_3.append(i)
    lens_3.append(len(i))

# len_reads = 0
# for key, value in d.items():
# print(f'\twith length {key} = {value}')
# len_reads += int(key) * int(value)
# print('Reads sequence average length =', round(sum(lens_1) / len(lens_1)))
# print('Reads sequence average length =', round(sum(lens_2) / len(lens_2)))
# print('Reads sequence average length =', round(sum(lens_3) / len(lens_3)))

repeats_1 = len(all_sequences_1) - len(set(all_sequences_1))
repeats_2 = len(all_sequences_2) - len(set(all_sequences_2))
repeats_3 = len(all_sequences_3) - len(set(all_sequences_3))

# percentage of the undefined nucleotides ( N ) per sequence
ns_per_seq_1 = []
for read in all_sequences_1:
    if read.count('N') != 0:
        ns_per_seq_1.append(read.count('N') / len(read.rstrip()) * 100)
# print('Reads with Ns =', len(ns_per_seq_1))
ns_per_seq_2 = []
for read in all_sequences_2:
    if read.count('N') != 0:
        ns_per_seq_2.append(read.count('N') / len(read.rstrip()) * 100)
# print('Reads with Ns =', len(ns_per_seq_2))
ns_per_seq_3 = []
for read in all_sequences_3:
    if read.count('N') != 0:
        ns_per_seq_3.append(read.count('N') / len(read.rstrip()) * 100)
# print('Reads with Ns =', len(ns_per_seq_3))

# gc content
gc_cont_av_1 = []
for i in all_sequences_1:
    gc_cont_av_1.append(round((i.count('G') + i.count('C')) / len(i) * 100, 2))
# print(f'GC content average = {round(sum(gc_cont_av_1) / len(all_sequences_1), 2)}%')
# print(f'Ns per read sequence = {round(sum(ns_per_seq_1) / len(all_sequences_1), 2)}%')

gc_cont_av_2 = []
for i in all_sequences_2:
    gc_cont_av_2.append(round((i.count('G') + i.count('C')) / len(i) * 100, 2))
# print(f'GC content average = {round(sum(gc_cont_av_2) / len(all_sequences_2), 2)}%')
# print(f'Ns per read sequence = {round(sum(ns_per_seq_2) / len(all_sequences_2), 2)}%')

gc_cont_av_3 = []
for i in all_sequences_3:
    gc_cont_av_3.append(round((i.count('G') + i.count('C')) / len(i) * 100, 2))
# print(f'GC content average = {round(sum(gc_cont_av_3) / len(all_sequences_3), 2)}%')
# print(f'Ns per read sequence = {round(sum(ns_per_seq_3) / len(all_sequences_3), 2)}%')

# if min(sum(ns_per_seq_1) / len(all_sequences_1), sum(ns_per_seq_2) / len(all_sequences_2), sum(ns_per_seq_3) / len(all_sequences_3)) == sum(ns_per_seq_1) / len(all_sequences_1):
print('Reads in the file =', len(all_sequences_1))
print('Reads sequence average length =', round(sum(lens_1) / len(lens_1)))
print(f'Repeats = {repeats_1}')
print('Reads with Ns =', len(ns_per_seq_1))
print(f'GC content average = {round(sum(gc_cont_av_1) / len(all_sequences_1), 2)}%')
print(f'Ns per read sequence = {round(sum(ns_per_seq_1) / len(all_sequences_1), 2)}%')

# elif min(sum(ns_per_seq_1) / len(all_sequences_1), sum(ns_per_seq_2) / len(all_sequences_2), sum(ns_per_seq_3) / len(all_sequences_3)) == sum(ns_per_seq_2) / len(all_sequences_2):
# print('Reads sequence average length =', round(sum(lens_2) / len(lens_2)))
# print(f'Repeats = {repeats_2}')
# print('Reads with Ns =', len(ns_per_seq_2))
# print(f'GC content average = {round(sum(gc_cont_av_2) / len(all_sequences_2), 2)}%')
# print(f'Ns per read sequence = {round(sum(ns_per_seq_2) / len(all_sequences_2), 2)}%')
# elif min(sum(ns_per_seq_1) / len(all_sequences_1), sum(ns_per_seq_2) / len(all_sequences_2), sum(ns_per_seq_3) / len(all_sequences_3)) == sum(ns_per_seq_3) / len(all_sequences_3):
# print('Reads sequence average length =', round(sum(lens_3) / len(lens_3)))
# print(f'Repeats = {repeats_3}')
# print('Reads with Ns =', len(ns_per_seq_3))
# print(f'GC content average = {round(sum(gc_cont_av_3) / len(all_sequences_3), 2)}%')
# print(f'Ns per read sequence = {round(sum(ns_per_seq_3) / len(all_sequences_3), 2)}%')

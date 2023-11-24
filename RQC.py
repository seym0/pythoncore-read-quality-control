import gzip
import numpy as np


def unpack_gz(path_to_archive):
    with gzip.open(path_to_archive, mode="rt", encoding="utf-8") as f:
        lst = f.read().split("\n")
    return lst


def process_archive(path_to_archive):
    content = unpack_gz(path_to_archive)
    # number of reads and their average length
    all_seqs, lens_of_seqs = [], []
    for line in content[1::4]:
        all_seqs.append(line)
        lens_of_seqs.append(len(line.rstrip()))
    print("Reads in the file =", len(all_seqs))
    print("Reads sequence average length =", round(np.mean(lens_of_seqs), 2))

    # repeats
    repeats = len(all_seqs) - len(set(all_seqs))
    print(f"Repeats = {repeats}")

    # percentage of the undefined nucleotides ( N ) per sequence
    ns_per_seq = []
    for read in all_seqs:
        if read.count("N") != 0:
            ns_per_seq.append(read.count("N") / len(read.rstrip()) * 100)
    print("Reads with Ns =", len(ns_per_seq))
    print(f"Ns per read sequence = {round(sum(ns_per_seq)/len(all_seqs), 2)}%")

    # gc content
    gc_cont_av = []
    for read in all_seqs:
        gc_cont_av.append(
            round((read.count("G") + read.count("C"))/len(read) * 100, 2)
        )
    print(f"GC content average = {round(sum(gc_cont_av)/len(all_seqs), 2)}%")


process_archive("data1.gz")
print("the first archive has been processed")
print()
process_archive("data2.gz")
print("the second archive has been processed")
print()
process_archive("data3.gz")
print("the third archive has been processed")

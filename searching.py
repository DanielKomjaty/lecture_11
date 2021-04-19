import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None


    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]

def linear_search(seqs, wanted_number):
    pozice = []
    pocet = 0
    for random in range(0, len(seqs)):
        if seqs[random] == wanted_number:
            pozice.append(random + 1)
            pocet += 1

    vysledek = {"positions": pozice, "count": pocet}
    return vysledek


def pattern_search(seqs, pattern):
    pozice = set()
    idx = 0
    while idx <= (len(seqs) - len(pattern)):
        if seqs[idx:(idx + len(pattern))] == pattern:
            pozice.add(f"{idx + 1}:{(idx + len(pattern))}")
        idx += 1
    return pozice






def main():
    seqs = read_data("sequential.json", "unordered_numbers")

    print(linear_search(seqs, 0))

    seqs = read_data("sequential.json", "dna_sequence")

    print(pattern_search(seqs, pattern="ATA"))

if __name__ == '__main__':
    main()
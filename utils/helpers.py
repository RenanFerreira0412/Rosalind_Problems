import os
import json


class Helpers:
    __codons = []

    # invertendo a string
    @classmethod
    def reverse(cls, complement: str):
        comple_size = len(complement)
        arr = [None] * comple_size

        for i in range(comple_size//2+1):
            j = comple_size - i - 1
            # invertendo as posições
            arr[j], arr[i] = complement[i], complement[j]

        return ''.join(arr)

    # complemeto do dna
    @classmethod
    def complement_of(cls, dna: str):
        comple = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

        c = ""

        for base in dna:
            c += comple[base]

        return c

    # transcrição - DNA -> RNA
    @classmethod
    def transcribe(cls, dna: str):
        rna = ""

        for base in dna:
            if base == 'T':
                rna += 'U'
                continue
            rna += base

        return rna

    # tabela de códons
    @classmethod
    def __get_codons(cls):
        try:
            path = os.path.realpath("codons.json")
            input_data = open(path, 'r')
            cls.codons = json.load(input_data)
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo .json!")

    # traduzir rna para uma sequência de aminoácidos (proteína)
    @classmethod
    def translate(cls, rna: str):
        cls.__get_codons()

        protein = ""
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            protein += cls.codons[codon]
        return protein


helpers = Helpers()

import os
import requests


class FRMTSolution:
    def __init__(self):
        # GenBank entry IDs
        self.ids = []
        self.fasta_files = []
        self.size_dna_seq = []
        self.shortest_line_size = 0

        self.get_ids()
        self.get_data()

    # recebendo os ids de acesso
    def get_ids(self):
        try:
            path = os.path.realpath("../../input/rosalind_frmt.txt")
            input_data = open(path, 'r')
            # linha de texto
            line = input_data.readline().split()
            # IDs
            self.ids = [id.strip() for id in line]
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # recebendo os dados
    def fetch_data(self, id):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
        search_param = f'db=nucleotide&id={id}&rettype=fasta'

        url = f"{base_url}{search_param}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                # dados
                data = response.text
                # linhas de texto do arquivo
                lines = data.strip().split('\n')
                # sequência de dna do arquivo
                dna = ''.join(lines[1::])
                # adicionando o tamanho da sequência de DNA
                self.size_dna_seq.append(len(dna))
                # adicionando os arquivos
                self.fasta_files.append(data)

        except requests.HTTPError as e:
            print(f"Erro ao carregar os dados: {e}")

    # verificando o índice do tamanho menor linha
    def get_index_shortest_line_size(self):
        lower = 0
        value = self.size_dna_seq[0]
        for i in range(1, len(self.size_dna_seq)):
            if self.size_dna_seq[i] < value:
                value = self.size_dna_seq[i]
                lower = i
        return lower

    # recebendo os dados dos arquivos .fasta

    def get_data(self):
        for id in self.ids:
            # carregando os dados
            self.fetch_data(id)

    def write_data(self):
        i = self.get_index_shortest_line_size()
        print(self.size_dna_seq)
        try:
            path = os.path.realpath("../../output/FRMT.txt")
            output_data = open(path, 'w')
            output_data.write(self.fasta_files[i])
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = FRMTSolution()
    solution.write_data()
